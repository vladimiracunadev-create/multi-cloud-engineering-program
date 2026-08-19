# Fuentes de la Parte 19 — Google Cloud: arquitectura de datos y operación en producción

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-19-gcp-production-architecture/README.md)

## [229 — Resource Manager, folders, Shared VPC y guardrails](../../classes/part-19-gcp-production-architecture/229-resource-manager-folders-shared-vpc-y-guardrails/README.md)

- **Google Cloud (2025), *Resource hierarchy*** — jerarquía de organización, carpetas y proyectos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) ✅
- **Google Cloud (2025), *Organization policy constraints*** — restricciones de política de organización como barreras<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) ✅
- **Google Cloud (2025), *Shared VPC overview*** — red compartida entre proyectos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/shared-vpc) ✅
- **Google Cloud (2025), *VPC firewall rules and service account targets*** — reglas de cortafuegos dirigidas por cuenta de servicio<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/firewall/docs/firewalls) ✅
- **Google Cloud (2025), *Landing zone design in Google Cloud*** — diseño de la zona de aterrizaje en Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/landing-zones) ✅

## [230 — Workload Identity Federation, IAM Conditions y PAM](../../classes/part-19-gcp-production-architecture/230-workload-identity-federation-iam-conditions-y-pam/README.md)

- **Google Cloud (2025), *Best practices for using service accounts*** — uso correcto de cuentas de servicio y sus riesgos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/best-practices-service-accounts) ✅
- **Google Cloud (2025), *Workload identity federation*** — federación para cargas externas sin claves<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/workload-identity-federation) ✅
- **Google Cloud (2025), *IAM conditions overview*** — condiciones que acotan cuándo aplica un permiso<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/conditions-overview) ✅
- **Google Cloud (2025), *Privileged Access Manager*** — elevación temporal de privilegio<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/pam-overview) ✅
- **Google Cloud (2025), *Policy Analyzer and IAM recommender*** — análisis de políticas y recomendación de mínimo privilegio<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/policy-intelligence/docs/policy-analyzer-overview) ✅

## [231 — Red global, load balancing, PSC y Cloud DNS](../../classes/part-19-gcp-production-architecture/231-red-global-load-balancing-psc-y-cloud-dns/README.md)

- **Google Cloud (2025), *VPC network overview*** — el modelo de red y sus fronteras<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/vpc) ✅
- **Google Cloud (2025), *Cloud Load Balancing: global external Application Load Balancer*** — balanceo global de capa de aplicación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/load-balancing/docs/https) ✅
- **Google Cloud (2025), *Private Service Connect*** — consumo privado de servicios entre redes<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/private-service-connect) ✅
- **Google Cloud (2025), *Cloud DNS private zones and forwarding*** — zonas privadas y reenvío de resolución<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/dns/docs/zones) ✅
- **Google Cloud (2025), *Connectivity Tests*** — pruebas de conectividad para diagnóstico<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) ✅

## [232 — Terraform, Infrastructure Manager y policy validation](../../classes/part-19-gcp-production-architecture/232-terraform-infrastructure-manager-y-policy-validation/README.md)

- **HashiCorp (2025), *Terraform state: remote backends and locking*** — estado remoto y bloqueo frente a ejecuciones simultáneas<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state) ✅
- **Google Cloud (2025), *Infrastructure Manager*** — el servicio gestionado que ejecuta Terraform<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/infrastructure-manager/docs/overview) ✅
- **Google Cloud (2025), *Policy validation with Policy Library*** — validación de políticas antes de aplicar el cambio<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/docs/terraform/policy-validation) ✅
- **Google Cloud (2025), *Cloud Foundation Toolkit modules*** — módulos de referencia ya conformes<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/foundation-toolkit) ✅
- **HashiCorp (2025), *Importing existing infrastructure*** — incorporar infraestructura existente al estado<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/cli/import) ✅

## [233 — Cloud Run, Functions, API Gateway y Workflows](../../classes/part-19-gcp-production-architecture/233-cloud-run-functions-api-gateway-y-workflows/README.md)

- **Google Cloud (2025), *Cloud Run: concurrency and instance settings*** — concurrencia por instancia y su efecto en el coste<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/about-concurrency) ✅
- **Google Cloud (2025), *Cloud Run: traffic management and revisions*** — reparto de tráfico entre revisiones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/managing/revisions) ✅
- **Google Cloud (2025), *Cloud Run: CPU allocation and background activity*** — asignación de CPU y trabajo en segundo plano<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/configuring/cpu-allocation) ✅
- **Google Cloud (2025), *Connecting to a VPC network from Cloud Run*** — acceso a la red privada desde el servicio<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/configuring/connecting-vpc) ✅
- **Google Cloud (2025), *Workflows*** — orquestación de pasos sin servidor<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/workflows/docs/overview) ✅

## [234 — GKE Autopilot, Workload Identity y Config Sync](../../classes/part-19-gcp-production-architecture/234-gke-autopilot-workload-identity-y-config-sync/README.md)

- **Google Cloud (2025), *GKE Autopilot overview*** — modo gestionado y qué deja de controlarse<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) ✅
- **Google Cloud (2025), *Workload Identity Federation for GKE*** — identidad de carga para acceder a servicios<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) ✅
- **Google Cloud (2025), *IP address planning for GKE clusters*** — planificación de direcciones del clúster<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) ✅
- **Google Cloud (2025), *Config Sync and Policy Controller*** — sincronización declarativa y control de políticas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/overview) ✅
- **Google Cloud (2025), *GKE release channels and maintenance windows*** — canales de versión y ventanas de mantenimiento<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels) ✅

