# Fuentes de la Parte 21 — Operación cloud, automatización y respuesta a incidentes

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-21-cloud-operations-automation/README.md)

## [253 — Inventario, etiquetado, CMDB y ownership](../../classes/part-21-cloud-operations-automation/253-inventario-etiquetado-cmdb-y-ownership/README.md)

- **AWS (2025), *AWS Config and Resource Explorer*** — inventario y consulta de recursos en AWS<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) ✅
- **Microsoft (2025), *Azure Resource Graph*** — consulta de inventario a escala en Azure<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview) ✅
- **Google Cloud (2025), *Cloud Asset Inventory*** — inventario y búsqueda de activos en Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/asset-inventory/docs/overview) ✅
- **Limoncelli et al. (2016), *The Practice of Cloud System Administration*** — prácticas de administración de sistemas a escala<br>  ↳ documentación · [the-cloud-book.com](https://the-cloud-book.com) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — propiedad y responsabilidad del servicio<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅

## [254 — Patching, imágenes doradas y gestión de configuración](../../classes/part-21-cloud-operations-automation/254-patching-imagenes-doradas-y-gestion-de-configuracion/README.md)

- **CISA (2025), *Known Exploited Vulnerabilities catalog*** — vulnerabilidades con explotación activa confirmada<br>  ↳ documentación · [cisa.gov](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) ⏳
- **CycloneDX (2025), *Software bill of materials specification*** — inventario de componentes del artefacto<br>  ↳ documentación · [cyclonedx.org](https://cyclonedx.org/specification/overview) ✅
- **SLSA (2025), *Supply chain levels for software artifacts*** — niveles de integridad de la cadena de suministro<br>  ↳ documentación · [slsa.dev](https://slsa.dev) ✅
- **AWS (2025), *EC2 Image Builder and golden AMI pipelines*** — canalización de imágenes base reproducibles<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — gestión del cambio en producción<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅

## [255 — Backups, restore testing, vaults e inmutabilidad](../../classes/part-21-cloud-operations-automation/255-backups-restore-testing-vaults-e-inmutabilidad/README.md)

- **AWS (2025), *AWS Backup: vault lock and cross-account backups*** — bloqueo del almacén y copias entre cuentas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) ✅
- **Microsoft (2025), *Azure Backup: immutable vaults and multi-user authorization*** — almacenes inmutables y autorización de varios operadores<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/backup/backup-azure-immutable-vault-concept) ✅
- **Google Cloud (2025), *Backup and DR Service*** — el servicio equivalente en Google Cloud<br>  ↳ documentación · [docs.cloud.google.com](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) ✅
- **Beyer et al. (2016), *Site Reliability Engineering*** — por qué una copia sin restauración probada no es copia<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/data-integrity) ✅
- **NIST SP 800-34 (2010), *Contingency planning guide for federal information systems*** — el procedimiento normativo de planificación de contingencia<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) ✅

## [256 — Administración remota sin SSH permanente](../../classes/part-21-cloud-operations-automation/256-administracion-remota-sin-ssh-permanente/README.md)

