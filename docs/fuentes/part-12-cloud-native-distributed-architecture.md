# Fuentes de la Parte 12 — Arquitectura cloud-native y sistemas distribuidos

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-12-cloud-native-distributed-architecture/README.md)

## [145 — Requisitos, restricciones y atributos de calidad](../../classes/part-12-cloud-native-distributed-architecture/145-requisitos-restricciones-y-atributos-de-calidad/README.md)

- **Bass et al. (2021), *Software Architecture in Practice*** — atributos de calidad y escenarios<br>  ↳ libro · [ISBN 9780136885672](https://openlibrary.org/isbn/9780136885672) ✅
- **SEI (2025), *Quality attribute workshop and utility tree*** — cómo obtener y priorizar escenarios<br>  ↳ documentación · [insights.sei.cmu.edu](https://insights.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition) ✅
- **Ford et al. (2017), *Building Evolutionary Architectures*** — atributos como funciones de aptitud comprobables<br>  ↳ documentación · [evolutionaryarchitecture.com](https://evolutionaryarchitecture.com) ✅
- **Conway (1968), *How do committees invent?*** — relación entre comunicación de equipos y forma del sistema<br>  ↳ documentación · [melconway.com](https://melconway.com/Home/Committees_Paper.html) ✅
- **ISO/IEC (2023), *25010: modelo de calidad del producto software*** — taxonomía de atributos<br>  ↳ norma · [iso.org](https://www.iso.org/standard/78176.html) ⏳

## [146 — Twelve-Factor App y configuración cloud-native](../../classes/part-12-cloud-native-distributed-architecture/146-twelve-factor-app-y-configuracion-cloud-native/README.md)

- **Wiggins (2011), *The Twelve-Factor App*** — la lista original y su contexto<br>  ↳ documentación · [12factor.net](https://12factor.net) ✅
- **Hoffman (2016), *Beyond the Twelve-Factor App*** — propiedades añadidas: telemetría, autenticación y seguridad<br>  ↳ libro · [ISBN 9781491944011](https://openlibrary.org/isbn/9781491944011) ✅
- **Kubernetes (2025), *Pod lifecycle: termination and probes*** — señal de terminación, plazo y señales de estado<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle) ✅
- **Google Cloud (2025), *Best practices for building containers*** — arranque, configuración y desechabilidad<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/best-practices-for-building-containers) ✅
- **OpenTelemetry (2025), *Instrumentation as a first-class output*** — telemetría como salida de la aplicación<br>  ↳ documentación · [opentelemetry.io](https://opentelemetry.io/docs/concepts/instrumentation) ✅

## [147 — DDD, bounded contexts y ownership de datos](../../classes/part-12-cloud-native-distributed-architecture/147-ddd-bounded-contexts-y-ownership-de-datos/README.md)

- **Evans (2003), *Domain-Driven Design*** — contextos acotados, mapas de contexto y capa de traducción<br>  ↳ documentación · [domainlanguage.com](https://domainlanguage.com/ddd) ✅
- **Vernon (2013), *Implementing Domain-Driven Design*** — contextos, relaciones y lenguaje<br>  ↳ documentación · [informit.com](https://informit.com/store/implementing-domain-driven-design-9780321834577) ✅
- **Brandolini (2025), *Event storming*** — encontrar fronteras a partir de los hechos del negocio<br>  ↳ documentación · [eventstorming.com](https://eventstorming.com) ✅
- **Fowler (2025), *Bounded context and integration database*** — el antipatrón de la base compartida<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/BoundedContext.html) ✅
- **Skelton et al. (2019), *Team Topologies*** — una frontera necesita un equipo detrás<br>  ↳ documentación · [teamtopologies.com](https://teamtopologies.com/book) ✅

## [148 — Monolito modular, microservicios y función](../../classes/part-12-cloud-native-distributed-architecture/148-monolito-modular-microservicios-y-funcion/README.md)

- **Fowler (2015), *Monolith first*** — por qué conviene empezar por menos unidades y dividir con motivo<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/MonolithFirst.html) ✅
- **Newman (2019), *Monolith to Microservices*** — extracción progresiva y separación de datos<br>  ↳ documentación · [samnewman.io](https://samnewman.io/books/monolith-to-microservices) ✅
- **Richardson (2025), *Microservice architecture: the pattern and its drawbacks*** — beneficios y costes explícitos<br>  ↳ documentación · [microservices.io](https://microservices.io/patterns/microservices.html) ✅
- **Tornhill (2025), *Architectural fitness functions and dependency rules*** — pruebas de arquitectura automatizadas<br>  ↳ documentación · [adamtornhill.com](https://www.adamtornhill.com/) ⏳
- **Ford et al. (2021), *Software Architecture: The Hard Parts*** — criterios de granularidad y desintegración<br>  ↳ libro · [ISBN 9781492086840](https://openlibrary.org/isbn/9781492086840) ✅

## [149 — CAP, PACELC y consistencia por operación](../../classes/part-12-cloud-native-distributed-architecture/149-cap-pacelc-y-consistencia-por-operacion/README.md)

- **Brewer (2012), *CAP twelve years later: how the rules have changed*** — el enunciado correcto y sus matices<br>  ↳ documentación · [infoq.com](https://infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed) ✅
- **Abadi (2012), *Consistency tradeoffs in modern distributed database design*** — la extensión que incluye la latencia<br>  ↳ documentación · [cs.umd.edu](https://cs.umd.edu/~abadi/papers/abadi-pacelc.pdf) ✅
- **Terry et al. (1994), *Session guarantees for weakly consistent replicated data*** — leer lo propio y no retroceder<br>  ↳ artículo · [doi:10.1109/PDIS.1994.331722](https://doi.org/10.1109/PDIS.1994.331722) ✅
- **Kleppmann (2017), *Designing Data-Intensive Applications*** — replicación, relojes y consistencia<br>  ↳ documentación · [dataintensive.net](https://dataintensive.net) ✅
- **Shapiro et al. (2011), *Conflict-free replicated data types*** — estructuras que conmutan por construcción<br>  ↳ documentación · [inria.hal.science](https://inria.hal.science/inria-00555588) ✅

## [150 — Replicación, particionado y consenso](../../classes/part-12-cloud-native-distributed-architecture/150-replicacion-particionado-y-consenso/README.md)

- **Kleppmann (2017), *Designing Data-Intensive Applications*** — replicación, particionado y consenso<br>  ↳ documentación · [dataintensive.net](https://dataintensive.net) ✅
- **Ongaro et al. (2014), *In search of an understandable consensus algorithm (Raft)*** — elección de líder y mayorías<br>  ↳ documentación · [raft.github.io](https://raft.github.io/raft.pdf) ✅
- **Kleppmann (2016), *How to do distributed locking*** — por qué un bloqueo con caducidad necesita testigo comprobado en el destino<br>  ↳ documentación · [martin.kleppmann.com](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) ✅
- **Karger et al. (1997), *Consistent hashing and random trees*** — reequilibrado sin recalcular la asignación<br>  ↳ artículo · [doi:10.1145/258533.258660](https://doi.org/10.1145/258533.258660) ✅
- **DeCandia et al. (2007), *Dynamo: Amazon's highly available key-value store*** — quórum, reparación y sus límites<br>  ↳ documentación · [allthingsdistributed.com](https://allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) ✅

## [151 — Fallos parciales y patrones de resiliencia](../../classes/part-12-cloud-native-distributed-architecture/151-fallos-parciales-y-patrones-de-resiliencia/README.md)

- **Huang et al. (2017), *Gray failure: the Achilles' heel of cloud-scale systems*** — el fallo que el componente no reconoce<br>  ↳ documentación · [microsoft.com](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf) ✅
- **Bronson et al. (2021), *Metastable failures in distributed systems*** — fallos que se sostienen tras desaparecer la causa<br>  ↳ documentación · [sigops.org](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf) ✅
- **AWS (2025), *Reliability and constant work*** — diseñar para hacer siempre la misma cantidad de trabajo<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/builders-library/reliability-and-constant-work) ✅
- **AWS (2025), *Workload isolation using shuffle sharding*** — reparto por sorteo y su aritmética<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding) ✅
- **AWS (2025), *Implementing health checks*** — vivo frente a listo y fracción sana mínima<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/builders-library/implementing-health-checks) ✅

## [152 — Service discovery, malla y comunicación](../../classes/part-12-cloud-native-distributed-architecture/152-service-discovery-malla-y-comunicacion/README.md)

- **Istio (2025), *Traffic management and mutual TLS*** — capacidades de una malla y su configuración<br>  ↳ documentación · [istio.io](https://istio.io/latest/docs/concepts/traffic-management) ✅
- **Envoy (2025), *Load balancing: algorithms and panic threshold*** — menos peticiones, dos al azar y fracción sana mínima<br>  ↳ documentación · [envoyproxy.io](https://envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/overview) ✅
- **Mitzenmacher (2001), *The power of two choices in randomized load balancing*** — por qué elegir dos al azar funciona tan bien<br>  ↳ documentación · [eecs.harvard.edu](https://eecs.harvard.edu/~michaelm/postscripts/tpds2001.pdf) ✅
- **gRPC (2025), *Load balancing with long-lived connections*** — el problema del reparto con conexiones persistentes<br>  ↳ documentación · [grpc.io](https://grpc.io/blog/grpc-load-balancing) ✅
- **Google Cloud (2025), *Service discovery patterns*** — descubrimiento en la biblioteca, en la plataforma y con intermediario<br>  ↳ documentación · [docs.cloud.google.com](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-service-discovery) ✅

## [153 — Contratos API, compatibilidad y evolución](../../classes/part-12-cloud-native-distributed-architecture/153-contratos-api-compatibilidad-y-evolucion/README.md)

- **Fowler (2011), *Tolerant reader*** — ignorar lo desconocido y depender de lo mínimo<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/TolerantReader.html) ✅
- **Fowler (2011), *Consumer-driven contracts*** — el consumidor publica lo que usa y el proveedor lo verifica<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/articles/consumerDrivenContracts.html) ✅
- **Wright (2025), *Hyrum's law*** — con suficientes consumidores, todo comportamiento observable es contrato<br>  ↳ documentación · [hyrumslaw.com](https://www.hyrumslaw.com/) ✅
- **Pact (2025), *Contract testing: broker and provider verification*** — implantación de contratos del consumidor<br>  ↳ documentación · [docs.pact.io](https://docs.pact.io) ✅
- **Google (2025), *API design guide: compatibility*** — qué cambios son compatibles y cuáles no<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/apis/design/compatibility) ✅

## [154 — Multi-tenancy, aislamiento y noisy neighbor](../../classes/part-12-cloud-native-distributed-architecture/154-multi-tenancy-aislamiento-y-noisy-neighbor/README.md)

- **AWS (2025), *SaaS tenant isolation strategies*** — niveles de aislamiento y modelos de despliegue<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html) ✅
- **PostgreSQL (2025), *Row security policies*** — filtro impuesto por la base y no por la consulta<br>  ↳ documentación · [postgresql.org](https://postgresql.org/docs/current/ddl-rowsecurity.html) ✅
- **Microsoft (2025), *Multitenant SaaS patterns: tenancy models and noisy neighbor*** — modelos y cuotas<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/architecture/guide/multitenant/overview) ✅
- **AWS (2025), *Workload isolation using shuffle sharding*** — acotar el alcance de un vecino ruidoso<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding) ✅
- **Google Cloud (2025), *Per-tenant cost attribution*** — coste por cliente con recursos compartidos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework/cost-optimization) ✅

## [155 — Rendimiento, costo, seguridad y operabilidad](../../classes/part-12-cloud-native-distributed-architecture/155-rendimiento-costo-seguridad-y-operabilidad/README.md)

- **Ford et al. (2021), *Software Architecture: The Hard Parts*** — compromisos explícitos y análisis de alternativas<br>  ↳ libro · [ISBN 9781492086840](https://openlibrary.org/isbn/9781492086840) ✅
- **Bass et al. (2021), *Software Architecture in Practice*** — evaluación de arquitecturas por atributos<br>  ↳ libro · [ISBN 9780136885672](https://openlibrary.org/isbn/9780136885672) ✅
- **SEI (2025), *ATAM: architecture tradeoff analysis method*** — puntos de compromiso y sensibilidad<br>  ↳ documentación · [insights.sei.cmu.edu](https://insights.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection) ✅
- **Google SRE (2025), *Balancing reliability, cost and velocity*** — los cuatro atributos publicados juntos<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **FinOps Foundation (2025), *Unit economics as a decision input*** — coste por unidad como columna de la decisión<br>  ↳ documentación · [finops.org](https://finops.org/framework/capabilities/unit-economics) ✅

## [156 — Proyecto: revisión de arquitectura con ADR](../../classes/part-12-cloud-native-distributed-architecture/156-proyecto-revision-de-arquitectura-con-adr/README.md)

- **Nygard (2011), *Documenting architecture decisions*** — formato y motivo del registro de decisiones<br>  ↳ documentación · [cognitect.com](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) ✅
- **SEI (2025), *Lightweight architecture evaluation*** — revisión acotada con resultado accionable<br>  ↳ documentación · [insights.sei.cmu.edu](https://insights.sei.cmu.edu/library) ✅
- **Ford et al. (2017), *Building Evolutionary Architectures*** — funciones de aptitud y revisión continua<br>  ↳ documentación · [evolutionaryarchitecture.com](https://evolutionaryarchitecture.com) ✅
- **ADR GitHub organization (2025), *Architecture decision records: templates and tooling*** — plantillas y prácticas<br>  ↳ documentación · [adr.github.io](https://adr.github.io) ✅
- **Ford et al. (2021), *Software Architecture: The Hard Parts*** — registrar compromisos y revisarlos<br>  ↳ libro · [ISBN 9781492086840](https://openlibrary.org/isbn/9781492086840) ✅
