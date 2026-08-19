# Fuentes de la Parte 17 — AWS: arquitectura, automatización y operación en producción

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-17-aws-production-architecture/README.md)

## [205 — Hosting progresivo con Amplify, S3 y CloudFront](../../classes/part-17-aws-production-architecture/205-hosting-progresivo-con-amplify-s3-y-cloudfront/README.md)

- **AWS (2025), *Amplify Hosting user guide*** — flujo de publicación gestionado del sitio<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) ✅
- **AWS (2025), *Restricting access to an Amazon S3 origin (origin access control)*** — cerrar el origen para que solo se sirva por el CDN<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) ✅
- **AWS (2025), *CloudFront cache policies and cache key*** — políticas de caché y composición de su clave<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html) ✅
- **AWS (2025), *CloudFront Functions*** — lógica ligera ejecutada en el borde<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html) ✅
- **AWS (2025), *Blocking public access to your Amazon S3 storage*** — bloqueo de acceso público del almacenamiento<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) ✅

## [206 — OIDC de GitHub y GitLab hacia AWS sin secretos](../../classes/part-17-aws-production-architecture/206-oidc-de-github-y-gitlab-hacia-aws-sin-secretos/README.md)

- **GitHub (2025), *About security hardening with OpenID Connect*** — por qué un token efímero sustituye a la clave estática<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) ✅
- **GitHub (2025), *Configuring OpenID Connect in Amazon Web Services*** — configuración concreta del proveedor de identidad en AWS<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) ✅
- **GitLab (2025), *Connect to cloud services with OIDC*** — el procedimiento equivalente desde GitLab<br>  ↳ documentación · [docs.gitlab.com](https://docs.gitlab.com/ee/ci/cloud_services) ✅
- **AWS (2025), *Create an OpenID Connect identity provider in IAM*** — alta del proveedor de identidad en IAM<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) ✅
- **AWS (2025), *AssumeRoleWithWebIdentity and session policies*** — acotar la sesión asumida mediante políticas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) ✅

## [207 — SAM, Lambda, API Gateway y despliegue serverless](../../classes/part-17-aws-production-architecture/207-sam-lambda-api-gateway-y-despliegue-serverless/README.md)

- **AWS (2025), *Serverless Application Model developer guide*** — definición declarativa de la aplicación serverless<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) ✅
- **AWS (2025), *Lambda function scaling and reserved concurrency*** — control del escalado y reserva de concurrencia<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html) ✅
- **AWS (2025), *Choosing between HTTP APIs and REST APIs*** — criterio para elegir entre ambos tipos de API<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html) ✅
- **AWS (2025), *Operating Lambda: performance optimization and cold starts*** — origen del arranque en frío y cómo se mitiga<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1) ✅
- **AWS (2025), *Amazon RDS Proxy*** — agrupación de conexiones para funciones<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) ✅

## [208 — DynamoDB por patrones de acceso y single-table design](../../classes/part-17-aws-production-architecture/208-dynamodb-por-patrones-de-acceso-y-single-table-design/README.md)

- **AWS (2025), *DynamoDB developer guide: best practices for designing partition keys*** — reparto de claves de partición para evitar puntos calientes<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html) ✅
- **AWS (2025), *Single-table design considerations*** — cuándo compensa una sola tabla y cuándo no<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html) ✅
- **DeBrie (2020), *The DynamoDB Book*** — modelado guiado por los patrones de acceso<br>  ↳ documentación · [dynamodbbook.com](https://dynamodbbook.com) ✅
- **AWS (2025), *Secondary indexes and their capacity implications*** — coste en capacidad de los índices secundarios<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) ✅
- **AWS (2025), *DynamoDB Streams and change data capture*** — captura de cambios para propagar estado a otros servicios<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) ✅

## [209 — Cognito, JWT authorizers, WAF y defensa en profundidad](../../classes/part-17-aws-production-architecture/209-cognito-jwt-authorizers-waf-y-defensa-en-profundidad/README.md)

- **AWS (2025), *Amazon Cognito user pools: using tokens*** — qué contiene cada token y cuánto dura<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html) ✅
- **AWS (2025), *Verifying a JSON Web Token*** — validación de la firma y de las reclamaciones<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html) ✅
- **AWS (2025), *AWS WAF: testing rules in count mode*** — probar reglas en modo recuento sin bloquear tráfico legítimo<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html) ✅
- **OWASP (2025), *API Security Top 10: broken object level authorization*** — el fallo de autorización que el diseño debe cerrar<br>  ↳ documentación · [owasp.org](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization) ✅
- ***RFC 8725*** — JSON Web Token best current practices<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc8725) ✅

## [210 — EventBridge, SQS, DLQ, replay e idempotencia](../../classes/part-17-aws-production-architecture/210-eventbridge-sqs-dlq-replay-e-idempotencia/README.md)

