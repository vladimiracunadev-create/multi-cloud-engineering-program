"""Generate the complete curriculum from the canonical catalog.

Generated files are committed on purpose: learners can browse the course without
installing Python, while maintainers keep numbering and navigation deterministic.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

from course_data import LAB_EXPECTATIONS, PARTS

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ROOT / "classes"


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return value


def keywords(title: str) -> list[str]:
    stop = {"de", "del", "la", "las", "los", "y", "en", "con", "por", "para", "a", "como", "un", "una"}
    words = [w.lower() for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+", title)]
    return [w for w in words if w not in stop][:6]


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def build_catalog() -> list[dict]:
    catalog = []
    number = 1
    for part_no, part in enumerate(PARTS):
        for class_no, (title, lab_kind, artifact) in enumerate(part["classes"], start=1):
            catalog.append(
                {
                    "id": f"{number:03d}",
                    "number": number,
                    "title": title,
                    "slug": slugify(title),
                    "part": f"{part_no:02d}",
                    "part_slug": part["slug"],
                    "part_title": part["title"],
                    "part_class": class_no,
                    "level": part["level"],
                    "estimated_hours": 8 if lab_kind == "capstone" else 4,
                    "lab_kind": lab_kind,
                    "artifact": artifact,
                    "keywords": keywords(title),
                    "books": part["books"],
                    "status": "EXECUTABLE_CORE",
                    "maturity": "stable" if part_no < 10 else "evolving",
                }
            )
            number += 1
    return catalog


def lesson_readme(item: dict, part: dict, previous: dict | None, following: dict | None) -> str:
    concept_rows = "\n".join(
        f"| `{concept}` | Define su papel en **{item['title'].lower()}** y cómo observarlo en un sistema real. |"
        for concept in item["keywords"]
    )
    books = "\n".join(f"- {book}." for book in item["books"])
    prev_link = "Inicio del programa" if previous is None else f"[← Clase anterior](../../part-{previous['part']}-{previous['part_slug']}/{previous['id']}-{previous['slug']}/README.md)"
    next_link = "Fin del programa" if following is None else f"[Clase siguiente →](../../part-{following['part']}-{following['part_slug']}/{following['id']}-{following['slug']}/README.md)"
    expected = LAB_EXPECTATIONS[item["lab_kind"]]
    return f"""# {item['id']} — {item['title']}

> {prev_link} · [Índice de la parte](../README.md) · {next_link}

**Parte:** {item['part']} — {item['part_title']}  
**Nivel:** {item['level']} · **Horas estimadas:** {item['estimated_hours']}  
**Laboratorio:** `{item['lab_kind']}` · **Estado:** `{item['status']}`

## 🎯 Propósito

Comprender y aplicar **{item['title'].lower()}** dentro de una plataforma cloud realista,
produciendo evidencia reproducible y una decisión que explicite seguridad, confiabilidad,
costo y operación. La meta no es memorizar nombres de servicios: es reconocer el problema,
seleccionar una solución proporcional y demostrar qué ocurrió.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Explicar** {item['title'].lower()} con vocabulario independiente del proveedor.
2. **Relacionar** sus componentes con el modelo mental de la parte.
3. **Ejecutar** un laboratorio local determinista y leer su contrato JSON.
4. **Evaluar** al menos una alternativa y justificar el trade-off elegido.
5. **Entregar** `{item['artifact']}` con evidencia, límites y criterio de reversión.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
{concept_rows}

## 🧠 Modelo mental

{part['model']}

Aplicado a esta clase, separa siempre cuatro planos: **intención** (qué necesita el usuario),
**configuración** (qué declaramos), **estado observado** (qué existe de verdad) y
**evidencia** (cómo sabemos que cumple). Confundirlos produce diseños que se ven correctos
en un diagrama pero fallan al operar.

## 🗺️ Flujo de razonamiento

```mermaid
flowchart LR
    A["Necesidad y restricciones"] --> B["Diseño: {item['title']}"]
    B --> C["Implementación reproducible"]
    C --> D["Estado observado"]
    D --> E{{"¿Cumple seguridad, SLO y costo?"}}
    E -- "No" --> B
    E -- "Sí" --> F["Evidencia y decisión registrada"]
```

## 📖 Desarrollo

### 1. Del requisito al mecanismo