- **AWS (2025), *Systems Manager Session Manager*** — sesión administrada sin abrir el puerto de SSH<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) ✅
- **Microsoft (2025), *Azure Bastion and just-in-time VM access*** — acceso puntual a la máquina con aprobación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview) ✅
- **Google Cloud (2025), *Identity-Aware Proxy for TCP forwarding*** — reenvío TCP autenticado por identidad<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iap/docs/using-tcp-forwarding) ✅
- **NIST SP 800-207 (2020), *Zero Trust Architecture*** — el principio que justifica retirar el acceso permanente<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/207/final) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — operación del acceso administrativo<br>  ↳ documentación · [sre.google](https://sre.google/workbook/eliminating-toil) ✅

## [257 — Alertas, on-call, escalamiento y comunicación](../../classes/part-21-cloud-operations-automation/257-alertas-on-call-escalamiento-y-comunicacion/README.md)

- **Beyer et al. (2016), *Site Reliability Engineering*** — guardia, escalamiento y salud del equipo<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/being-on-call) ✅
- **Google (2018), *The Site Reliability Workbook: alerting on SLOs*** — alertar por consumo del presupuesto de error<br>  ↳ documentación · [sre.google](https://sre.google/workbook/alerting-on-slos) ✅
- **PagerDuty (2025), *Incident response documentation: roles and escalation*** — roles del incidente y ruta de escalamiento<br>  ↳ documentación · [response.pagerduty.com](https://response.pagerduty.com) ✅
- **Atlassian (2025), *Incident communication best practices*** — comunicación con las personas afectadas durante el corte<br>  ↳ documentación · [atlassian.com](https://atlassian.com/incident-management/incident-communication) ✅
- **Allspaw (2016), *Incident command for IT*** — el mando de incidentes trasladado a operaciones de TI<br>  ↳ libro · [oreilly.com](https://www.oreilly.com/library/view/incident-management-for/9781492045922/) ⏳

## [258 — Triage de red, cómputo, datos y dependencias](../../classes/part-21-cloud-operations-automation/258-triage-de-red-computo-datos-y-dependencias/README.md)

- **Beyer et al. (2016), *Site Reliability Engineering*** — método de diagnóstico bajo presión<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/effective-troubleshooting) ✅
- **Allspaw (2015), *Trade-offs under pressure: heuristics and observations of teams resolving internet service outages*** — cómo decide un equipo real con información incompleta<br>  ↳ documentación · [researchgate.net](https://www.researchgate.net/publication/282869185) ⏳
- **Huang et al. (2017), *Gray failure: the Achilles' heel of cloud-scale systems*** — fallos parciales que el diagnóstico binario no ve<br>  ↳ documentación · [microsoft.com](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf) ✅
- **Nygard (2018), *Release It!*** — patrones de fallo y su firma<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅
- **Google (2018), *The Site Reliability Workbook: incident response*** — conducción de la respuesta al incidente<br>  ↳ documentación · [sre.google](https://sre.google/workbook/incident-response) ✅

## [259 — Runbooks ejecutables y auto-remediation](../../classes/part-21-cloud-operations-automation/259-runbooks-ejecutables-y-auto-remediation/README.md)

- **Beyer et al. (2018), *The Site Reliability Workbook*** — el runbook como procedimiento verificable<br>  ↳ documentación · [sre.google](https://sre.google/workbook/eliminating-toil) ✅
- **AWS (2024), *Systems Manager Automation runbooks*** — automatización de procedimientos en AWS<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) ✅
- **Microsoft (2024), *Azure Automation runbooks*** — automatización de procedimientos en Azure<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/automation/automation-runbook-types) ✅
- **Google Cloud (2024), *Automated remediation with Cloud Functions and alerting*** — remediación disparada desde la alerta<br>  ↳ documentación · [docs.cloud.google.com](https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-incidents-and-problems) ✅
- **Limoncelli (2020), *Operational excellence in April Fools' pranks*** — sobre automatización probada frente a escrita<br>  ↳ documentación · [queue.acm.org](https://queue.acm.org/detail.cfm?id=3380780) ✅

## [260 — Change management, ventanas y rollback](../../classes/part-21-cloud-operations-automation/260-change-management-ventanas-y-rollback/README.md)

- **Forsgren et al. (2018), *Accelerate*** — frecuencia y estabilidad correlacionan positivamente<br>  ↳ libro · [ISBN 9781942788379](https://openlibrary.org/isbn/9781942788379) ✅
- **Google (2024), *DORA: capabilities*** — change approval processes<br>  ↳ documentación · [dora.dev](https://dora.dev/capabilities/streamlining-change-approval) ✅
- **Humble et al. (2010), *Continuous Delivery*** — canalización de despliegue con retroceso posible<br>  ↳ libro · [ISBN 9780321670250](https://openlibrary.org/isbn/9780321670250) ✅
- **AWS (2024), *Operational Excellence Pillar: managing change*** — gestión del cambio como práctica de excelencia operativa<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) ✅
- **Microsoft (2024), *Azure Well-Architected Framework: safe deployment practices*** — prácticas de despliegue seguro por fases<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/well-architected/operational-excellence/safe-deployments) ✅

## [261 — Game days, chaos engineering y aprendizaje](../../classes/part-21-cloud-operations-automation/261-game-days-chaos-engineering-y-aprendizaje/README.md)

- **Basiri et al. (2016), *Chaos engineering*** — el experimento de fallo como método<br>  ↳ artículo · [ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/7436642) ⏳
- **Rosenthal et al. (2020), *Chaos Engineering: system resiliency in practice*** — el procedimiento completo del experimento<br>  ↳ libro · [ISBN 9781492043867](https://openlibrary.org/isbn/9781492043867) ✅
- **Google (2018), *Site Reliability Engineering*** — el ensayo como aprendizaje del equipo<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/reliable-product-launches/) ✅
- **AWS (2024), *Fault Injection Service*** — experiment design<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) ✅
- **Microsoft (2024), *Azure Chaos Studio*** — inyección de fallos gestionada en Azure<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-overview) ✅

## [262 — Capacity planning, cuotas y gestión de demanda](../../classes/part-21-cloud-operations-automation/262-capacity-planning-cuotas-y-gestion-de-demanda/README.md)

- **Gunther (2007), *Guerrilla Capacity Planning*** — leyes de escalabilidad y efecto de la utilización<br>  ↳ libro · [ISBN 9783540261384](https://openlibrary.org/isbn/9783540261384) ✅
- **Google (2018), *Site Reliability Engineering*** — planificación de capacidad con datos de servicio<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/handling-overload) ✅
- **AWS (2024), *Service Quotas*** — monitoring and requesting increases<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) ✅
- **Microsoft (2024), *Azure subscription and service limits, quotas, and constraints*** — límites y cuotas que acotan el crecimiento<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits) ✅
- **Google Cloud (2024), *Quotas and limits*** — cuotas del proveedor y su ampliación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/docs/quotas) ✅