- **AWS (2025), *Amazon SQS: visibility timeout and dead-letter queues*** — tiempo de visibilidad y destino de los mensajes fallidos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) ✅
- **AWS (2025), *Lambda event source mapping: partial batch responses*** — reintento parcial de un lote sin reprocesarlo entero<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html) ✅
- **AWS (2025), *Amazon EventBridge: rules, archives and replay*** — archivo y reproducción de eventos ya emitidos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) ✅
- **AWS (2025), *Powertools for AWS Lambda: idempotency*** — idempotencia mediante clave y almacén de estado<br>  ↳ documentación · [docs.powertools.aws.dev](https://docs.powertools.aws.dev/lambda/python/latest/utilities/idempotency) ✅
- **Hohpe et al. (2003), *Enterprise Integration Patterns*** — canal de mensajes inválidos y reintentos<br>  ↳ libro · [ISBN 9780321200686](https://openlibrary.org/isbn/9780321200686) ✅

## [211 — CloudWatch, X-Ray y observabilidad como código](../../classes/part-17-aws-production-architecture/211-cloudwatch-x-ray-y-observabilidad-como-codigo/README.md)

- **AWS (2025), *CloudWatch embedded metric format*** — emitir métricas desde el propio registro de la función<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html) ✅
- **AWS (2025), *CloudWatch Logs Insights query syntax*** — sintaxis de consulta de registros para el diagnóstico<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html) ✅
- **AWS (2025), *AWS X-Ray sampling rules*** — muestreo de trazas y su efecto en el coste<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html) ✅
- **OpenTelemetry (2025), *Context propagation*** — propagación de contexto entre servicios<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/concepts/context-propagation) ✅
- **Google (2018), *The Site Reliability Workbook: alerting on SLOs*** — alertar por consumo del presupuesto de error<br>  ↳ documentación · [sre.google](https://sre.google/workbook/alerting-on-slos) ✅

## [212 — ECR, ECS Fargate, ALB y autoscaling](../../classes/part-17-aws-production-architecture/212-ecr-ecs-fargate-alb-y-autoscaling/README.md)

- **AWS (2025), *Amazon ECR: image tag mutability and lifecycle policies*** — inmutabilidad de etiquetas y caducidad de imágenes<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html) ✅
- **AWS (2025), *Amazon ECS deployment types and circuit breaker*** — despliegue con corte automático ante fallo<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) ✅
- **AWS (2025), *Application Load Balancer: deregistration delay*** — retirada ordenada de destinos del balanceador<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html) ✅
- **AWS (2025), *Service auto scaling for Amazon ECS*** — políticas de escalado automático del servicio<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) ✅
- **AWS (2025), *AWS Fargate pricing and task sizing*** — dimensionar la tarea junto con su coste<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/fargate/pricing) ✅

## [213 — EKS, IRSA, GitOps y operación de clúster](../../classes/part-17-aws-production-architecture/213-eks-irsa-gitops-y-operacion-de-cluster/README.md)

- **AWS (2025), *IAM roles for service accounts (IRSA)*** — identidad por cuenta de servicio sin claves estáticas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) ✅
- **AWS (2025), *Amazon EKS Kubernetes version support and upgrade*** — ventana de soporte y procedimiento de actualización<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) ✅
- **Kubernetes (2025), *Managing resources for containers: requests and limits*** — peticiones y límites como contrato de recursos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers) ✅
- **Argo CD (2025), *GitOps and application health*** — estado de salud de la aplicación en el flujo GitOps<br>  ↳ documentación · [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io/en/stable) ✅
- **AWS (2025), *EKS Best Practices Guide*** — prácticas recomendadas de operación del clúster gestionado<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html) ✅

## [214 — Budgets, Cost Explorer, etiquetado y FinOps automatizado](../../classes/part-17-aws-production-architecture/214-budgets-cost-explorer-etiquetado-y-finops-automatizado/README.md)

- **AWS (2025), *Cost allocation tags and tag policies*** — etiquetas de asignación de coste y políticas que las obligan<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) ✅
- **AWS (2025), *AWS Budgets and budget actions*** — presupuestos con acción automática al superarse<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) ✅
- **AWS (2025), *AWS Cost Anomaly Detection*** — detección de desviaciones de gasto sin umbral fijo<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) ✅
- **FinOps Foundation (2025), *FinOps Framework: capabilities and maturity*** — las capacidades del marco y su nivel de madurez<br>  ↳ documentación · [finops.org](https://finops.org/framework) ✅
- **AWS (2025), *Savings Plans and Reserved Instances: coverage and utilization*** — cobertura y utilización de los compromisos de compra<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) ✅

## [215 — Multi-región, Route 53, failover y game day](../../classes/part-17-aws-production-architecture/215-multi-region-route-53-failover-y-game-day/README.md)

- **AWS (2025), *Disaster recovery options in the cloud*** — las cuatro estrategias de recuperación y su coste<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) ✅
- **AWS (2025), *Route 53 health checks and DNS failover*** — conmutación por fallo gobernada desde el DNS<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) ✅
- **AWS (2025), *Amazon DynamoDB global tables*** — réplica multirregión activa-activa de la base de datos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) ✅
- **Google (2018), *The Site Reliability Workbook: disaster role playing and testing*** — ensayo de desastre con roles asignados<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **Basiri et al. (2016), *Chaos engineering*** — experimentos con hipótesis y radio de alcance<br>  ↳ artículo · [ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/7503833) ⏳

## [216 — Proyecto: CloudShop productivo en AWS](../../classes/part-17-aws-production-architecture/216-proyecto-cloudshop-productivo-en-aws/README.md)

- **AWS (2025), *Well-Architected Framework*** — los pilares como lista de verificación del proyecto<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) ✅
- **AWS (2025), *Serverless Application Lens*** — la lente específica para arquitecturas serverless<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) ✅
- **AWS (2025), *Security Reference Architecture*** — arquitectura de referencia de los servicios de seguridad<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — prácticas de operación aplicadas al servicio productivo<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **Basiri et al. (2016), *Chaos engineering*** — inyección controlada de fallos para validar la resiliencia<br>  ↳ artículo · [ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/7503833) ⏳