Empieza por una frase medible: quién consume la capacidad, bajo qué carga, desde dónde,
con qué datos y qué impacto tendría un fallo. Después identifica el mecanismo de esta clase
que satisface cada restricción. Un producto cloud solo es una implementación posible; el
requisito permanece aunque cambies de AWS a Azure, Google Cloud o infraestructura propia.

### 2. Fronteras y responsabilidades

Documenta quién administra identidad, red, datos, runtime y observabilidad. Marca qué queda
en manos del proveedor y qué sigue siendo responsabilidad del equipo. Cada frontera debe
tener propietario, interfaz, señal operativa y forma de recuperación. Si una responsabilidad
no tiene dueño, el diseño todavía está incompleto.

### 3. Compensaciones que deben quedar visibles

| Dimensión | Pregunta de diseño |
|---|---|
| Confiabilidad | ¿Qué falla, cómo se detecta y cuánto tarda en recuperarse? |
| Seguridad | ¿Qué identidad actúa y cuál es el mínimo privilegio necesario? |
| Costo | ¿Cuál es la unidad de consumo y qué hace crecer la factura? |
| Operación | ¿Qué señal permite diagnosticarlo sin entrar manualmente al servidor? |
| Portabilidad | ¿Qué contrato es estándar y qué decisión es específica del proveedor? |

La respuesta correcta puede ser más simple que la arquitectura inicialmente imaginada. En
cloud, complejidad también consume presupuesto de error, tiempo de equipo y capacidad de
respuesta a incidentes.

## 🔬 Ejemplo trabajado

Una plataforma de pedidos necesita aplicar **{item['title'].lower()}**. El equipo registra:

- demanda base de 20 solicitudes/s y pico de 120 solicitudes/s;
- SLO mensual de 99,9 % para operaciones de lectura;
- RPO de 15 minutos y RTO de 60 minutos;
- datos personales que no pueden salir de la región aprobada;
- presupuesto inicial de USD 600/mes.

La decisión se acepta solo si explica cómo la propuesta responde a esas cinco restricciones.
Se descarta cualquier alternativa que dependa de acceso administrativo permanente, no tenga
telemetría o cuyo costo no pueda atribuirse. El resultado esperado no es "usar servicio X",
sino una cadena trazable: requisito → mecanismo → prueba → señal → límite.

## 🧪 Laboratorio guiado

Ejecuta desde la raíz:

```bash
python classes/part-{item['part']}-{item['part_slug']}/{item['id']}-{item['slug']}/lab.py
```

El laboratorio reutiliza un motor didáctico probado y produce `lab_result.json`. Su objetivo
es practicar el contrato antes de depender de credenciales o una cuenta con costo.

1. Ejecuta con la semilla predeterminada y conserva la salida.
2. Repite con `--seed 42`; confirma qué cambia y qué permanece estable.
3. Revisa `decision`, `evidence`, `limitations` y `cost_units`.
4. Añade una prueba negativa relacionada con el tema de la clase.
5. Documenta por qué la simulación no equivale a una validación en producción.

### Evidencia esperada

El artefacto principal es {expected}. Además, la entrega debe incluir el comando ejecutado,
la salida estructurada y una conclusión que no exceda lo observado.

## 🏆 Reto verificable

Construye **`{item['artifact']}`** para el caso CloudShop. Incluye una alternativa descartada,
un supuesto que pueda falsarse, una prueba de fallo y una decisión de rollback.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0 y genera JSON válido.
- [ ] La entrega conecta al menos tres requisitos con mecanismos verificables.
- [ ] Existe una prueba positiva y una prueba negativa con evidencia.
- [ ] Seguridad, costo y operación aparecen como decisiones, no como anexos.
- [ ] Se declara una limitación y una condición que obligaría a revisar el diseño.
- [ ] Otra persona puede repetir el recorrido sin conocimiento tácito.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El diseño enumera servicios pero no requisitos | Se comenzó por el catálogo del proveedor | Reescribe primero escenarios y restricciones medibles. |
| La demo funciona una vez y se declara lista | Se confundió ejecución con evidencia operacional | Añade repetición, fallo, telemetría y recuperación. |
| Todo tiene permisos administrativos | El laboratorio heredó credenciales humanas | Usa identidad de workload y prueba explícitamente la denegación. |
| No se puede explicar la factura | Faltan unidades y ownership de costo | Etiqueta, estima por unidad y define presupuesto o alerta. |
| La solución se llama multi-cloud pero replica todo | Portabilidad se confundió con duplicación | Define qué riesgo se mitiga y porta solo el contrato necesario. |

