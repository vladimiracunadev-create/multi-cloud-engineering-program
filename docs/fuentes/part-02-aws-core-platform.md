# Fuentes de la Parte 02 — AWS: plataforma esencial

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-02-aws-core-platform/README.md)

## [025 — Organizations, cuentas, OU, SCP y landing zone](../../classes/part-02-aws-core-platform/025-organizations-cuentas-ou-scp-y-landing-zone/README.md)

- **AWS (2024), *Organizations: service control policies*** — evaluación, estrategias y límites<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) ✅
- **AWS (2024), *Organizing your AWS environment using multiple accounts*** — cuentas de la base y unidades recomendadas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) ✅
- **AWS (2024), *Control Tower: how controls work*** — guardarraíles preventivos y detectivos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) ✅
- **AWS (2024), *CloudTrail: security best practices*** — rastro de organización, validación de integridad y bloqueo de objetos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html) ✅
- **AWS (2024), *AWS services that work with IAM*** — qué servicios son globales y cómo se comportan con condiciones de región<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) ✅

## [026 — IAM, roles, políticas, STS y federación](../../classes/part-02-aws-core-platform/026-iam-roles-politicas-sts-y-federacion/README.md)

- **AWS (2024), *Policy evaluation logic*** — orden de evaluación completo con SCP y límites de permisos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) ✅
- **AWS (2024), *Global condition context keys*** — catálogo de claves de condición y su comportamiento<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) ✅
- **AWS (2024), *Permissions boundaries for IAM entities*** — delegación segura de creación de roles<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) ✅
- **AWS (2024), *IAM Access Analyzer policy validation*** — comprobaciones de seguridad antes de aplicar una política<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) ✅
- **Hardt (2012), *RFC 6749: The OAuth 2.0 Authorization Framework*** — base del intercambio de token por credenciales<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc6749) ✅

## [027 — VPC, subredes, rutas, NAT, endpoints y seguridad](../../classes/part-02-aws-core-platform/027-vpc-subredes-rutas-nat-endpoints-y-seguridad/README.md)

- **AWS (2024), *VPC user guide: subnets and routing*** — direcciones reservadas y tablas de rutas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) ✅
- **AWS (2024), *Compare security groups and network ACLs*** — con estado frente a sin estado<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html) ✅
- **AWS (2024), *AWS PrivateLink and VPC endpoints*** — tipos de endpoint, precios y restricciones<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) ✅
- **AWS (2024), *VPC Flow Logs*** — formato de registro y campos para diagnóstico<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) ✅
- **AWS (2024), *Reachability Analyzer*** — análisis estático de la ruta entre dos recursos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) ✅

## [028 — EC2, AMI, EBS y selección de capacidad](../../classes/part-02-aws-core-platform/028-ec2-ami-ebs-y-seleccion-de-capacidad/README.md)

- **AWS (2024), *Amazon EC2 instance types*** — nomenclatura, familias y capacidades adicionales<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) ✅
- **AWS (2024), *Burstable performance instances*** — línea base, créditos y modo ilimitado<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) ✅
- **AWS (2024), *Amazon EBS volume types*** — IOPS, throughput y tamaño de operación de E/S<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) ✅
- **AWS (2024), *Savings Plans*** — compromiso por gasto horario frente a instancias reservadas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) ✅
- **AWS (2024), *Spot Instances: interruption notices*** — preaviso de dos minutos y patrones de uso seguro<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html) ✅

## [029 — Elastic Load Balancing y Auto Scaling](../../classes/part-02-aws-core-platform/029-elastic-load-balancing-y-auto-scaling/README.md)

- **AWS (2024), *Application Load Balancer: target groups and health checks*** — parámetros y semántica<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) ✅
- **AWS (2024), *Deregistration delay*** — drenado de conexiones y su interacción con el ciclo de vida<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html) ✅
- **AWS (2024), *Target tracking scaling policies*** — métricas predefinidas y enfriamientos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) ✅
- **AWS (2024), *Troubleshoot your Application Load Balancer*** — causas de 502, 503 y 504 y campos del log de acceso<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-troubleshooting.html) ✅
- **Beyer (2016), *Site Reliability Engineering*** — reparto de carga y comprobaciones de salud<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/load-balancing-datacenter) ✅

## [030 — S3: objetos, versionado, lifecycle y replicación](../../classes/part-02-aws-core-platform/030-s3-objetos-versionado-lifecycle-y-replicacion/README.md)

- **AWS (2024), *Using versioning in S3 buckets*** — versiones, marcadores de borrado y facturación<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) ✅
- **AWS (2024), *S3 Object Lock*** — modos gobernanza y cumplimiento, y sus límites<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) ✅
- **AWS (2024), *Blocking public access to your Amazon S3 storage*** — semántica de los cuatro parámetros<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) ✅
- **AWS (2024), *Managing your storage lifecycle*** — transiciones, mínimos de duración y limpieza de multiparte<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) ✅
- **AWS (2024), *S3 storage classes*** — precios, latencias de recuperación y umbrales de tamaño<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) ✅

