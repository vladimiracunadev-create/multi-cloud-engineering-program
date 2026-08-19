# Fuentes de la Parte 03 — Azure: plataforma esencial

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-03-azure-core-platform/README.md)

## [037 — Tenant, management groups, suscripciones y resource groups](../../classes/part-03-azure-core-platform/037-tenant-management-groups-suscripciones-y-resource-groups/README.md)

- **Microsoft (2024), *Organize your Azure resources with management groups*** — jerarquía, herencia y profundidad máxima<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview) ✅
- **Microsoft (2024), *Azure Policy: understand policy effects*** — audit, deny, modify y deployIfNotExists<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects) ✅
- **Microsoft (2024), *Azure subscription and service limits, quotas, and constraints*** — cuotas ampliables y límites duros<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) ✅
- **Microsoft (2024), *Cloud Adoption Framework: enterprise-scale landing zones*** — estructura de grupos de administración de referencia<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone) ✅
- **Microsoft (2024), *Azure Resource Manager: resource groups*** — ámbito, ciclo de vida y qué no aísla<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) ✅

## [038 — Microsoft Entra ID, RBAC, managed identities y PIM](../../classes/part-03-azure-core-platform/038-microsoft-entra-id-rbac-managed-identities-y-pim/README.md)

- **Microsoft (2024), *Azure RBAC vs Microsoft Entra roles*** — los dos planos y qué gobierna cada uno<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-overview) ✅
- **Microsoft (2024), *Understand Azure role definitions*** — actions, notActions, dataActions y su evaluación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions) ✅
- **Microsoft (2024), *Managed identities for Azure resources*** — asignadas por el sistema y por el usuario<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) ✅
- **Microsoft (2024), *Workload identity federation*** — credenciales federadas y coincidencia exacta del sujeto<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) ✅
- **Microsoft (2024), *Privileged Identity Management*** — activación con caducidad, justificación y aprobación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) ✅

## [039 — Virtual Network, subredes, NSG, UDR, peering y Private Link](../../classes/part-03-azure-core-platform/039-virtual-network-subredes-nsg-udr-peering-y-private-link/README.md)

- **Microsoft (2025), *Default outbound access in Azure*** — la salida implícita y su retirada para redes virtuales nuevas<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access) ✅
- **Microsoft (2025), *Network security groups*** — reglas por defecto, evaluación en subred y NIC, y etiquetas de servicio<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) ✅
- **Microsoft (2025), *Virtual network traffic routing*** — rutas del sistema y precedencia entre UDR, BGP y sistema<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) ✅
- **Microsoft (2025), *Private endpoint DNS configuration*** — zonas `privatelink`, enlaces a redes virtuales y resolución desde on-premises<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) ✅
- **Microsoft (2025), *Hub-spoke network topology*** — transitividad, tráfico reenviado y tránsito de puerta de enlace<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke) ✅

## [040 — Virtual Machines, Scale Sets y Load Balancer](../../classes/part-03-azure-core-platform/040-virtual-machines-scale-sets-y-load-balancer/README.md)

- **Microsoft (2025), *Sizes for virtual machines in Azure*** — nomenclatura, letras aditivas y límites por tamaño<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview) ✅
- **Microsoft (2025), *Azure managed disk types*** — escalones de rendimiento, SSD premium v2 y Ultra Disk<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types) ✅
- **Microsoft (2025), *Virtual Machine Scale Sets orchestration modes*** — flexible frente a uniforme<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes) ✅
- **Microsoft (2025), *Load-balancing options*** — Load Balancer, Application Gateway, Front Door y Traffic Manager<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview) ✅
- **Microsoft (2025), *Azure Spot Virtual Machines*** — aviso de desalojo, políticas y precio máximo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms) ✅

## [041 — Blob Storage, Files, redundancia y lifecycle](../../classes/part-03-azure-core-platform/041-blob-storage-files-redundancia-y-lifecycle/README.md)

- **Microsoft (2025), *Azure Storage redundancy*** — LRS a GZRS, región emparejada y lectura en la secundaria<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) ✅
- **Microsoft (2025), *Disaster recovery and storage account failover*** — conmutación iniciada por el cliente, `lastSyncTime` y estado posterior<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/storage/common/storage-disaster-recovery-guidance) ✅
- **Microsoft (2025), *Access tiers for blob data*** — niveles, permanencia mínima y rehidratación desde archivo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview) ✅
- **Microsoft (2025), *Data protection overview*** — versionado, eliminación temporal, restauración a un punto anterior e inmutabilidad<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview) ✅
- **Microsoft (2025), *Grant limited access with shared access signatures*** — tipos de SAS y delegación de usuario<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) ✅

## [042 — Azure SQL, Cosmos DB y Azure Cache for Redis](../../classes/part-03-azure-core-platform/042-azure-sql-cosmos-db-y-azure-cache-for-redis/README.md)

- **Microsoft (2025), *vCore purchasing model for Azure SQL Database*** — recursos separados y niveles de servicio<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-sql-database-vcore) ✅
- **Microsoft (2025), *Resource limits and `sys.dm_db_resource_stats`*** — CPU, E/S de datos, velocidad de registro, trabajadores y sesiones<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-sql/database/resource-limits-logical-server) ✅
- **Microsoft (2025), *Partitioning and horizontal scaling in Azure Cosmos DB*** — partición lógica, tope de 20 GB y claves sintéticas<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview) ✅
- **Microsoft (2025), *Consistency levels in Azure Cosmos DB*** — los cinco niveles, testigo de sesión y costo en RU<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) ✅
- **Microsoft (2025), *Azure Cache for Redis best practices*** — niveles, políticas de expulsión, memoria reservada y conexiones<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-best-practices-development) ✅

