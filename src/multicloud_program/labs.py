"""Deterministic, credential-free teaching labs.

The local engine teaches observable contracts before learners spend money in a
cloud account. Provider labs can later replace the simulated adapter while
preserving the same evidence contract.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path
from typing import Any


KIND_RULES = {
    "network": ("segment private traffic and expose only the required port", "connection_path"),
    "iam": ("grant a workload role and deny the administrative action", "access_matrix"),
    "security": ("reduce attack surface and retain auditable evidence", "control_result"),
    "finops": ("select the lowest-cost option that still meets the SLO", "cost_model"),
    "reliability": ("add redundancy only where the recovery objective requires it", "failure_result"),
    "observability": ("correlate a user symptom with one high-signal telemetry path", "telemetry"),
    "metrics": ("choose bounded-cardinality metrics tied to an action", "metric_contract"),
    "sre": ("use the error budget to govern release risk", "slo_result"),
    "incident": ("establish command, stabilize impact, then preserve a timeline", "incident_record"),
    "iac": ("produce a reviewed plan with isolated state and no embedded secrets", "plan_summary"),
    "container": ("run a minimal immutable image without root privileges", "image_report"),
    "kubernetes": ("declare desired state and inspect controller reconciliation", "reconciliation"),
    "data": ("match consistency and access patterns before choosing a store", "data_decision"),
    "messaging": ("make delivery, ordering and poison-message behavior explicit", "delivery_contract"),
    "serverless": ("bound concurrency and make retries idempotent", "invocation_result"),
    "delivery": ("promote one immutable artifact with an automatic rollback signal", "pipeline_result"),
    "gitops": ("reconcile drift from a reviewed source of truth", "drift_result"),
    "platform": ("offer a paved path with a stable interface and escape hatch", "platform_contract"),
    "distributed": ("treat timeout as uncertainty and make repeated work safe", "consistency_trace"),
    "performance": ("compare a baseline with a controlled load and locate saturation", "load_result"),
    "chaos": ("test one failure hypothesis with a stop condition", "experiment_result"),
    "migration": ("group dependencies into reversible migration waves", "wave_plan"),
    "governance": ("encode a preventive guardrail and an auditable exception", "policy_result"),
    "compliance": ("map a control to owner, evidence and review frequency", "control_mapping"),
    "architecture": ("select the simplest design that satisfies quality scenarios", "architecture_decision"),
    "decision": ("compare alternatives with explicit weighted criteria", "decision_matrix"),
    "capstone": ("integrate architecture, delivery, operations and evidence", "capstone_increment"),
}

PRACTICE_STEPS = {
    "network": ["calcula el espacio de direcciones", "construye la tabla de rutas", "prueba conectividad y denegación"],
    "iam": ["define principal, acción y recurso", "concede el mínimo privilegio", "demuestra una denegación esperada"],
    "security": ["modela la amenaza", "aplica el control preventivo o detectivo", "conserva evidencia de eficacia"],
    "iac": ["valida y formatea", "genera un plan sin secretos", "comprueba drift y destrucción"],
    "container": ["construye una imagen reproducible", "inspecciona usuario, capas y SBOM", "ejecuta health check y apagado"],
    "kubernetes": ["aplica estado deseado", "observa reconciliación y eventos", "provoca fallo y verifica recuperación"],
    "data": ["declara patrones de acceso", "modela claves y consistencia", "prueba concurrencia y recuperación"],
    "messaging": ["publica un contrato versionado", "simula reintento y duplicado", "envía el mensaje venenoso a DLQ"],
    "observability": ["formula una pregunta operativa", "correlaciona logs, métricas y trazas", "crea una alerta accionable"],
    "reliability": ["define SLI, RTO y RPO", "inyecta un fallo acotado", "mide detección y recuperación"],
    "architecture": ["escribe escenarios de calidad", "compara estructuras y fronteras", "registra la decisión y fitness function"],
    "capstone": ["integra el incremento", "ejecuta pruebas positivas y de fallo", "empaqueta evidencia y defensa"],
}


def _rule(kind: str) -> tuple[str, str]:
    return KIND_RULES.get(kind, (f"apply the {kind} contract with explicit evidence", "result"))


def run_lab(lesson_id: str, kind: str, seed: int = 7, title: str = "", artifact: str = "evidence-pack") -> dict[str, Any]:
    rng = random.Random(f"{lesson_id}:{kind}:{seed}")
    baseline_rps = rng.randint(18, 42)
    peak_multiplier = rng.choice([3, 4, 5, 6])
    peak_rps = baseline_rps * peak_multiplier
    monthly_budget = rng.choice([300, 450, 600, 900])
    availability_target = rng.choice([99.5, 99.9, 99.95])
    failure_minutes = round((100 - availability_target) / 100 * 30 * 24 * 60, 2)
    decision, evidence_key = _rule(kind)
    digest = hashlib.sha256(f"{lesson_id}:{kind}:{seed}:{decision}".encode()).hexdigest()[:16]
    steps = PRACTICE_STEPS.get(kind, [
        f"define el contrato de {kind}",
        "ejecuta el cambio en un entorno local aislado",
        "verifica resultado, fallo y reversión",
    ])
    return {
        "contract_version": "2.0",
        "lesson_id": lesson_id,
        "kind": kind,
        "title": title or f"Lesson {lesson_id}",
        "artifact": artifact,
        "seed": seed,
        "scenario": {
            "baseline_rps": baseline_rps,
            "peak_rps": peak_rps,
            "monthly_budget_usd": monthly_budget,
            "availability_target_percent": availability_target,
            "allowed_failure_minutes_30d": failure_minutes,
        },
        "decision": decision,
        "exercise": {"mode": "local-safe", "steps": steps, "deliverable": artifact},
        "checks": [
            {"id": "positive", "status": "pass", "evidence": f"positive:{digest}"},
            {"id": "negative", "status": "pass", "evidence": f"denial:{digest}"},
            {"id": "rollback", "status": "pass", "evidence": f"rollback:{digest}"},
        ],
        evidence_key: {
            "status": "simulated-pass",
            "check_id": digest,
            "observed_peak_ratio": peak_multiplier,
        },
        "evidence": [
            f"deterministic-check:{digest}",
            f"capacity:{baseline_rps}->{peak_rps}rps",
            f"availability-budget:{failure_minutes}min/30d",
        ],
        "cost_units": ["requests", "runtime-hours", "stored-gb", "egress-gb"],
        "sandbox": {
            "requires": ["cuenta autorizada", "identidad federada temporal", "presupuesto y etiquetas"],
            "cost_gate": "CLOUD_LAB_ALLOW_COST=1",
            "destroy": "python scripts/cloud_lab.py destroy --lesson " + lesson_id,
        },
        "negative_test": {
            "input": "unauthorized-or-over-capacity",
            "expected": "denied-or-degraded-with-signal",
            "observed": "simulated-denial",
        },
        "limitations": [
            "This is a local deterministic teaching model, not a provider deployment.",
            "Latency, quotas, regional failure and real billing require a sandbox validation.",
            "A passing result is evidence of contract understanding, not production readiness.",
        ],
    }


def main(lesson_id: str | None = None, kind: str | None = None, title: str = "", artifact: str = "evidence-pack") -> int:
    parser = argparse.ArgumentParser(description="Run a deterministic cloud engineering lab")
    parser.add_argument("--lesson-id", default=lesson_id)
    parser.add_argument("--kind", default=kind)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not args.lesson_id or not args.kind:
        parser.error("--lesson-id and --kind are required")
    result = run_lab(args.lesson_id, args.kind, args.seed, title, artifact)
    default_output = Path(__file__).resolve()
    invoked = Path(__import__("sys").argv[0]).resolve()
    if invoked.name == "lab.py":
        default_output = invoked.parent / "lab_result.json"
    else:
        default_output = Path.cwd() / "lab_result.json"
    output = args.output or default_output
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"\nEvidence written to {output}")
    return 0
