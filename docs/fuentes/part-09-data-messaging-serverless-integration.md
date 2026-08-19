# Fuentes de la Parte 09 — Datos, mensajería, serverless e integración

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-09-data-messaging-serverless-integration/README.md)

## [109 — Bases relacionales administradas y pooling](../../classes/part-09-data-messaging-serverless-integration/109-bases-relacionales-administradas-y-pooling/README.md)

- **PostgreSQL (2025), *Connections and resource consumption*** — coste por conexión y parámetros de límite de tiempo<br>  ↳ documentación · [postgresql.org](https://postgresql.org/docs/current/runtime-config-connection.html) ✅
- **PgBouncer (2025), *Pooling modes*** — sesión, transacción y sentencia, y lo que cada modo rompe<br>  ↳ documentación · [pgbouncer.org](https://pgbouncer.org/features.html) ✅
- **AWS (2025), *RDS Proxy: connection pooling and failover*** — agrupación gestionada y comportamiento durante la conmutación<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) ✅
- **Azure (2025), *Azure Database for PostgreSQL: read replicas and lag*** — retardo de replicación y cuándo no usar réplica<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/postgresql/flexible-server/concepts-read-replicas) ✅
- **Google Cloud (2025), *Cloud SQL: high availability and failover*** — tiempos de conmutación y requisitos de la aplicación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/sql/docs/postgres/high-availability) ✅

## [110 — NoSQL: clave-valor, documento, columna y grafo](../../classes/part-09-data-messaging-serverless-integration/110-nosql-clave-valor-documento-columna-y-grafo/README.md)

- **AWS (2025), *DynamoDB: partition keys and best practices*** — cardinalidad, reparto y particiones calientes<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html) ✅
- **Google Cloud (2025), *Bigtable schema design*** — clave de fila, reparto y antipatrones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/bigtable/docs/schema-design) ✅
- **Azure (2025), *Cosmos DB: partitioning and horizontal scaling*** — clave de partición lógica y física<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/cosmos-db/partitioning-overview) ✅
- **Kleppmann (2017), *Designing Data-Intensive Applications*** — modelos de datos y particionado<br>  ↳ libro · [ISBN 9781491903117](https://openlibrary.org/isbn/9781491903117) ✅
- **Neo4j (2025), *When to use a graph database*** — profundidad variable como criterio de elección<br>  ↳ documentación · [neo4j.com](https://neo4j.com/docs/getting-started/data-modeling) ✅

## [111 — Caché, invalidación, TTL y consistencia](../../classes/part-09-data-messaging-serverless-integration/111-cache-invalidacion-ttl-y-consistencia/README.md)

- **Redis (2025), *Key eviction and expiration*** — políticas de expulsión, caducidad y su efecto en la carga<br>  ↳ documentación · [redis.io](https://redis.io/docs/latest/develop/reference/eviction) ✅
- **Nygard (2018), *Release It!*** — caché, avalancha y degradación controlada<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅
- **Facebook Engineering (2013), *Scaling Memcache at Facebook*** — cerrojo de recálculo y avalancha en producción<br>  ↳ documentación · [usenix.org](https://usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf) ✅
- **MDN (2025), *HTTP caching*** — capas de caché, validadores y control de desfase<br>  ↳ documentación · [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) ✅
- **AWS (2025), *ElastiCache: caching strategies and best practices*** — caché aparte, escritura a través y recalentamiento<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html) ✅

## [112 — Object storage, data lake y formatos columnares](../../classes/part-09-data-messaging-serverless-integration/112-object-storage-data-lake-y-formatos-columnares/README.md)

- **Apache Parquet (2025), *File format specification*** — grupos de filas, estadísticas y codificaciones por columna<br>  ↳ documentación · [parquet.apache.org](https://parquet.apache.org/docs/file-format) ✅
- **Apache Iceberg (2025), *Table specification*** — instantáneas, confirmación atómica y evolución de esquema<br>  ↳ documentación · [iceberg.apache.org](https://iceberg.apache.org/spec) ✅
- **AWS (2025), *S3 storage classes and lifecycle considerations*** — mínimos facturables, permanencia y coste de recuperación<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) ✅
- **Google Cloud (2025), *Cloud Storage: object versioning and retention policies*** — versionado, retención e inmutabilidad<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/storage/docs/object-versioning) ✅
- **Azure (2025), *Data Lake Storage best practices*** — tamaño de fichero, particionado y organización por zonas<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-best-practices) ✅

## [113 — Colas, entrega, reintentos y dead-letter queues](../../classes/part-09-data-messaging-serverless-integration/113-colas-entrega-reintentos-y-dead-letter-queues/README.md)

- **AWS (2025), *SQS: visibility timeout and dead-letter queues*** — invisibilidad, reentrega y destino de fallidos<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) ✅
- **Azure (2025), *Service Bus: message transfers, locks and settlement*** — bloqueo, renovación y confirmación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/service-bus-messaging/message-transfers-locks-settlement) ✅
- **Google Cloud (2025), *Pub/Sub: subscription retry policy and dead lettering*** — espera creciente y reenvío<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/handling-failures) ✅
- **Brooker (2015), *Exponential backoff and jitter*** — por qué la variación importa tanto como la espera<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter) ✅
- **Nygard (2018), *Release It!*** — tormentas de reintentos y cortocircuitos<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅

