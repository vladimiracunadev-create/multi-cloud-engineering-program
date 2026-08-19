# Fuentes de la Parte 18 — Azure: arquitectura empresarial y operación en producción

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-18-azure-production-architecture/README.md)

## [217 — Enterprise-scale landing zones y management groups](../../classes/part-18-azure-production-architecture/217-enterprise-scale-landing-zones-y-management-groups/README.md)

- **Microsoft (2025), *Cloud Adoption Framework: Azure landing zone design areas*** — las áreas de diseño de una zona de aterrizaje<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone) ✅
- **Microsoft (2025), *Management groups and organizing resources*** — jerarquía de grupos de administración para heredar control<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview) ✅
- **Microsoft (2025), *Azure Policy effects and remediation*** — efectos de política y remediación de lo ya desplegado<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects) ✅
- **Microsoft (2025), *Azure Policy exemptions*** — excepciones acotadas y con caducidad<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/exemption-structure) ✅
- **Microsoft (2025), *Subscription vending and landing zone automation*** — automatizar la entrega de suscripciones ya conformes<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/subscription-vending) ✅

## [218 — Entra ID, workload identity, PIM y Conditional Access](../../classes/part-18-azure-production-architecture/218-entra-id-workload-identity-pim-y-conditional-access/README.md)

- **Microsoft (2025), *Managed identities for Azure resources*** — identidad administrada para no guardar credenciales<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) ✅
- **Microsoft (2025), *Workload identity federation*** — federación de identidad para cargas fuera de Azure<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) ✅
- **Microsoft (2025), *Azure RBAC scope and best practices*** — ámbito de asignación de roles y su alcance real<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices) ✅
- **Microsoft (2025), *Privileged Identity Management*** — elevación temporal de privilegio con aprobación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) ✅
- **Microsoft (2025), *Conditional Access and emergency access accounts*** — acceso condicional y cuentas de emergencia<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) ✅

## [219 — Hub-spoke, Virtual WAN, Private Link y DNS privado](../../classes/part-18-azure-production-architecture/219-hub-spoke-virtual-wan-private-link-y-dns-privado/README.md)

- **Microsoft (2025), *Hub-spoke network topology in Azure*** — topología de concentrador y radios<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke) ✅
- **Microsoft (2025), *Azure Private Link and private endpoint DNS configuration*** — resolución DNS de los puntos de enlace privados<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) ✅
- **Microsoft (2025), *Network security groups: default rules and evaluation*** — reglas por defecto y orden de evaluación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) ✅
- **Microsoft (2025), *User-defined routes and forced tunneling*** — rutas definidas por el usuario y túnel forzado<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) ✅
- **Microsoft (2025), *Azure Virtual WAN architecture*** — la alternativa gestionada a la topología manual<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about) ✅

## [220 — Bicep, deployment stacks y Azure Verified Modules](../../classes/part-18-azure-production-architecture/220-bicep-deployment-stacks-y-azure-verified-modules/README.md)

- **Microsoft (2025), *Bicep documentation*** — sintaxis y modelo de despliegue declarativo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) ✅
- **Microsoft (2025), *Deployment stacks*** — pilas de despliegue para gestionar el ciclo de vida completo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks) ✅
- **Microsoft (2025), *ARM template deployment modes*** — diferencia entre despliegue incremental y completo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-modes) ✅
- **Microsoft (2025), *Azure Verified Modules*** — módulos verificados como base reutilizable<br>  ↳ documentación · [azure.github.io](https://azure.github.io/Azure-Verified-Modules) ✅
- **Microsoft (2025), *ARM template what-if operation*** — previsualizar el cambio antes de aplicarlo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-what-if) ✅

## [221 — App Service, Functions y Container Apps en producción](../../classes/part-18-azure-production-architecture/221-app-service-functions-y-container-apps-en-produccion/README.md)

- **Microsoft (2025), *Azure App Service deployment slots*** — ranuras de despliegue para intercambio sin corte<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) ✅
- **Microsoft (2025), *Azure Functions hosting options*** — planes de alojamiento y su efecto en arranque y coste<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) ✅
- **Microsoft (2025), *Azure Container Apps revisions and traffic splitting*** — revisiones y reparto de tráfico entre versiones<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/container-apps/revisions) ✅
- **Microsoft (2025), *Integrate your app with an Azure virtual network*** — integración de la aplicación con la red virtual<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration) ✅
- **Microsoft (2025), *Troubleshooting SNAT port exhaustion*** — agotamiento de puertos SNAT como causa de fallo intermitente<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/load-balancer/troubleshoot-outbound-connection) ✅

## [222 — AKS, workload identity, ingress y GitOps](../../classes/part-18-azure-production-architecture/222-aks-workload-identity-ingress-y-gitops/README.md)

- **Microsoft (2025), *Azure Kubernetes Service: workload identity*** — identidad de carga de trabajo sin secretos en el clúster<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) ✅
- **Microsoft (2025), *AKS networking: Azure CNI overlay*** — el modelo de red superpuesta y su consumo de direcciones<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/azure-cni-overlay) ✅
- **Microsoft (2025), *Application routing add-on and managed ingress*** — complemento gestionado de entrada al clúster<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/app-routing) ✅
- **Microsoft (2025), *AKS cluster upgrades and maintenance windows*** — actualización del clúster y ventanas de mantenimiento<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/upgrade-cluster) ✅
- **Microsoft (2025), *AKS baseline architecture*** — arquitectura de referencia del clúster productivo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks) ✅

