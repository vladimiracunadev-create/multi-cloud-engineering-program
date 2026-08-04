"""Build the Android APK straight from the Android SDK build tools.

No Gradle on purpose: the app is a single activity that loads the already
generated `site/` from the assets, so the whole build is aapt2 + javac + d8 +
apksigner. That keeps the release reproducible from a checkout with only the
SDK and a JDK installed.

Usage:
    python scripts/build_apk.py [--sdk PATH] [--out output/android]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANDROID = ROOT / "android"
SITE = ROOT / "site"
PACKAGE = "dev.vladimiracuna.multicloud"
APK_NAME = "multi-cloud-engineering-program.apk"

# El manual pesa 8 MiB y ya se descarga del portal: no viaja dentro de la APK.
ASSET_EXCLUDES = {"downloads"}


def newest(folder: Path) -> Path:
    def key(path: Path) -> tuple[int, ...]:
        parts = []
        for chunk in path.name.replace("android-", "").split("."):
            parts.append(int(chunk) if chunk.isdigit() else 0)
        return tuple(parts)

    candidates = [p for p in folder.iterdir() if p.is_dir()]
    if not candidates:
        raise SystemExit(f"no hay componentes del SDK en {folder}")
    return max(candidates, key=key)


def find_sdk(explicit: str | None) -> Path:
    for candidate in (
        explicit,
        os.environ.get("ANDROID_HOME"),
        os.environ.get("ANDROID_SDK_ROOT"),
        Path.home() / "AppData" / "Local" / "Android" / "Sdk",
        Path.home() / "Android" / "Sdk",
        Path.home() / "Library" / "Android" / "sdk",
    ):
        if candidate and Path(candidate).is_dir():
            return Path(candidate)
    raise SystemExit("no se encontro el SDK de Android; usa --sdk")


def complete_jdk(bindir: Path) -> bool:
    """Un JDK sirve solo si tiene las tres: compilar, empaquetar y firmar."""
    return all(
        (bindir / f"{name}.exe").exists() or (bindir / name).exists()
        for name in ("javac", "jar", "keytool")
    )


def find_jdk() -> Path:
    javac = shutil.which("javac")
    if javac:
        # En Windows javapath son enlaces a un JRE sin javac real: se comprueba.
        candidate = Path(javac).resolve().parent
        if complete_jdk(candidate):
            return candidate
    for base in (Path("C:/Program Files/Java"), Path("/usr/lib/jvm"), Path("/Library/Java/JavaVirtualMachines")):
        if not base.is_dir():
            continue
        for jdk in sorted(base.iterdir(), reverse=True):
            for bindir in (jdk / "bin", jdk / "Contents" / "Home" / "bin"):
                if complete_jdk(bindir):
                    return bindir
    raise SystemExit("no se encontro un JDK completo (javac, jar y keytool)")


def run(command: list[str], **kwargs) -> None:
    result = subprocess.run(command, capture_output=True, text=True, **kwargs)
    if result.returncode != 0:
        sys.stderr.write(result.stdout + "\n" + result.stderr + "\n")
        raise SystemExit(f"fallo: {Path(command[0]).name} ({result.returncode})")


def tool(folder: Path, name: str) -> str:
    for suffix in (".exe", ".bat", ""):
        candidate = folder / f"{name}{suffix}"
        if candidate.exists():
            return str(candidate)
    raise SystemExit(f"no se encontro {name} en {folder}")


def site_files() -> list[tuple[Path, str]]:
    """Los assets del curso, con su ruta dentro del APK siempre en formato POSIX."""
    entries = []
    for source in sorted(SITE.rglob("*")):
        if source.is_dir():
            continue
        relative = source.relative_to(SITE)
        if relative.parts and relative.parts[0] in ASSET_EXCLUDES:
            continue
        entries.append((source, "assets/site/" + relative.as_posix()))
    return entries


def add_entries(apk: Path, entries: list[tuple[Path, str]]) -> None:
    """aapt2 en Windows escribe los assets con '\\' y AssetManager no los
    encuentra: se anaden aqui, con separadores POSIX, en vez de con -A."""
    with zipfile.ZipFile(apk, "a", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source, name in entries:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes())


def build(sdk: Path, out: Path) -> Path:
    build_tools = newest(sdk / "build-tools")
    platform = newest(sdk / "platforms")
    android_jar = platform / "android.jar"
    if not android_jar.exists():
        raise SystemExit(f"falta android.jar en {platform}")
    jdk = find_jdk()

    work = out / "build"
    shutil.rmtree(work, ignore_errors=True)
    (work / "compiled").mkdir(parents=True)
    (work / "classes").mkdir(parents=True)
    (work / "dex").mkdir(parents=True)

    entries = site_files()
    asset_files = len(entries)
    asset_bytes = sum(source.stat().st_size for source, _ in entries)

    # 1. recursos
    resource_files = sorted(str(p) for p in (ANDROID / "res").rglob("*") if p.is_file())
    run([tool(build_tools, "aapt2"), "compile", "-o", str(work / "compiled"), *resource_files])
    flat = sorted(str(p) for p in (work / "compiled").glob("*.flat"))
    unsigned = work / "app-unaligned.apk"
    run([
        tool(build_tools, "aapt2"), "link",
        "-o", str(unsigned),
        "-I", str(android_jar),
        "--manifest", str(ANDROID / "AndroidManifest.xml"),
        "--java", str(work / "gen"),
        "--auto-add-overlay",
        *flat,
    ])

    # 2. codigo
    sources = [str(p) for p in (ANDROID / "src").rglob("*.java")]
    sources += [str(p) for p in (work / "gen").rglob("*.java")]
    run([
        tool(jdk, "javac"), "-source", "17", "-target", "17",
        "-classpath", str(android_jar),
        "-d", str(work / "classes"),
        "-nowarn",
        *sources,
    ])
    class_files = [str(p) for p in (work / "classes").rglob("*.class")]
    run([
        tool(build_tools, "d8"),
        "--lib", str(android_jar),
        "--output", str(work / "dex"),
        "--min-api", "26",
        *class_files,
    ])

    # 3. empaquetado: dex y curso, siempre con rutas POSIX
    add_entries(unsigned, [(work / "dex" / "classes.dex", "classes.dex"), *entries])

    # 4. firma
    keystore = out / "release.keystore"
    if not keystore.exists():
        run([
            tool(jdk, "keytool"), "-genkeypair",
            "-keystore", str(keystore),
            "-storepass", "multicloud", "-keypass", "multicloud",
            "-alias", "multicloud",
            "-keyalg", "RSA", "-keysize", "4096", "-validity", "10950",
            "-dname", "CN=Multi-Cloud Engineering Program, O=vladimiracunadev, C=PE",
        ])

    aligned = work / "app-aligned.apk"
    run([tool(build_tools, "zipalign"), "-p", "-f", "4", str(unsigned), str(aligned)])

    apk = out / APK_NAME
    run([
        tool(build_tools, "apksigner"), "sign",
        "--ks", str(keystore),
        "--ks-pass", "pass:multicloud",
        "--key-pass", "pass:multicloud",
        "--v1-signing-enabled", "true",
        "--v2-signing-enabled", "true",
        "--v3-signing-enabled", "true",
        "--out", str(apk),
        str(aligned),
    ])
    run([tool(build_tools, "apksigner"), "verify", "--print-certs", str(apk)])

    manifest = {
        "schema_version": 1,
        "apk": apk.relative_to(ROOT).as_posix(),
        "package": PACKAGE,
        "version_name": "1.0.0",
        "version_code": 1,
        "min_sdk": 26,
        "target_sdk": 35,
        "build_tools": build_tools.name,
        "platform": platform.name,
        "bundled_asset_files": asset_files,
        "bundled_asset_bytes": asset_bytes,
        "apk_bytes": apk.stat().st_size,
        "apk_sha256": hashlib.sha256(apk.read_bytes()).hexdigest(),
    }
    (out / "apk-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    shutil.rmtree(work, ignore_errors=True)
    print(
        f"{apk} ({apk.stat().st_size / 1048576:.1f} MiB, "
        f"{asset_files} recursos empaquetados, firmada con {build_tools.name})"
    )
    return apk


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sdk")
    parser.add_argument("--out", default="output/android")
    args = parser.parse_args()
    out = (ROOT / args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    build(find_sdk(args.sdk), out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
