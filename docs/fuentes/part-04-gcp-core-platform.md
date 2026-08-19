# Fuentes de la Parte 04 — Google Cloud: plataforma esencial

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-04-gcp-core-platform/README.md)

## [049 — Organización, folders, proyectos, billing y cuotas](../../classes/part-04-gcp-core-platform/049-organizacion-folders-proyectos-billing-y-cuotas/README.md)

- **Google Cloud (2025), *Resource hierarchy*** — organización, carpetas, proyectos y herencia<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) ✅
- **Google Cloud (2025), *Creating and managing projects*** — identificador, nombre, número y borrado con retención<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/resource-manager/docs/creating-managing-projects) ✅
- **Google Cloud (2025), *Working with quotas*** — cuotas de tasa y de asignación, por proyecto y por región<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/docs/quotas/overview) ✅
- **Google Cloud (2025), *Export Cloud Billing data to BigQuery*** — configuración, esquema y ausencia de retroactividad<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/billing/docs/how-to/export-data-bigquery) ✅
- **Google Cloud (2025), *Organization policy constraints*** — restricciones booleanas y de lista, herencia y excepciones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) ✅

## [050 — IAM, service accounts y Workload Identity Federation](../../classes/part-04-gcp-core-platform/050-iam-service-accounts-y-workload-identity-federation/README.md)

- **Google Cloud (2025), *Service accounts overview*** — identidad y recurso, suplantación y adjunción<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/service-account-overview) ✅
- **Google Cloud (2025), *Best practices for using service accounts*** — claves, alternativas y cuentas por defecto<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/best-practices-service-accounts) ✅
- **Google Cloud (2025), *Workload Identity Federation*** — grupos, proveedores, mapeo y condición de atributo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/workload-identity-federation) ✅
- **Google Cloud (2025), *IAM deny policies*** — reglas de denegación y orden de evaluación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/deny-overview) ✅
- **Google Cloud (2025), *Role recommendations*** — reducción de privilegios a partir del uso observado y sus límites<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/policy-intelligence/docs/role-recommendations-overview) ✅

## [051 — VPC global, subredes regionales, firewall y Cloud NAT](../../classes/part-04-gcp-core-platform/051-vpc-global-subredes-regionales-firewall-y-cloud-nat/README.md)

- **Google Cloud (2025), *VPC network overview*** — alcance global, subredes regionales y rutas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/vpc) ✅
- **Google Cloud (2025), *VPC firewall rules*** — prioridad, reglas implícitas y destinos por etiqueta o cuenta de servicio<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/firewall/docs/firewalls) ✅
- **Google Cloud (2025), *Shared VPC overview*** — proyecto anfitrión, proyectos de servicio y permiso por subred<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/shared-vpc) ✅
- **Google Cloud (2025), *Private Google Access*** — acceso a las API desde máquinas sin dirección externa<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/private-google-access) ✅
- **Google Cloud (2025), *Cloud NAT overview*** — asignación de puertos, asignación dinámica y registro<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/nat/docs/overview) ✅

## [052 — Compute Engine, managed instance groups y load balancing](../../classes/part-04-gcp-core-platform/052-compute-engine-managed-instance-groups-y-load-balancing/README.md)

- **Google Cloud (2025), *Machine families resource and comparison guide*** — familias, tipos personalizados y proporciones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/compute/docs/machine-resource) ✅
- **Google Cloud (2025), *Sustained use discounts*** — descuento automático y su interacción con los compromisos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/compute/docs/sustained-use-discounts) ✅
- **Google Cloud (2025), *Block storage performance*** — IOPS por GB y límites por número de vCPU<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/compute/docs/disks/performance) ✅
- **Google Cloud (2025), *Autohealing instances in MIGs*** — comprobación de reparación, retardo inicial y diferencias con la del balanceador<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) ✅
- **Google Cloud (2025), *External Application Load Balancer overview*** — anycast, modos de equilibrio y escalador de capacidad<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/load-balancing/docs/https) ✅