## [263 — AIOps, automatización asistida y límites humanos](../../classes/part-21-cloud-operations-automation/263-aiops-automatizacion-asistida-y-limites-humanos/README.md)

- **Google (2018), *The Site Reliability Workbook*** — por qué se alerta sobre síntomas<br>  ↳ documentación · [sre.google](https://sre.google/workbook/alerting-on-slos) ✅
- **Parasuraman et al. (1997), *Humans and automation: use, misuse, disuse, abuse*** — cuándo la automatización degrada el desempeño humano<br>  ↳ documentación · [journals.sagepub.com](https://journals.sagepub.com/doi/10.1518/001872097778543886) ⏳
- **AWS (2024), *CloudWatch anomaly detection*** — detección de anomalías sobre la métrica<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) ✅
- **Microsoft (2024), *Azure Monitor: dynamic thresholds and smart detection*** — umbrales dinámicos y detección asistida<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/azure-monitor/alerts/alerts-dynamic-thresholds) ✅
- **OWASP (2025), *Top 10 for LLM applications*** — entrada no fiable y permisos excesivos<br>  ↳ documentación · [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications) ✅

## [264 — Proyecto: centro de operaciones de CloudShop](../../classes/part-21-cloud-operations-automation/264-proyecto-centro-de-operaciones-de-cloudshop/README.md)

- **Beyer et al. (2018), *The Site Reliability Workbook*** — operación completa de extremo a extremo<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **Forsgren et al. (2018), *Accelerate*** — las cuatro métricas de entrega<br>  ↳ libro · [ISBN 9781942788379](https://openlibrary.org/isbn/9781942788379) ✅
- **AWS (2024), *Operational Excellence Pillar*** — el pilar de excelencia operativa como referencia<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) ✅
- **Microsoft (2024), *Azure Well-Architected Framework: Operational Excellence*** — el pilar equivalente en Azure<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/well-architected/operational-excellence) ✅
- **Google Cloud (2024), *Architecture Framework: Operational excellence*** — el pilar equivalente en Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework/operational-excellence) ✅