## [043 — App Service, Functions y Container Apps](../../classes/part-03-azure-core-platform/043-app-service-functions-y-container-apps/README.md)

- **Microsoft (2025), *App Service plan overview*** — la unidad de escalado y facturación, y el efecto de compartirla<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans) ✅
- **Microsoft (2025), *Set up staging environments in App Service*** — intercambio, ajustes fijados al espacio y calentamiento<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) ✅
- **Microsoft (2025), *Azure Functions hosting options*** — duración máxima, red virtual y arranque en frío por plan<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) ✅
- **Microsoft (2025), *Set scaling rules in Azure Container Apps*** — reglas KEDA, réplicas mínimas y escaladores de cola<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/container-apps/scale-app) ✅
- **Microsoft (2025), *Troubleshoot SNAT port exhaustion*** — cupo por instancia, métricas y mitigaciones<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-intermittent-outbound-connection-errors) ✅

## [044 — Service Bus, Event Grid y Event Hubs](../../classes/part-03-azure-core-platform/044-service-bus-event-grid-y-event-hubs/README.md)

- **Microsoft (2025), *Compare Azure messaging services*** — cuándo Service Bus, cuándo Event Grid y cuándo Event Hubs<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services) ✅
- **Microsoft (2025), *Service Bus dead-letter queues*** — traslado automático, motivos y reproceso<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues) ✅
- **Microsoft (2025), *Message sessions and duplicate detection*** — orden por sesión y ventana de duplicados<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) ✅
- **Microsoft (2025), *Event Hubs features*** — particiones, grupos de consumidores, puntos de control y captura<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-features) ✅
- **Microsoft (2025), *Event Grid delivery and retry*** — saludo de validación, reintentos y mensajes fallidos<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/event-grid/delivery-and-retry) ✅

## [045 — Azure Monitor, Log Analytics y Application Insights](../../classes/part-03-azure-core-platform/045-azure-monitor-log-analytics-y-application-insights/README.md)

- **Microsoft (2025), *Azure Monitor overview*** — métricas, registros, orígenes y destinos<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/overview) ✅
- **Microsoft (2025), *Diagnostic settings in Azure Monitor*** — activación por recurso, destinos y despliegue por directiva<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings) ✅
- **Microsoft (2025), *Log Analytics workspace table plans and cost optimization*** — planes por tabla, retención y archivo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs) ✅
- **Microsoft (2025), *Sampling in Application Insights*** — muestreo adaptativo, `itemCount` y sus efectos en las consultas<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling) ✅
- **Microsoft (2025), *Types of Azure Monitor alerts*** — métrica, registro y registro de actividad, con sus latencias<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types) ✅

## [046 — Key Vault, Defender for Cloud y Azure Policy](../../classes/part-03-azure-core-platform/046-key-vault-defender-for-cloud-y-azure-policy/README.md)

- **Microsoft (2025), *Azure Key Vault security overview*** — modelos de permisos, protección contra purga y límites de servicio<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/key-vault/general/security-features) ✅
- **Microsoft (2025), *Customer-managed keys*** — control, revocación y consecuencias de perder el acceso a la clave<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview) ✅
- **Microsoft (2025), *Understand Azure Policy effects*** — `Audit`, `Deny`, `Modify`, `DeployIfNotExists` y su alcance<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects) ✅
- **Microsoft (2025), *Azure Policy exemption structure*** — exenciones con motivo, responsable y caducidad<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/exemption-structure) ✅
- **Microsoft (2025), *Microsoft Defender for Cloud plans*** — postura frente a protección de cargas y precios por tipo de recurso<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) ✅

## [047 — Bicep, plantillas y despliegues por alcance](../../classes/part-03-azure-core-platform/047-bicep-plantillas-y-despliegues-por-alcance/README.md)

- **Microsoft (2025), *What is Bicep?*** — relación con ARM, módulos y compilación transparente<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) ✅
- **Microsoft (2025), *Deployment scopes in Bicep*** — `targetScope`, módulos con `scope` y qué se crea en cada nivel<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-subscription) ✅
- **Microsoft (2025), *Azure Resource Manager deployment modes*** — incremental frente a completo y qué elimina cada uno<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-modes) ✅
- **Microsoft (2025), *Deployment what-if operation*** — símbolos, limitaciones y ruido de proveedores<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) ✅
- **Microsoft (2025), *Use Azure Key Vault to pass secure parameter values*** — `@secure()`, `getSecret()` e historial de despliegues<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/key-vault-parameter) ✅

## [048 — Proyecto: aplicación de tres capas en Azure](../../classes/part-03-azure-core-platform/048-proyecto-aplicacion-de-tres-capas-en-azure/README.md)

- **Microsoft (2025), *Azure Well-Architected Framework*** — los cinco pilares como rejilla de revisión de la entrega<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/well-architected) ✅
- **Microsoft (2025), *Troubleshoot transient connection errors in Azure SQL*** — códigos transitorios y lógica de reintento obligatoria<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-sql/database/troubleshoot-common-connectivity-issues) ✅
- **Microsoft (2025), *Reliability in Azure: availability zones*** — comportamiento de la conmutación y qué mide un simulacro de zona<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) ✅
- **Microsoft (2025), *Cloud Adoption Framework: landing zone design areas*** — línea base declarada y vigilada, y sus áreas de decisión<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-areas) ✅
- **Microsoft (2025), *Chaos Studio experiment design*** — provocar fallos con alcance acotado y medir el resultado<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-overview) ✅