## [053 — Cloud Storage, clases, lifecycle y replicación](../../classes/part-04-gcp-core-platform/053-cloud-storage-clases-lifecycle-y-replicacion/README.md)

- **Google Cloud (2025), *Bucket locations*** — región, birregión con destino elegido, multirregión y replicación turbo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/storage/docs/locations) ✅
- **Google Cloud (2025), *Storage classes*** — permanencia mínima, recuperación y precios por operación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/storage/docs/storage-classes) ✅
- **Google Cloud (2025), *Object Lifecycle Management*** — condiciones, versiones no actuales y transiciones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/storage/docs/lifecycle) ✅
- **Google Cloud (2025), *Uniform bucket-level access*** — IAM frente a listas de control por objeto<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/storage/docs/uniform-bucket-level-access) ✅
- **Google Cloud (2025), *Soft delete*** — retención de objetos y de buckets, y restauración<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/storage/docs/soft-delete) ✅

## [054 — Cloud SQL, Spanner, Firestore y Memorystore](../../classes/part-04-gcp-core-platform/054-cloud-sql-spanner-firestore-y-memorystore/README.md)

- **Google Cloud (2025), *Configure private IP for Cloud SQL*** — acceso a servicios privados y rango reservado<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/sql/docs/postgres/configure-private-ip) ✅
- **Google Cloud (2025), *About the Cloud SQL Auth Proxy*** — autenticación con IAM y conexión cifrada<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/sql/docs/postgres/sql-proxy) ✅
- **Google Cloud (2025), *Schema design best practices in Spanner*** — claves primarias, puntos calientes y tablas intercaladas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/spanner/docs/schema-design) ✅
- **Google Cloud (2025), *Understand Firestore billing*** — lecturas, escrituras y costo de las consultas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/firestore/docs/billing-example) ✅
- **Google Cloud (2025), *Distributed counters in Firestore*** — límite de escritura por documento y contadores repartidos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/firestore/docs/solutions/counters) ✅

## [055 — Cloud Run, Cloud Functions y API Gateway](../../classes/part-04-gcp-core-platform/055-cloud-run-cloud-functions-y-api-gateway/README.md)

- **Google Cloud (2025), *About instance concurrency in Cloud Run*** — concurrencia, efecto en costo y requisitos del código<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/about-concurrency) ✅
- **Google Cloud (2025), *CPU allocation in Cloud Run*** — CPU durante la petición frente a siempre asignada<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/configuring/cpu-allocation) ✅
- **Google Cloud (2025), *Rollbacks, gradual rollouts and traffic migration*** — revisiones, etiquetas y reparto de tráfico<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) ✅
- **Google Cloud (2025), *Authenticating service-to-service*** — testigos de identidad y `roles/run.invoker`<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/authenticating/service-to-service) ✅
- **Google Cloud (2025), *Cloud Run jobs overview*** — tareas, paralelismo, reintentos y tiempos límite<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/create-jobs) ✅

## [056 — Pub/Sub, Cloud Tasks y Workflows](../../classes/part-04-gcp-core-platform/056-pub-sub-cloud-tasks-y-workflows/README.md)

- **Google Cloud (2025), *Pub/Sub subscription types*** — extracción, entrega HTTP, BigQuery y Cloud Storage<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/subscriber) ✅
- **Google Cloud (2025), *Handling message failures*** — cola de fallidos, permisos del agente de servicio y reintentos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/handling-failures) ✅
- **Google Cloud (2025), *Exactly-once delivery*** — alcance de la garantía y sus límites<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/exactly-once-delivery) ✅
- **Google Cloud (2025), *Replay and purge messages*** — búsqueda por marca de tiempo e instantáneas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/replay-overview) ✅
- **Google Cloud (2025), *Cloud Tasks overview*** — control de ritmo, programación y deduplicación por nombre<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/tasks/docs/dual-overview) ✅