## [235 — Cloud SQL, Spanner, Firestore y Bigtable](../../classes/part-19-gcp-production-architecture/235-cloud-sql-spanner-firestore-y-bigtable/README.md)

- **Google Cloud (2025), *Spanner schema design and hotspot avoidance*** — diseño de esquema que evita puntos calientes<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/spanner/docs/schema-design) ✅
- **Google Cloud (2025), *Spanner: interleaved tables and transactions*** — tablas intercaladas y semántica transaccional<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/spanner/docs/schema-and-data-model) ✅
- **Google Cloud (2025), *Firestore: best practices and limits*** — límites del servicio y prácticas recomendadas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/firestore/docs/best-practices) ✅
- **Google Cloud (2025), *Bigtable schema design*** — diseño de clave de fila y su efecto en el acceso<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/bigtable/docs/schema-design) ✅
- **Google Cloud (2025), *Cloud SQL: read replicas and high availability*** — réplicas de lectura y alta disponibilidad<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/sql/docs/mysql/high-availability) ✅

## [236 — BigQuery, Dataflow, Dataproc y gobernanza de datos](../../classes/part-19-gcp-production-architecture/236-bigquery-dataflow-dataproc-y-gobernanza-de-datos/README.md)

- **Google Cloud (2025), *BigQuery: controlling costs*** — control del coste de consulta<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/bigquery/docs/best-practices-costs) ✅
- **Google Cloud (2025), *Partitioned and clustered tables*** — particionado y agrupamiento para acotar el escaneo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/bigquery/docs/partitioned-tables) ✅
- **Google Cloud (2025), *Column-level and row-level security*** — seguridad a nivel de columna y de fila<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/bigquery/docs/column-level-security-intro) ✅
- **Google Cloud (2025), *Dataflow: unified batch and streaming*** — un mismo modelo para lote y flujo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/dataflow/docs/concepts) ✅
- **Google Cloud (2025), *Dataplex and data lineage*** — gobierno y linaje del dato<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/dataplex/docs/about-data-lineage) ✅

## [237 — Pub/Sub, Eventarc y entrega exactamente-una-vez](../../classes/part-19-gcp-production-architecture/237-pub-sub-eventarc-y-entrega-exactamente-una-vez/README.md)

- **Google Cloud (2025), *Pub/Sub: exactly-once delivery*** — garantía de entrega exactamente una vez y sus condiciones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/exactly-once-delivery) ✅
- **Google Cloud (2025), *Pub/Sub subscription types and delivery*** — tipos de suscripción y modo de entrega<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/subscriber) ✅
- **Google Cloud (2025), *Message ordering*** — ordenación de mensajes y su coste<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/ordering) ✅
- **Google Cloud (2025), *Dead-letter topics and retry policies*** — temas de mensajes fallidos y política de reintento<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/handling-failures) ✅
- **Google Cloud (2025), *Eventarc*** — enrutado de eventos entre servicios gestionados<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/eventarc/docs/overview) ✅

## [238 — Cloud Operations, Trace y OpenTelemetry](../../classes/part-19-gcp-production-architecture/238-cloud-operations-trace-y-opentelemetry/README.md)

- **Google Cloud (2025), *Cloud Logging: routing and storage*** — enrutado y almacenamiento de registros<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/logging/docs/routing/overview) ✅
- **Google Cloud (2025), *Cloud Audit Logs*** — registros de auditoría como evidencia<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/logging/docs/audit) ✅
- **Google Cloud (2025), *Service monitoring: SLOs and burn rate alerts*** — objetivos de servicio y alertas por tasa de consumo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring) ✅
- **Google Cloud (2025), *Cloud Trace and OpenTelemetry*** — trazas distribuidas con instrumentación estándar<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/trace/docs/setup) ✅
- **Google Cloud (2025), *Cloud Profiler*** — perfilado continuo en producción<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/profiler/docs/about-profiler) ✅

## [239 — SCC, VPC Service Controls, KMS y FinOps](../../classes/part-19-gcp-production-architecture/239-scc-vpc-service-controls-kms-y-finops/README.md)

- **Google Cloud (2025), *Security Command Center: attack path simulation*** — simulación de rutas de ataque<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/security-command-center/docs/attack-exposure-learn) ✅
- **Google Cloud (2025), *VPC Service Controls: dry run mode*** — modo de prueba antes de aplicar el perímetro<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc-service-controls/docs/dry-run-mode) ✅
- **Google Cloud (2025), *Customer-managed encryption keys*** — claves de cifrado gestionadas por el cliente<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kms/docs/cmek) ✅
- **Google Cloud (2025), *Sustained use and committed use discounts*** — descuentos por uso sostenido y por compromiso<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/compute/docs/sustained-use-discounts) ✅
- **Google Cloud (2025), *Billing labels and cost breakdown*** — etiquetas de facturación y desglose del gasto<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/billing/docs/how-to/bq-examples) ✅

## [240 — Proyecto: CloudShop productivo en Google Cloud](../../classes/part-19-gcp-production-architecture/240-proyecto-cloudshop-productivo-en-google-cloud/README.md)

- **Google Cloud (2025), *Architecture Framework*** — el marco de arquitectura aplicado al proyecto<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework) ✅
- **Google Cloud (2025), *Enterprise foundations blueprint*** — el plano de fundación empresarial como referencia<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/security-foundations) ✅
- **Google Cloud (2025), *Landing zone design*** — diseño de la zona de aterrizaje del proyecto<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/landing-zones) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — operación con objetivos de nivel de servicio<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **Forsgren et al. (2018), *Accelerate*** — medir antes y después con las mismas definiciones<br>  ↳ documentación · [itrevolution.com](https://itrevolution.com/product/accelerate) ✅