## [114 — Pub/sub, streams, particiones y orden](../../classes/part-09-data-messaging-serverless-integration/114-pub-sub-streams-particiones-y-orden/README.md)

- **Apache Kafka (2025), *Design: topics, partitions and consumer groups*** — orden por partición y reparto del grupo<br>  ↳ documentación · [kafka.apache.org](https://kafka.apache.org/documentation) ✅
- **Apache Kafka (2025), *Log compaction*** — retención por clave y borrado con mensaje vacío<br>  ↳ documentación · [kafka.apache.org](https://kafka.apache.org/documentation) ✅
- **Google Cloud (2025), *Pub/Sub: ordering keys and message retention*** — orden por clave y relectura<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/pubsub/docs/ordering) ✅
- **AWS (2025), *Kinesis Data Streams: shards and resharding*** — paralelismo por fragmento y coste de reparticionar<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding.html) ✅
- **Kleppmann (2017), *Designing Data-Intensive Applications*** — registros, posiciones y reproceso<br>  ↳ libro · [ISBN 9781491903117](https://openlibrary.org/isbn/9781491903117) ✅

## [115 — Arquitectura dirigida por eventos y contratos](../../classes/part-09-data-messaging-serverless-integration/115-arquitectura-dirigida-por-eventos-y-contratos/README.md)

- **CloudEvents (2025), *Specification*** — envoltura común: identificador, tipo, origen, sujeto y momento<br>  ↳ documentación · [github.com](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) ✅
- **Fowler (2025), *What do you mean by event-driven?*** — notificación, transferencia de estado y sus consecuencias<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/articles/201701-event-driven.html) ✅
- **Confluent (2025), *Schema Registry: compatibility types*** — compatibilidad hacia atrás, hacia delante y completa<br>  ↳ documentación · [docs.confluent.io](https://docs.confluent.io/platform/current/schema-registry/fundamentals/avro.html) ✅
- **Richardson (2025), *Saga and event choreography trade-offs*** — coreografía frente a orquestación<br>  ↳ documentación · [microservices.io](https://microservices.io/patterns/index.html) ✅
- **Debezium (2025), *Change data capture: when to use it*** — límites de publicar cambios de filas como contrato<br>  ↳ documentación · [debezium.io](https://debezium.io/documentation/reference/stable/architecture.html) ✅

## [116 — Sagas, outbox, idempotencia y deduplicación](../../classes/part-09-data-messaging-serverless-integration/116-sagas-outbox-idempotencia-y-deduplicacion/README.md)

- **Richardson (2025), *Transactional outbox pattern*** — publicar el hecho en la misma transacción que el cambio<br>  ↳ documentación · [microservices.io](https://microservices.io/patterns/index.html) ✅
- **Richardson (2025), *Saga pattern*** — transacciones locales con compensación, coreografiadas y orquestadas<br>  ↳ documentación · [microservices.io](https://microservices.io/patterns/index.html) ✅
- **Stripe (2025), *Idempotent requests*** — clave de idempotencia en un efecto externo y su ventana<br>  ↳ documentación · [docs.stripe.com](https://docs.stripe.com/api/idempotent_requests) ✅
- **Helland (2012), *Idempotence is not a medical condition*** — idempotencia como propiedad del efecto, no de la entrega<br>  ↳ documentación · [queue.acm.org](https://queue.acm.org/detail.cfm?id=2187821) ✅
- **Garcia-Molina et al. (1987), *Sagas*** — el artículo original sobre transacciones largas con compensación<br>  ↳ documentación · [cs.cornell.edu](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf) ⏳

## [117 — Serverless: límites, cold starts y concurrencia](../../classes/part-09-data-messaging-serverless-integration/117-serverless-limites-cold-starts-y-concurrencia/README.md)

- **AWS (2025), *Lambda: concurrency, reserved and provisioned*** — techo, suelo y comportamiento al escalar<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html) ✅
- **AWS (2025), *Lambda execution environment lifecycle*** — inicialización, congelación tras responder y reciclado<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) ✅
- **Google Cloud (2025), *Cloud Run functions: cold starts and minimum instances*** — coste del arranque y mitigaciones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/run/docs/tips/general) ✅
- **Azure (2025), *Azure Functions: performance and scale considerations*** — límites, planes y conexiones salientes<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/azure-functions/functions-best-practices) ✅
- **Jonas et al. (2019), *Cloud programming simplified: a Berkeley view on serverless computing*** — límites del modelo y cuándo no encaja<br>  ↳ artículo · [doi:10.48550/arXiv.1902.03383](https://doi.org/10.48550/arXiv.1902.03383) ✅

## [118 — API management, cuotas, versiones y monetización](../../classes/part-09-data-messaging-serverless-integration/118-api-management-cuotas-versiones-y-monetizacion/README.md)

- **IETF (2024), *RFC 9457: Problem Details for HTTP APIs*** — formato uniforme de errores<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc9457.html) ✅
- **IETF (2023), *RFC 8594: The Sunset HTTP header*** — anuncio de retirada de recursos y versiones<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc8594.html) ✅
- **Cloudflare (2025), *Rate limiting algorithms*** — ventana fija, deslizante y cubo de credenciales con sus efectos<br>  ↳ documentación · [developers.cloudflare.com](https://developers.cloudflare.com/waf/rate-limiting-rules) ✅
- **Google (2025), *API design guide: versioning and compatibility*** — cambios compatibles y versión mayor<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/apis/design/versioning) ✅
- **OpenAPI Initiative (2025), *Specification*** — documentación y validación generadas de la especificación<br>  ↳ documentación · [spec.openapis.org](https://spec.openapis.org/oas/latest.html) ✅

## [119 — Workflows y orquestación durable](../../classes/part-09-data-messaging-serverless-integration/119-workflows-y-orquestacion-durable/README.md)

- **Temporal (2025), *Workflow determinism and versioning*** — reejecución, restricciones y ramas por versión<br>  ↳ documentación · [docs.temporal.io](https://docs.temporal.io/workflows) ✅
- **Azure (2025), *Durable Functions: orchestrator code constraints*** — qué no se puede hacer en el código de orquestación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-code-constraints) ✅
- **AWS (2025), *Step Functions: standard and express workflows*** — máquina de estados declarativa y sus límites<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) ✅
- **Google Cloud (2025), *Workflows: syntax and error handling*** — pasos, reintentos y compensación declarativa<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/workflows/docs/reference/syntax) ✅
- **Richardson (2025), *Orchestration-based saga*** — cuándo centralizar la secuencia y sus compensaciones<br>  ↳ documentación · [microservices.io](https://microservices.io/patterns/index.html) ✅

## [120 — Proyecto: pipeline de pedidos orientado a eventos](../../classes/part-09-data-messaging-serverless-integration/120-proyecto-pipeline-de-pedidos-orientado-a-eventos/README.md)

- **Kleppmann (2017), *Designing Data-Intensive Applications*** — procesamiento de flujos y sistemas derivados<br>  ↳ libro · [ISBN 9781491903117](https://openlibrary.org/isbn/9781491903117) ✅
- **Richardson (2025), *Microservice patterns: data management*** — tabla de salida, secuencias con compensación y consultas<br>  ↳ documentación · [microservices.io](https://microservices.io/patterns/index.html) ✅
- **Helland (2016), *Life beyond distributed transactions*** — diseñar sin transacciones que abarquen varios servicios<br>  ↳ documentación · [queue.acm.org](https://queue.acm.org/detail.cfm?id=3025012) ✅
- **AWS (2025), *Well-Architected: reliability pillar*** — garantías, pruebas de fallo y recuperación<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) ✅
- **Google Cloud (2025), *Architecture framework: data and event-driven design*** — elección de almacén por patrón de acceso<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework) ✅
