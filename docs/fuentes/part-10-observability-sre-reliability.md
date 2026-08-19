# Fuentes de la Parte 10 — Observabilidad, SRE y confiabilidad

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-10-observability-sre-reliability/README.md)

## [121 — Logs, métricas, trazas y eventos como señales](../../classes/part-10-observability-sre-reliability/121-logs-metricas-trazas-y-eventos-como-senales/README.md)

- **OpenTelemetry (2025), *Signals overview*** — métricas, trazas, registros y su correlación<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/concepts/signals) ✅
- **Google SRE (2025), *Monitoring distributed systems*** — señales, alertas y el papel de los cambios<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/monitoring-distributed-systems) ✅
- **Majors et al. (2022), *Observability Engineering*** — preguntas nuevas sobre datos existentes<br>  ↳ libro · [ISBN 9781492076445](https://openlibrary.org/isbn/9781492076445) ✅
- **OpenTelemetry (2025), *Sampling: head and tail*** — qué se descarta en cada estrategia<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/concepts/sampling) ✅
- **Prometheus (2025), *Exemplars*** — salto de una métrica a una traza concreta<br>  ↳ documentación · [prometheus.io](https://prometheus.io/docs/prometheus/latest/feature_flags) ✅

## [122 — Logging estructurado, correlación y retención](../../classes/part-10-observability-sre-reliability/122-logging-estructurado-correlacion-y-retencion/README.md)

- **Honeycomb (2025), *Structured events and wide events*** — una línea ancha por unidad de trabajo<br>  ↳ documentación · [docs.honeycomb.io](https://docs.honeycomb.io/get-started/basics/observability) ✅
- **OpenTelemetry (2025), *Logs data model and correlation*** — campos, atributos y enlace con trazas<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/specs/otel/logs/data-model) ✅
- **OWASP (2025), *Logging cheat sheet*** — qué no registrar nunca y cómo depurar en la emisión<br>  ↳ documentación · [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) ✅
- **Google SRE (2025), *Practical alerting and log volume*** — coste del registro y su papel durante incidentes<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/practical-alerting) ✅
- **Charity Majors (2019), *Logs versus structured events*** — por qué agrupar exige mensaje constante<br>  ↳ documentación · [charity.wtf](https://charity.wtf/2019/02/05/logs-vs-structured-events) ✅

## [123 — Métricas, cardinalidad y modelos RED y USE](../../classes/part-10-observability-sre-reliability/123-metricas-cardinalidad-y-modelos-red-y-use/README.md)

- **Prometheus (2025), *Metric types and naming*** — contadores, medidores, histogramas y resúmenes<br>  ↳ documentación · [prometheus.io](https://prometheus.io/docs/concepts/metric_types) ✅
- **Prometheus (2025), *Instrumentation best practices: labels and cardinality*** — coste del producto de etiquetas<br>  ↳ documentación · [prometheus.io](https://prometheus.io/docs/practices/instrumentation) ✅
- **Wilkie (2018), *The RED method*** — ritmo, errores y duración para servicios<br>  ↳ documentación · [grafana.com](https://grafana.com/blog/2018/08/02/the-red-method-how-to-instrument-your-services) ✅
- **Gregg (2013), *The USE method*** — uso, saturación y errores para recursos<br>  ↳ documentación · [brendangregg.com](https://brendangregg.com/usemethod.html) ✅
- **Google SRE (2025), *The four golden signals*** — latencia, tráfico, errores y saturación<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/monitoring-distributed-systems) ✅

## [124 — Tracing distribuido y OpenTelemetry](../../classes/part-10-observability-sre-reliability/124-tracing-distribuido-y-opentelemetry/README.md)

- **W3C (2025), *Trace Context*** — cabecera estándar de propagación y bit de muestreo<br>  ↳ norma · [w3.org](https://w3.org/TR/trace-context) ✅
- **OpenTelemetry (2025), *Traces: spans, links and context propagation*** — modelo de datos y enlaces<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/concepts/signals/traces) ✅
- **OpenTelemetry (2025), *Collector: processors and exporters*** — muestreo en la cola, depuración y reparto<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/collector) ✅
- **Sigelman et al. (2010), *Dapper, a large-scale distributed systems tracing infrastructure*** — origen del modelo<br>  ↳ documentación · [research.google](https://research.google/pubs/pub36356) ✅
- **Dean et al. (2013), *The tail at scale*** — latencia de cola y respuesta parcial en abanicos<br>  ↳ documentación · [research.google](https://research.google/pubs/pub40801) ✅

## [125 — Dashboards, alertas accionables y fatiga](../../classes/part-10-observability-sre-reliability/125-dashboards-alertas-accionables-y-fatiga/README.md)

- **Google SRE (2025), *Practical alerting and symptom-based paging*** — alertar por síntomas y evitar el ruido<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/practical-alerting) ✅
- **Google SRE (2025), *Being on-call*** — carga sostenible de guardia y sus umbrales<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/being-on-call) ✅
- **Prometheus (2025), *Alerting rules and Alertmanager: grouping, inhibition, silences*** — agrupación y supresión<br>  ↳ documentación · [prometheus.io](https://prometheus.io/docs/alerting/latest/alertmanager) ✅
- **Rob Ewaschuk (2025), *My philosophy on alerting*** — reglas prácticas para decidir qué merece despertar a alguien<br>  ↳ documentación · [docs.google.com](https://docs.google.com/document/d/199PqyG3UsyXlwieHaqbGiWVa8eMWi8zzAn0YfcApr8Q/preview) ✅
- **Grafana (2025), *Dashboard design best practices*** — un panel, una pregunta<br>  ↳ documentación · [grafana.com](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/best-practices) ✅

## [126 — SLI, SLO, SLA y presupuesto de error](../../classes/part-10-observability-sre-reliability/126-sli-slo-sla-y-presupuesto-de-error/README.md)

- **Google SRE (2025), *Service level objectives*** — indicadores, objetivos y presupuesto de error<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/service-level-objectives) ✅
- **Google SRE (2025), *Alerting on SLOs: multiwindow, multi-burn-rate*** — ventanas y ritmos de consumo<br>  ↳ documentación · [sre.google](https://sre.google/workbook/alerting-on-slos) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — cómo elegir indicadores útiles<br>  ↳ documentación · [sre.google](https://sre.google/workbook/implementing-slos) ✅
- **Wilkinson (2025), *SLO implementation patterns*** — proporción de eventos buenos y ventanas móviles<br>  ↳ documentación · [github.com](https://github.com/google/slo-generator) ✅
- **Prometheus (2025), *Histograms and quantiles*** — por qué el intervalo colocado en el objetivo importa<br>  ↳ documentación · [prometheus.io](https://prometheus.io/docs/practices/histograms) ✅

## [127 — Incidentes, severidad, comando y comunicación](../../classes/part-10-observability-sre-reliability/127-incidentes-severidad-comando-y-comunicacion/README.md)

- **Google SRE (2025), *Managing incidents*** — papeles, mando y separación entre coordinar y resolver<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/managing-incidents) ✅
- **Google SRE (2025), *Postmortem culture: learning from failure*** — revisión sin culpa y acciones<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/postmortem-culture) ✅
- **PagerDuty (2025), *Incident response documentation*** — severidad, comunicación y relevos<br>  ↳ documentación · [response.pagerduty.com](https://response.pagerduty.com) ✅
- **Allspaw (2012), *Blameless postmortems and a just culture*** — por qué buscar culpables destruye la información<br>  ↳ documentación · [etsy.com](https://www.etsy.com/codeascraft/blameless-postmortems/) ⏳
- **Atlassian (2025), *Incident communication best practices*** — cadencia fija y contenido de las actualizaciones<br>  ↳ documentación · [atlassian.com](https://atlassian.com/incident-management/incident-communication) ✅

## [128 — Runbooks, playbooks y automatización operativa](../../classes/part-10-observability-sre-reliability/128-runbooks-playbooks-y-automatizacion-operativa/README.md)

- **Google SRE (2025), *Eliminating toil*** — definición, medición y objetivo de reducción<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/eliminating-toil) ✅
- **Google SRE (2025), *Emergency response and playbooks*** — contenido y mantenimiento de los procedimientos<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/emergency-response) ✅
- **PagerDuty (2025), *Runbook documentation*** — estructura y enlace desde la alerta<br>  ↳ documentación · [response.pagerduty.com](https://response.pagerduty.com/oncall/alerting_principles/) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — escala de automatización y sus riesgos<br>  ↳ documentación · [sre.google](https://sre.google/workbook/eliminating-toil) ✅
- **Woods et al. (2010), *Behind Human Error*** — por qué los automatismos que compensan ocultan el deterioro<br>  ↳ documentación · [taylorfrancis.com](https://taylorfrancis.com/books/mono/10.1201/9781315568935/behind-human-error) ✅

## [129 — Capacidad, rendimiento y pruebas de carga](../../classes/part-10-observability-sre-reliability/129-capacidad-rendimiento-y-pruebas-de-carga/README.md)

- **Gunther (2007), *Guerrilla Capacity Planning*** — curva de espera, ley de escalabilidad y márgenes<br>  ↳ artículo · [doi:10.1007/978-3-540-31010-5](https://doi.org/10.1007/978-3-540-31010-5) ✅
- **Tene (2015), *How NOT to measure latency*** — omisión coordinada y modelos abierto y cerrado<br>  ↳ documentación · [infoq.com](https://infoq.com/presentations/latency-response-time) ✅
- **Google SRE (2025), *Managing load and handling overload*** — comportamiento cerca de la saturación y descarte<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/handling-overload) ✅
- **Gregg (2020), *Systems Performance*** — metodología de medición y cuellos de botella<br>  ↳ documentación · [brendangregg.com](https://brendangregg.com/systems-performance-2nd-edition-book.html) ✅
- **k6 (2025), *Test types: smoke, load, stress, soak, spike*** — qué pregunta responde cada una<br>  ↳ documentación · [grafana.com](https://grafana.com/docs/k6/latest/testing-guides/test-types) ✅

## [130 — Timeouts, retries, backoff, circuit breaker y bulkhead](../../classes/part-10-observability-sre-reliability/130-timeouts-retries-backoff-circuit-breaker-y-bulkhead/README.md)

- **Nygard (2018), *Release It!*** — plazos, cortacircuitos, compartimentos y fallos en cascada<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅
- **AWS (2025), *Timeouts, retries and backoff with jitter*** — cálculo de plazos y amplificación<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter) ✅
- **Google SRE (2025), *Addressing cascading failures*** — descarte por sobrecarga, colas acotadas y presupuesto de reintentos<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/addressing-cascading-failures) ✅
- **gRPC (2025), *Deadlines and deadline propagation*** — presupuesto de plazo heredado entre servicios<br>  ↳ documentación · [grpc.io](https://grpc.io/docs/guides/deadlines) ✅
- **Dean et al. (2013), *The tail at scale*** — peticiones duplicadas y respuesta parcial como alternativas al reintento<br>  ↳ documentación · [research.google](https://research.google/pubs/pub40801) ✅

## [131 — Chaos engineering y game days](../../classes/part-10-observability-sre-reliability/131-chaos-engineering-y-game-days/README.md)

- **Basiri et al. (2016), *Chaos engineering*** — método, hipótesis y radio de afectación<br>  ↳ artículo · [ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/7503833) ⏳
- **Principles of Chaos (2025), *Principles of chaos engineering*** — estado normal, experimentos en producción y automatización<br>  ↳ documentación · [principlesofchaos.org](https://principlesofchaos.org) ✅
- **Rosenthal et al. (2020), *Chaos Engineering*** — madurez, adopción y ensayos con personas<br>  ↳ libro · [ISBN 9781492043867](https://openlibrary.org/isbn/9781492043867) ✅
- **Google SRE (2025), *Disaster role playing and DiRT*** — ensayos con personas y hallazgos organizativos<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/accelerating-sre-on-call) ✅
- **AWS (2025), *Fault Injection Service: experiment templates and stop conditions*** — radio y condiciones de parada<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) ✅

## [132 — Proyecto: operación SRE de CloudShop](../../classes/part-10-observability-sre-reliability/132-proyecto-operacion-sre-de-cloudshop/README.md)

- **Beyer et al. (2016), *Site Reliability Engineering*** — el conjunto de prácticas como sistema, no como herramientas<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/table-of-contents) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — implantación práctica y medición del progreso<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **Majors et al. (2022), *Observability Engineering*** — coste, cardinalidad y preguntas nuevas<br>  ↳ libro · [ISBN 9781492076445](https://openlibrary.org/isbn/9781492076445) ✅
- **Woods et al. (2006), *Resilience Engineering*** — por qué la compensación automática oculta el deterioro<br>  ↳ documentación · [taylorfrancis.com](https://taylorfrancis.com/books/edit/10.1201/9781315605685/resilience-engineering) ✅
- **Allspaw (2015), *Trade-offs under pressure*** — decisiones durante incidentes y aprendizaje posterior<br>  ↳ documentación · [adaptivecapacitylabs.com](https://adaptivecapacitylabs.com/blog) ✅