## [057 — Cloud Logging, Monitoring, Trace y Audit Logs](../../classes/part-04-gcp-core-platform/057-cloud-logging-monitoring-trace-y-audit-logs/README.md)

- **Google Cloud (2025), *Cloud Audit Logs overview*** — tipos, cuáles están activos y cuáles se pagan<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/logging/docs/audit) ✅
- **Google Cloud (2025), *Routing and storage overview*** — enrutador, destinos, exclusiones y buckets `_Required` y `_Default`<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/logging/docs/routing/overview) ✅
- **Google Cloud (2025), *Log-based metrics*** — contadores y distribuciones extraídos de registros<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/logging/docs/logs-based-metrics) ✅
- **Google Cloud (2025), *SLO monitoring and burn rate alerts*** — SLI, SLO, presupuesto de error y ventanas múltiples<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring) ✅
- **Google Cloud (2025), *Cloud Profiler concepts*** — muestreo continuo en producción y su sobrecarga<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/profiler/docs/concepts-profiling) ✅

## [058 — Cloud KMS, Secret Manager y Security Command Center](../../classes/part-04-gcp-core-platform/058-cloud-kms-secret-manager-y-security-command-center/README.md)

- **Google Cloud (2025), *Cloud KMS resource hierarchy*** — anillos, claves y versiones, y qué no se puede eliminar<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kms/docs/resource-hierarchy) ✅
- **Google Cloud (2025), *Key rotation*** — versión primaria, datos ya cifrados y recifrado<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kms/docs/key-rotation) ✅
- **Google Cloud (2025), *Use Secret Manager with Cloud Run*** — referencias como variable de entorno y como volumen montado<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/configuring/services/secrets) ✅
- **Google Cloud (2025), *Secret rotation*** — notificaciones programadas y qué hay que construir<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/secret-manager/docs/secret-rotation) ✅
- **Google Cloud (2025), *Attack path simulations in Security Command Center*** — exposición de recursos valiosos y priorización<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/security-command-center/docs/attack-exposure-learn) ✅

## [059 — Terraform y despliegues reproducibles en GCP](../../classes/part-04-gcp-core-platform/059-terraform-y-despliegues-reproducibles-en-gcp/README.md)

- **HashiCorp (2025), *State: purpose and sensitive data*** — qué guarda el estado y por qué se protege<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state/sensitive-data) ✅
- **HashiCorp (2025), *`count` and `for_each`*** — identificación por posición frente a clave estable<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each) ✅
- **HashiCorp (2025), *Command: plan and saved plan files*** — planificar, guardar y aplicar exactamente lo revisado<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/cli/commands/plan) ✅
- **Google Cloud (2025), *Terraform GCS backend and state management*** — bucket de estado, bloqueo y versionado<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/docs/terraform/resource-management/store-state) ✅
- **Google Cloud (2025), *Authenticate Terraform with Workload Identity Federation*** — suplantación sin claves en la canalización<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/blog/products/identity-security/enabling-keyless-authentication-from-github-actions) ✅

## [060 — Proyecto: aplicación de tres capas en Google Cloud](../../classes/part-04-gcp-core-platform/060-proyecto-aplicacion-de-tres-capas-en-google-cloud/README.md)

- **Google Cloud (2025), *Architecture Framework*** — los pilares como rejilla de revisión de la entrega<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework) ✅
- **Google Cloud (2025), *Patterns for scalable and resilient apps*** — desbordamiento entre regiones y ubicación de los datos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/scalable-and-resilient-apps) ✅
- **Google Cloud (2025), *Disaster recovery planning guide*** — RTO, RPO y ensayo de procedimientos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/dr-scenarios-planning-guide) ✅
- **Google (2018), *The Site Reliability Workbook*** — SLI, SLO y alertas por consumo de presupuesto de error<br>  ↳ documentación · [sre.google](https://sre.google/workbook/implementing-slos) ✅
- **Google Cloud (2025), *Landing zone design in Google Cloud*** — jerarquía, red e identidad como línea base declarada<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/landing-zones) ✅
