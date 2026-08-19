# Fuentes de la Parte 13 — Multi-cloud, híbrido, migración y recuperación

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-13-multicloud-hybrid-disaster-recovery/README.md)

## [157 — Motivaciones y anti-patrones de multi-cloud](../../classes/part-13-multicloud-hybrid-disaster-recovery/157-motivaciones-y-anti-patrones-de-multi-cloud/README.md)

- **Gartner (2025), *Multicloud strategies: motivations and pitfalls*** — motivos declarados frente a resultados<br>  ↳ documentación · [gartner.com](https://gartner.com/en/information-technology) ✅
- **Google Cloud (2025), *Multicloud and hybrid architecture patterns*** — niveles concretos y su coste<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/hybrid-multicloud-patterns) ✅
- **AWS (2025), *Multi-Region fundamentals*** — comparación entre regiones y proveedores para disponibilidad<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/aws-multi-region-fundamentals) ✅
- **Fowler (2025), *Exit cost over lock-in*** — sustituir dependencia por coste de salida medible<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki) ✅
- **CNCF (2025), *Multicloud interoperability*** — qué es común entre proveedores y qué no<br>  ↳ documentación · [cncf.io](https://cncf.io/reports) ✅

## [158 — Portabilidad, capas de abstracción y lock-in](../../classes/part-13-multicloud-hybrid-disaster-recovery/158-portabilidad-capas-de-abstraccion-y-lock-in/README.md)

- **OCI (2025), *Image and runtime specifications*** — portabilidad real de la capa de contenedores<br>  ↳ norma · [opencontainers.org](https://opencontainers.org) ✅
- **CNCF (2025), *Cloud native landscape and interoperability*** — qué interfaces son comunes entre proveedores<br>  ↳ documentación · [landscape.cncf.io](https://landscape.cncf.io) ✅
- **Cockcroft (2025), *Lock-in and exit cost*** — sustituir el debate por una estimación en semanas<br>  ↳ documentación · [adrianco.medium.com](https://adrianco.medium.com/) ✅
- **Hexagonal architecture (2025), *Ports and adapters*** — mantener lo específico en el borde<br>  ↳ documentación · [alistair.cockburn.us](https://alistair.cockburn.us/hexagonal-architecture) ✅
- **Google Cloud (2025), *Portability considerations for hybrid and multicloud*** — límites prácticos de la portabilidad<br>  ↳ documentación · [docs.cloud.google.com](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices) ✅

## [159 — Federación de identidad entre nubes](../../classes/part-13-multicloud-hybrid-disaster-recovery/159-federacion-de-identidad-entre-nubes/README.md)

- **OpenID Foundation (2025), *OpenID Connect Core*** — base de la federación de personas entre sistemas<br>  ↳ documentación · [openid.net](https://openid.net/specs/openid-connect-core-1_0.html) ✅
- **AWS (2025), *Identity providers and OIDC federation for workloads*** — intercambio de testigo por credenciales temporales<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html) ✅
- **Google Cloud (2025), *Workload identity federation*** — condiciones de sujeto y acotación de la confianza<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/iam/docs/workload-identity-federation) ✅
- **Microsoft (2025), *Workload identity federation in Entra ID*** — federación entre proveedores sin secretos<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/entra/workload-id/workload-identity-federation) ✅
- **SPIFFE (2025), *Identity across trust domains*** — identidad de carga entre dominios distintos<br>  ↳ documentación · [spiffe.io](https://spiffe.io/docs/latest/spiffe-about/overview) ✅

## [160 — Conectividad, tránsito, DNS y service discovery](../../classes/part-13-multicloud-hybrid-disaster-recovery/160-conectividad-transito-dns-y-service-discovery/README.md)

- **AWS (2025), *Hybrid connectivity: VPN, Direct Connect and Transit Gateway*** — mecanismos y cuándo hace falta un concentrador<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html) ✅
- **Google Cloud (2025), *Hybrid and multicloud networking patterns*** — patrones de conexión y sus compromisos<br>  ↳ documentación · [docs.cloud.google.com](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns) ✅
- **Azure (2025), *DNS resolution across on-premises and cloud*** — reenvío condicional y extremos de resolución<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/architecture/hybrid/hybrid-dns-infra) ✅
- ***Espacios de direcciones privadas*** — base del plan de direccionamiento<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc6890.html) ✅
- **Google SRE (2025), *Load balancing and DNS TTL trade-offs*** — velocidad de conmutación frente a carga de resolución<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/load-balancing-frontend) ✅