## 🛡️ Seguridad, ética y costo

Trabaja con cuentas propias o sandboxes autorizados. No publiques secretos, identificadores
reales ni datos personales. Antes de crear recursos pagos define presupuesto, etiquetas y
comando de destrucción; después verifica que no queden recursos huérfanos. Los ejemplos
locales enseñan contratos, pero no certifican cumplimiento ni disponibilidad de producción.

## ❓ Preguntas de comprobación

1. ¿Qué parte del diseño seguiría siendo válida en otro proveedor?
2. ¿Qué señal distinguiría saturación, fallo de dependencia y error de configuración?
3. ¿Cuál es la unidad de costo y quién puede actuar sobre ella?
4. ¿Qué permiso puede retirarse sin romper el caso de uso?
5. ¿Qué evidencia falta para afirmar que esto está listo para producción?

## 🔗 Referencias

{books}
- Documentación oficial vigente del servicio implementado; registra URL y fecha de consulta.

---

> [Evaluación](assessment.md) · [Contrato de clase](lesson.yaml) · [Índice de la parte](../README.md)
"""


def assessment(item: dict) -> str:
    return f"""# Evaluación — {item['id']} {item['title']}

## Preguntas

1. Explica el problema que resuelve esta capacidad sin mencionar un proveedor.
2. Identifica una frontera de responsabilidad y su propietario.
3. Compara dos alternativas mediante confiabilidad, seguridad, costo y operación.
4. ¿Qué demuestra el laboratorio y qué no puede demostrar?
5. Propón un caso límite o una prueba de fallo.

## Reto verificable

Entrega `{item['artifact']}` con diagrama o configuración, evidencia de ejecución,
alternativa descartada, riesgo residual y criterio de rollback.

## Criterio de aceptación

- [ ] Resultado reproducible por una segunda persona.
- [ ] Evidencia vinculada a cada afirmación técnica.
- [ ] Prueba negativa o de fallo incluida.
- [ ] Costos y permisos expresados con unidades y alcance.
- [ ] Limitaciones declaradas sin presentar la simulación como producción.

## Escala

| Nivel | Evidencia |
|---|---|
| A — competente | Cumple todo y defiende trade-offs con datos. |
| B — en desarrollo | Cumple lo esencial; falta profundidad en una dimensión. |
| C — inicial | Artefacto parcial o conclusión sin evidencia suficiente. |
| 0 | Sin entrega reproducible. |
"""


def lesson_yaml(item: dict) -> str:
    key_lines = "\n".join(f"  - {yaml_quote(k)}" for k in item["keywords"])
    return f"""id: {yaml_quote(item['id'])}
number: {item['number']}
title: {yaml_quote(item['title'])}
part: {yaml_quote(item['part'])}
level: {yaml_quote(item['level'])}
estimated_hours: {item['estimated_hours']}
lab_kind: {yaml_quote(item['lab_kind'])}
artifact: {yaml_quote(item['artifact'])}
status: {yaml_quote(item['status'])}
maturity: {yaml_quote(item['maturity'])}
keywords:
{key_lines}
"""


def lab_entrypoint(item: dict) -> str:
    return f'''"""Executable lab for lesson {item["id"]}."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="{item['id']}", kind="{item['lab_kind']}"))