## [223 — Azure SQL, Cosmos DB y consistencia distribuida](../../classes/part-18-azure-production-architecture/223-azure-sql-cosmos-db-y-consistencia-distribuida/README.md)

- **Microsoft (2025), *Azure Cosmos DB consistency levels*** — los cinco niveles y su efecto en latencia y disponibilidad<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) ✅
- **Microsoft (2025), *Request units in Azure Cosmos DB*** — unidades de petición como unidad de capacidad y coste<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units) ✅
- **Microsoft (2025), *Partitioning and horizontal scaling*** — elección de clave de partición y escalado horizontal<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview) ✅
- **Microsoft (2025), *Indexing policies in Azure Cosmos DB*** — políticas de indexación y su coste de escritura<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cosmos-db/index-policy) ✅
- **Microsoft (2025), *Azure SQL Database: failover groups and elastic pools*** — grupos de conmutación y agrupaciones elásticas<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db) ✅

## [224 — Service Bus, Event Grid y Event Hubs](../../classes/part-18-azure-production-architecture/224-service-bus-event-grid-y-event-hubs/README.md)

- **Microsoft (2025), *Azure Service Bus: message sessions, transactions and dead-letter queues*** — sesiones, transacciones y cola de mensajes fallidos<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) ✅
- **Microsoft (2025), *Azure Event Grid: event delivery and retry*** — entrega de eventos y política de reintento<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/event-grid/delivery-and-retry) ✅
- **Microsoft (2025), *Azure Event Hubs: partitions, consumer groups and capture*** — particiones, grupos de consumo y captura<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-features) ✅
- **Microsoft (2025), *Choose between Azure messaging services*** — criterio para elegir entre los tres servicios<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services) ✅
- **Hohpe et al. (2003), *Enterprise Integration Patterns*** — los patrones de integración que sostienen el diseño<br>  ↳ libro · [ISBN 9780321200686](https://openlibrary.org/isbn/9780321200686) ✅

## [225 — Azure Monitor, Application Insights y OpenTelemetry](../../classes/part-18-azure-production-architecture/225-azure-monitor-application-insights-y-opentelemetry/README.md)

- **Microsoft (2025), *Azure Monitor: diagnostic settings*** — configuración de diagnóstico como origen de la telemetría<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings) ✅
- **Microsoft (2025), *Application Insights with OpenTelemetry*** — instrumentación con OpenTelemetry<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable) ✅
- **Microsoft (2025), *Log Analytics table plans and data transformations*** — planes de tabla y transformación en la ingesta<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs) ✅
- **Microsoft (2025), *Sampling in Application Insights*** — muestreo y su efecto sobre la fidelidad y el coste<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling) ✅
- **OpenTelemetry (2025), *Specification and semantic conventions*** — convenciones semánticas comunes a toda la telemetría<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/specs/otel) ✅

## [226 — Defender for Cloud, Policy y Sentinel](../../classes/part-18-azure-production-architecture/226-defender-for-cloud-policy-y-sentinel/README.md)

- **Microsoft (2025), *Microsoft Defender for Cloud: secure score and attack paths*** — puntuación segura y rutas de ataque<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls) ✅
- **Microsoft (2025), *Regulatory compliance in Defender for Cloud*** — cumplimiento normativo evaluado de forma continua<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard) ✅
- **Microsoft (2025), *Microsoft Sentinel: data connectors and analytics rules*** — conectores de datos y reglas de análisis<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/sentinel/overview) ✅
- **MITRE (2025), *ATT&CK for cloud*** — el catálogo de técnicas de ataque en la nube<br>  ↳ documentación · [attack.mitre.org](https://attack.mitre.org/matrices/enterprise/cloud) ✅
- **Microsoft (2025), *Sentinel cost optimization and data tiers*** — niveles de datos y control del coste de ingesta<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/sentinel/billing) ✅

## [227 — Cost Management, Advisor, resiliencia y Chaos Studio](../../classes/part-18-azure-production-architecture/227-cost-management-advisor-resiliencia-y-chaos-studio/README.md)

- **Microsoft (2025), *Azure Cost Management and Billing*** — análisis del gasto y su asignación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cost-management-billing) ✅
- **Microsoft (2025), *Azure Advisor recommendations*** — recomendaciones automáticas de mejora<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview) ✅
- **Microsoft (2025), *Azure savings plans and reservations*** — planes de ahorro y reservas frente a pago por uso<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-compute-overview) ✅
- **Microsoft (2025), *Azure Chaos Studio*** — experimentos de fallo controlados<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-overview) ✅
- **Microsoft (2025), *Reliability and availability zones in Azure*** — zonas de disponibilidad y objetivos de fiabilidad<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) ✅

## [228 — Proyecto: CloudShop productivo en Azure](../../classes/part-18-azure-production-architecture/228-proyecto-cloudshop-productivo-en-azure/README.md)

- **Microsoft (2025), *Azure Well-Architected Framework*** — los pilares aplicados a la revisión del proyecto<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/well-architected) ✅
- **Microsoft (2025), *Cloud Adoption Framework: Azure landing zones*** — la zona de aterrizaje como base del despliegue<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone) ✅
- **Microsoft (2025), *Azure Policy remediation tasks*** — remediación de recursos existentes no conformes<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — operación del servicio con objetivos medibles<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **Basiri et al. (2016), *Chaos engineering*** — validación de la resiliencia mediante fallos inyectados<br>  ↳ artículo · [ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/7503833) ⏳