## [161 — Replicación de datos, soberanía y costos de egress](../../classes/part-13-multicloud-hybrid-disaster-recovery/161-replicacion-de-datos-soberania-y-costos-de-egress/README.md)

- **AWS (2025), *Data transfer pricing and cross-AZ charges*** — qué se factura y en qué dirección<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures) ✅
- **Google Cloud (2025), *Network pricing and egress*** — tarifas por destino y tramos de volumen<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/network-pricing) ✅
- **Azure (2025), *Bandwidth pricing and zone-redundant traffic*** — coste entre zonas y regiones<br>  ↳ documentación · [azure.microsoft.com](https://azure.microsoft.com/pricing/details/bandwidth) ✅
- **Debezium (2025), *Change data capture for cross-system replication*** — replicar cambios en vez de estado<br>  ↳ documentación · [debezium.io](https://debezium.io/documentation/reference/stable) ✅
- **FinOps Foundation (2025), *Data transfer cost allocation*** — atribuir el tráfico a servicios y equipos<br>  ↳ documentación · [finops.org](https://finops.org/framework/capabilities/allocation) ✅

## [162 — Observabilidad y operación entre proveedores](../../classes/part-13-multicloud-hybrid-disaster-recovery/162-observabilidad-y-operacion-entre-proveedores/README.md)

- **OpenTelemetry (2025), *Semantic conventions and resource attributes*** — vocabulario común y normalización<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/specs/semconv) ✅
- **OpenTelemetry (2025), *Collector deployment patterns*** — recoger local, agregar y exportar a un destino común<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/collector/deployment) ✅
- **Google SRE (2025), *Monitoring across environments and synthetic probes*** — comprobación externa y ausencia de datos<br>  ↳ documentación · [sre.google](https://sre.google/workbook/monitoring) ✅
- **PagerDuty (2025), *Incident response with distributed teams*** — un canal, un mando y encaminamiento por catálogo<br>  ↳ documentación · [response.pagerduty.com](https://response.pagerduty.com) ✅
- **CNCF (2025), *Observability across clusters and clouds*** — patrones de agregación y federación de métricas<br>  ↳ documentación · [cncf.io](https://cncf.io/reports) ✅

## [163 — Terraform multi-provider y separación de estados](../../classes/part-13-multicloud-hybrid-disaster-recovery/163-terraform-multi-provider-y-separacion-de-estados/README.md)

- **HashiCorp (2025), *Terraform: multiple provider configurations and aliases*** — varios proveedores en una misma configuración<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/providers/configuration) ✅
- **HashiCorp (2025), *State: remote backends, locking and separation*** — almacenamiento, bloqueo y reparto del estado<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state/remote) ✅
- **HashiCorp (2025), *Module composition and interfaces*** — módulos con interfaces estables en vez de módulos condicionales<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/modules/develop/composition) ✅
- **Brikman (2022), *Terraform: Up & Running*** — reparto de estados y dependencias entre ellos<br>  ↳ documentación · [terraformupandrunning.com](https://terraformupandrunning.com) ✅
- **Open Policy Agent (2025), *Policy checks on infrastructure plans*** — análisis del plan antes de aplicar<br>  ↳ documentación · [openpolicyagent.org](https://openpolicyagent.org/docs/latest/terraform) ✅

## [164 — Flotas Kubernetes y políticas comunes](../../classes/part-13-multicloud-hybrid-disaster-recovery/164-flotas-kubernetes-y-politicas-comunes/README.md)

- **Kubernetes (2025), *Version skew policy*** — diferencias admitidas entre plano de control y nodos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/releases/version-skew-policy) ✅
- **Kubernetes (2025), *Deprecated API migration guide*** — detectar uso de API retiradas antes de actualizar<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/reference/using-api/deprecation-guide) ✅
- **Argo CD (2025), *ApplicationSet: cluster generators*** — aplicar configuración a conjuntos seleccionados por etiquetas<br>  ↳ documentación · [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Cluster) ✅
- **Google Cloud (2025), *Fleet management and policy consistency*** — flota, línea base y políticas comunes<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kubernetes-engine/fleet-management/docs) ✅
- **CNCF (2025), *Multicluster management patterns*** — colocación explícita frente a reparto automático<br>  ↳ documentación · [cncf.io](https://cncf.io/reports) ✅

## [165 — Nube híbrida, edge y conectividad privada](../../classes/part-13-multicloud-hybrid-disaster-recovery/165-nube-hibrida-edge-y-conectividad-privada/README.md)

- **AWS (2025), *Outposts, Local Zones and edge services*** — espectro de opciones y su operabilidad<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design) ✅
- **Azure (2025), *Azure Arc and hybrid management*** — gobierno de recursos fuera de la nube pública<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/azure-arc/overview) ✅
- **Google Cloud (2025), *Distributed Cloud and edge patterns*** — proceso en el sitio y envío de resultados<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/distributed-cloud) ✅
- **Eclipse Foundation (2025), *Edge device update and rollback patterns*** — actualización con reversión automática<br>  ↳ documentación · [projects.eclipse.org](https://projects.eclipse.org) ✅
- **NIST (2025), *Guide to industrial control system security*** — acceso físico, arranque verificado y credenciales en el sitio<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/82/r3/final) ✅