'''


def part_readme(part_no: int, part: dict, items: list[dict]) -> str:
    rows = "\n".join(
        f"| {x['id']} | [{x['title']}]({x['id']}-{x['slug']}/README.md) | `{x['lab_kind']}` | {x['estimated_hours']} |"
        for x in items
    )
    books = "\n".join(f"- {book}." for book in part["books"])
    previous = "Programa" if part_no == 0 else f"[← Parte {part_no - 1:02d}](../part-{part_no - 1:02d}-{PARTS[part_no - 1]['slug']}/README.md)"
    following = "Fin" if part_no == len(PARTS) - 1 else f"[Parte {part_no + 1:02d} →](../part-{part_no + 1:02d}-{PARTS[part_no + 1]['slug']}/README.md)"
    return f"""# Parte {part_no:02d} — {part['title']}

> {previous} · [Índice completo](../README.md) · {following}

**Nivel:** {part['level']} · **Clases:** 12 · **Duración sugerida:** 6–8 semanas

{part['focus']}

## Resultados de la parte

Al completar esta parte podrás explicar el dominio con lenguaje independiente del proveedor,
implementar sus mecanismos esenciales, diagnosticar fallos y defender decisiones mediante
evidencia, costo, seguridad y objetivos de confiabilidad.

## Modelo mental

{part['model']}

## Secuencia

```mermaid
flowchart LR
    A["Conceptos"] --> B["Implementación guiada"]
    B --> C["Pruebas y fallos"]
    C --> D["Operación"]
    D --> E["Proyecto integrador"]
```

## Clases

| ID | Clase | Laboratorio | Horas |
|---:|---|---|---:|
{rows}

## Evaluación de la parte

- 35 % laboratorios y evidencia reproducible.
- 25 % retos verificables.
- 20 % decisiones y ADR.
- 10 % seguridad, confiabilidad y costo.
- 10 % proyecto integrador de la parte.

Se aprueba con 80 % de clases en nivel B o superior y el proyecto integrador reproducible.

## Pauta bibliográfica

{books}
"""


def classes_index(catalog: list[dict]) -> str:
    rows = []
    for part_no, part in enumerate(PARTS):
        start = part_no * 12 + 1
        end = start + 11
        path = f"part-{part_no:02d}-{part['slug']}/README.md"
        rows.append(f"| {part_no:02d} | [{part['title']}]({path}) | {start:03d}–{end:03d} | 12 | {part['level']} |")
    return f"""# Índice completo de clases

**180 clases · 15 partes · 788 horas estimadas · inicial → experto-frontera**

El orden es deliberado. Cada parte cierra con un proyecto que aporta evidencia al capstone
continuo **CloudShop**. Quien ya domina fundamentos puede usar las rutas por rol, pero debe
validar los prerrequisitos con los retos de entrada.

| Parte | Tema | Clases | Cantidad | Nivel |
|---:|---|---:|---:|---|
{chr(10).join(rows)}

## Contrato de una clase

```text
classes/part-XX-slug/NNN-topic/
├── README.md       teoría, ejemplo, práctica, errores y referencias
├── assessment.md   preguntas, reto y criterio de aceptación
├── lesson.yaml     metadatos verificables
└── lab.py          entrypoint ejecutable del motor didáctico
```
"""


def generate() -> None:
    catalog = build_catalog()
    for index, item in enumerate(catalog):
        part_no = int(item["part"])
        part = PARTS[part_no]
        folder = CLASSES / f"part-{item['part']}-{item['part_slug']}" / f"{item['id']}-{item['slug']}"
        folder.mkdir(parents=True, exist_ok=True)
        previous = catalog[index - 1] if index else None
        following = catalog[index + 1] if index + 1 < len(catalog) else None
        (folder / "README.md").write_text(lesson_readme(item, part, previous, following), encoding="utf-8")
        (folder / "assessment.md").write_text(assessment(item), encoding="utf-8")
        (folder / "lesson.yaml").write_text(lesson_yaml(item), encoding="utf-8")
        (folder / "lab.py").write_text(lab_entrypoint(item), encoding="utf-8")

    for part_no, part in enumerate(PARTS):
        part_items = [x for x in catalog if x["part"] == f"{part_no:02d}"]
        part_folder = CLASSES / f"part-{part_no:02d}-{part['slug']}"
        (part_folder / "README.md").write_text(part_readme(part_no, part, part_items), encoding="utf-8")

    CLASSES.mkdir(exist_ok=True)
    (CLASSES / "README.md").write_text(classes_index(catalog), encoding="utf-8")
    data_folder = ROOT / "curriculum"
    data_folder.mkdir(exist_ok=True)
    serialized = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    (data_folder / "catalog.json").write_text(serialized, encoding="utf-8")
    site_folder = ROOT / "site"
    site_folder.mkdir(exist_ok=True)
    (site_folder / "catalog.json").write_text(serialized, encoding="utf-8")
    print(f"Generated {len(catalog)} classes in {len(PARTS)} parts.")


if __name__ == "__main__":
    sys.exit(generate())