## [031 — RDS, DynamoDB y ElastiCache: decisión de datos](../../classes/part-02-aws-core-platform/031-rds-dynamodb-y-elasticache-decision-de-datos/README.md)

- **AWS (2024), *DynamoDB best practices: partition key design*** — cardinalidad, particiones calientes y dispersión<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html) ✅
- **AWS (2024), *DynamoDB transactions*** — límites de elementos, tamaño y consumo de capacidad<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html) ✅
- **Kleppmann (2017), *Designing Data-Intensive Applications*** — modelos de datos, índices y motores de almacenamiento<br>  ↳ libro · [ISBN 9781491903117](https://openlibrary.org/isbn/9781491903117) ✅
- **PostgreSQL (2024), *Using EXPLAIN*** — lectura de planes y coste de E/S<br>  ↳ documentación · [postgresql.org](https://postgresql.org/docs/current/using-explain.html) ✅
- **AWS (2024), *ElastiCache caching strategies*** — caducidad, escritura activa y mitigación de estampidas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html) ✅

## [032 — Lambda, API Gateway y Step Functions](../../classes/part-02-aws-core-platform/032-lambda-api-gateway-y-step-functions/README.md)

- **AWS (2024), *Lambda function scaling and concurrency*** — límites de cuenta, reserva y ritmo de crecimiento<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html) ✅
- **AWS (2024), *Provisioned concurrency*** — coste y efecto sobre el arranque en frío<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) ✅
- **AWS (2024), *Using Amazon RDS Proxy*** — multiplexación, fijación de sesión y sus causas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) ✅
- **AWS (2024), *API Gateway quotas and important notes*** — tiempo de espera de 29 s y tamaño de carga útil<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html) ✅
- **AWS (2024), *Step Functions: Standard vs Express workflows*** — garantías de ejecución y modelo de precio<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) ✅

## [033 — SQS, SNS y EventBridge](../../classes/part-02-aws-core-platform/033-sqs-sns-y-eventbridge/README.md)

- **AWS (2024), *Amazon SQS visibility timeout*** — semántica, extensión y límite de 12 horas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) ✅
- **AWS (2024), *Amazon SQS dead-letter queues*** — política de reenvío y reproceso<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) ✅
- **AWS (2024), *FIFO queues: message groups and throughput*** — orden por grupo y límites<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html) ✅
- **AWS (2024), *EventBridge event patterns*** — filtrado por contenido y enrutamiento declarativo<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) ✅
- **Hohpe et al. (2003), *Enterprise Integration Patterns*** — canal punto a punto, publicación-suscripción y canal de mensajes inválidos<br>  ↳ libro · [ISBN 9780321200686](https://openlibrary.org/isbn/9780321200686) ✅

## [034 — CloudWatch, CloudTrail, Config y Systems Manager](../../classes/part-02-aws-core-platform/034-cloudwatch-cloudtrail-config-y-systems-manager/README.md)

- **AWS (2024), *CloudWatch: publishing custom metrics and dimensions*** — cardinalidad y facturación por serie<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) ✅
- **AWS (2024), *CloudWatch Embedded Metric Format*** — métricas desde logs estructurados<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html) ✅
- **AWS (2024), *CloudTrail: logging data events*** — qué se registra por defecto y qué hay que activar<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) ✅
- **AWS (2024), *AWS Config rules and remediation*** — evaluación continua y corrección automática<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) ✅
- **AWS (2024), *Systems Manager Session Manager*** — acceso sin puertos abiertos ni claves, con auditoría<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) ✅

## [035 — KMS, Secrets Manager, WAF y controles de seguridad](../../classes/part-02-aws-core-platform/035-kms-secrets-manager-waf-y-controles-de-seguridad/README.md)

- **AWS (2024), *AWS KMS: key policies*** — segunda barrera independiente de los permisos sobre el recurso<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) ✅
- **AWS (2024), *Rotating AWS KMS keys*** — qué rota, qué se conserva y por qué no hay recifrado<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) ✅
- **AWS (2024), *Secrets Manager rotation*** — los cuatro pasos y la estrategia de usuario alterno<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) ✅
- **AWS (2024), *AWS WAF managed rule groups*** — modo cuenta, exclusiones y sentencias de reducción de alcance<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html) ✅
- **AWS (2024), *S3 Bucket Keys*** — reducción de llamadas a KMS y su efecto en el coste<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) ✅

## [036 — Proyecto: aplicación de tres capas en AWS](../../classes/part-02-aws-core-platform/036-proyecto-aplicacion-de-tres-capas-en-aws/README.md)

- **AWS (2024), *Well-Architected Framework: the review process*** — cómo estructurar la revisión de una carga<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html) ✅
- **AWS (2024), *Fault Injection Service*** — inyección controlada de fallos de zona, red y recursos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) ✅
- **Beyer (2018), *Site Reliability Engineering*** — pruebas de fiabilidad y game days<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/testing-reliability/) ✅
- **Nygard (2018), *Release It!*** — plazos, mamparos y degradación bajo dependencia lenta<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅
- **Nygard (2011), *Documenting Architecture Decisions*** — formato de los ADR que acompañan la entrega<br>  ↳ documentación · [cognitect.com](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) ✅