## [166 — Backup, RTO, RPO y patrones de disaster recovery](../../classes/part-13-multicloud-hybrid-disaster-recovery/166-backup-rto-rpo-y-patrones-de-disaster-recovery/README.md)

- **AWS (2025), *Disaster recovery of workloads: backup, pilot light, warm standby, active/active*** — patrones y sus plazos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) ✅
- **Google Cloud (2025), *Disaster recovery planning guide*** — objetivos por escenario y verificación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/dr-scenarios-planning-guide) ✅
- **Azure (2025), *Business continuity and backup immutability*** — copias inmutables y separación de credenciales<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/backup/backup-azure-immutable-vault-concept) ✅
- **NIST (2010), *SP 800-34: contingency planning*** — definición de objetivos y pruebas del plan<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) ✅
- **Google SRE (2025), *Data integrity: backups versus replication*** — por qué la replicación no protege del borrado<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/data-integrity) ✅

## [167 — Las 7R de migración y oleadas](../../classes/part-13-multicloud-hybrid-disaster-recovery/167-las-7r-de-migracion-y-oleadas/README.md)

- **AWS (2025), *Migration strategies: the 7 Rs*** — definición y criterios de elección por carga<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html) ✅
- **Google Cloud (2025), *Migration to Google Cloud: assess and discover*** — descubrimiento y dependencias observadas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/migration-to-gcp-getting-started) ✅
- **Microsoft (2025), *Cloud Adoption Framework: migrate*** — oleadas, ventanas y validación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/cloud-adoption-framework/migrate) ✅
- **Fowler (2004), *Strangler fig application*** — sustitución progresiva con fachada<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/StranglerFigApplication.html) ✅
- **Humble et al. (2010), *Continuous Delivery*** — migraciones de datos y convivencia<br>  ↳ libro · [ISBN 9780321670250](https://openlibrary.org/isbn/9780321670250) ✅

## [168 — Proyecto: continuidad activa-pasiva entre nubes](../../classes/part-13-multicloud-hybrid-disaster-recovery/168-proyecto-continuidad-activa-pasiva-entre-nubes/README.md)

- **AWS (2025), *Disaster recovery across providers: considerations*** — límites y coste de la continuidad entre nubes<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) ✅
- **Google Cloud (2025), *Architecting disaster recovery for cloud infrastructure outages*** — objetivos, patrones y pruebas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/disaster-recovery) ✅
- **Azure (2025), *Reliability testing and failover drills*** — ensayos periódicos y su registro<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/reliability) ✅
- **Google SRE (2025), *Disaster role playing and readiness testing*** — ejecutar el plan como parte de la operación<br>  ↳ documentación · [sre.google](https://sre.google/workbook) ✅
- **Uptime Institute (2025), *Outage analysis and recovery practice*** — frecuencia real de fallos por región y por proveedor<br>  ↳ documentación · [uptimeinstitute.com](https://uptimeinstitute.com/resources) ✅
