# Fuentes de la Parte 15 — Arquitectura de sistemas e ingeniería de requisitos

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-15-systems-architecture-engineering/README.md)

## [181 — Requisitos funcionales, restricciones y atributos de calidad](../../classes/part-15-systems-architecture-engineering/181-requisitos-funcionales-restricciones-y-atributos-de-calidad/README.md)

- **Bass et al. (2021), *Software Architecture in Practice*** — escenarios de atributos de calidad<br>  ↳ libro · [ISBN 9780136885672](https://openlibrary.org/isbn/9780136885672) ✅
- **SEI (2006), *Quality Attribute Workshops*** — técnica para extraer atributos de calidad de los interesados<br>  ↳ documentación · [insights.sei.cmu.edu](https://insights.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition) ✅
- **Ford et al. (2017), *Building Evolutionary Architectures*** — características arquitectónicas y su priorización<br>  ↳ libro · [ISBN 9781491986363](https://openlibrary.org/isbn/9781491986363) ✅
- ***ISO/IEC 25010*** — modelo de calidad de producto software<br>  ↳ norma · [iso.org](https://www.iso.org/standard/78176.html) ⏳
- **AWS (2025), *Well-Architected Framework*** — atributos y compromisos entre pilares<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) ✅

## [182 — Contexto, contenedores, componentes y código con C4](../../classes/part-15-systems-architecture-engineering/182-contexto-contenedores-componentes-y-codigo-con-c4/README.md)

- **Brown (2025), *The C4 model for visualising software architecture*** — los cuatro niveles de abstracción del diagrama<br>  ↳ documentación · [c4model.com](https://c4model.com) ✅
- **Brown (2019), *Software Architecture for Developers*** — niveles de abstracción y documentación mínima útil<br>  ↳ documentación · [leanpub.com](https://leanpub.com/software-architecture-for-developers) ✅
- **Clements et al. (2010), *Documenting Software Architectures*** — vistas y su audiencia<br>  ↳ libro · [ISBN 9780321552686](https://openlibrary.org/isbn/9780321552686) ✅
- **Structurizr (2025), *Diagrams as code*** — diagramas versionados junto al código<br>  ↳ documentación · [structurizr.com](https://structurizr.com) ✅
- **Mermaid (2025), *Flowchart syntax*** — diagramas como texto en el repositorio<br>  ↳ documentación · [mermaid.js.org](https://mermaid.js.org/syntax/flowchart.html) ✅

## [183 — Acoplamiento, cohesión, modularidad y fronteras](../../classes/part-15-systems-architecture-engineering/183-acoplamiento-cohesion-modularidad-y-fronteras/README.md)

- **Parnas (1972), *On the criteria to be used in decomposing systems into modules*** — el criterio de ocultación de información para trazar fronteras de módulo<br>  ↳ artículo · [doi:10.1145/361598.361623](https://doi.org/10.1145/361598.361623) ✅
- **Newman (2019), *Monolith to Microservices*** — acoplamiento por datos y cómo dividirlo<br>  ↳ libro · [ISBN 9781492047841](https://openlibrary.org/isbn/9781492047841) ✅
- **Tornhill (2018), *Software Design X-Rays*** — cambios acoplados medidos sobre el historial<br>  ↳ libro · [ISBN 9781680502725](https://openlibrary.org/isbn/9781680502725) ✅
- **Evans (2003), *Domain-Driven Design*** — contextos delimitados y sus fronteras<br>  ↳ libro · [ISBN 9780321125217](https://openlibrary.org/isbn/9780321125217) ✅
- **Conway (1968), *How do committees invent?*** — la frontera y el organigrama<br>  ↳ documentación · [melconway.com](https://melconway.com/Home/Committees_Paper.html) ✅

## [184 — Arquitectura monolítica, modular y de microservicios](../../classes/part-15-systems-architecture-engineering/184-arquitectura-monolitica-modular-y-de-microservicios/README.md)

- **Newman (2021), *Building Microservices*** — cuándo separar y qué cuesta<br>  ↳ libro · [ISBN 9781492034025](https://openlibrary.org/isbn/9781492034025) ✅
- **Fowler (2015), *MonolithFirst*** — empezar junto y separar con evidencia<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/MonolithFirst.html) ✅
- **Fowler (2004), *StranglerFigApplication*** — migración por estrangulamiento<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/StranglerFigApplication.html) ✅
- **Shopify Engineering (2019), *Deconstructing the monolith*** — monolito modular a escala<br>  ↳ documentación · [shopify.engineering](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) ✅
- **Skelton et al. (2019), *Team Topologies*** — servicios, equipos y carga cognitiva<br>  ↳ documentación · [teamtopologies.com](https://teamtopologies.com/book) ✅

## [185 — Disponibilidad, confiabilidad y análisis de puntos de fallo](../../classes/part-15-systems-architecture-engineering/185-disponibilidad-confiabilidad-y-analisis-de-puntos-de-fallo/README.md)

- **Beyer et al. (2016), *Site Reliability Engineering*** — aritmética de disponibilidad y coste de cada nueve<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/embracing-risk) ✅
- **AWS (2025), *Reliability Pillar: failure management*** — modos de fallo y dependencias<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) ✅
- **Huang et al. (2017), *Gray failure: the Achilles' heel of cloud-scale systems*** — fallos parciales que una comprobación binaria de salud no detecta<br>  ↳ documentación · [microsoft.com](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf) ✅
- **Nygard (2018), *Release It!*** — mamparos, plazos y fallo en cascada<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅
- **Google Cloud (2025), *Designing resilient systems*** — dependencias duras, blandas y degradación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework/reliability) ✅

## [186 — Capacidad, latencia, throughput y teoría de colas](../../classes/part-15-systems-architecture-engineering/186-capacidad-latencia-throughput-y-teoria-de-colas/README.md)

- **Little (1961), *A proof for the queuing formula L = λW*** — la relación L = λW aplicada al dimensionamiento de capacidad<br>  ↳ documentación · [pubsonline.informs.org](https://pubsonline.informs.org/doi/10.1287/opre.9.3.383) ⏳
- **Gunther (2007), *Guerrilla Capacity Planning*** — utilización, escalabilidad y sus límites<br>  ↳ artículo · [doi:10.1007/978-3-540-31010-5](https://doi.org/10.1007/978-3-540-31010-5) ✅
- **Schroeder et al. (2006), *Open versus closed: a cautionary tale*** — por qué el modelo de carga cambia las conclusiones del ensayo<br>  ↳ documentación · [usenix.org](https://usenix.org/legacy/event/nsdi06/tech/schroeder.html) ✅
- **Harchol-Balter (2013), *Performance Modeling and Design of Computer Systems*** — colas y variabilidad<br>  ↳ documentación · [cambridge.org](https://www.cambridge.org/core/books/performance-modeling-and-design-of-computer-systems/8E5B6F1D9E2E1E4B2A4C0B9B1B0E3E0D) ⏳
- **Google (2016), *SRE Book: addressing cascading failures*** — realimentación, rechazo y plazos<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/addressing-cascading-failures) ✅

## [187 — Consistencia, particiones, relojes y consenso](../../classes/part-15-systems-architecture-engineering/187-consistencia-particiones-relojes-y-consenso/README.md)

- **Gilbert et al. (2002), *Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services*** — la demostración formal del compromiso entre consistencia y disponibilidad<br>  ↳ artículo · [doi:10.1145/564585.564601](https://doi.org/10.1145/564585.564601) ✅
- **Abadi (2012), *Consistency tradeoffs in modern distributed database system design (PACELC)*** — el compromiso entre latencia y consistencia cuando no hay partición<br>  ↳ artículo · [ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/6127847) ⏳
- **Lamport (1978), *Time, clocks, and the ordering of events in a distributed system*** — orden causal de eventos sin reloj global<br>  ↳ artículo · [doi:10.1145/359545.359563](https://doi.org/10.1145/359545.359563) ✅
- **Ongaro et al. (2014), *In search of an understandable consensus algorithm (Raft)*** — consenso comprensible como alternativa a Paxos<br>  ↳ documentación · [raft.github.io](https://raft.github.io/raft.pdf) ✅
- **Kleppmann (2017), *Designing Data-Intensive Applications*** — replicación, consistencia y consenso<br>  ↳ documentación · [dataintensive.net](https://dataintensive.net) ✅

## [188 — Contratos de API, eventos y compatibilidad evolutiva](../../classes/part-15-systems-architecture-engineering/188-contratos-de-api-eventos-y-compatibilidad-evolutiva/README.md)

- **Wright (2017), *Hyrum's Law*** — por qué todo comportamiento observable acaba siendo contrato<br>  ↳ documentación · [hyrumslaw.com](https://www.hyrumslaw.com/) ✅
- **Confluent (2025), *Schema evolution and compatibility*** — reglas hacia atrás y hacia delante en eventos<br>  ↳ documentación · [docs.confluent.io](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) ✅
- **Pact (2025), *Consumer-driven contract testing*** — verificar compatibilidad desde las expectativas del consumidor<br>  ↳ documentación · [docs.pact.io](https://docs.pact.io) ✅
- **Google (2025), *API Improvement Proposals: versioning and compatibility*** — reglas de versionado y compatibilidad evolutiva<br>  ↳ documentación · [google.aip.dev](https://google.aip.dev/180) ✅
- **Ambler et al. (2006), *Refactoring Databases*** — expandir y contraer aplicado a esquemas<br>  ↳ libro · [ISBN 9780321630179](https://openlibrary.org/isbn/9780321630179) ✅

## [189 — Modelado de amenazas y arquitectura de confianza cero](../../classes/part-15-systems-architecture-engineering/189-modelado-de-amenazas-y-arquitectura-de-confianza-cero/README.md)

- **Shostack (2014), *Threat Modeling: Designing for Security*** — las cuatro preguntas del modelado de amenazas<br>  ↳ documentación · [shostack.org](https://shostack.org/books/threat-modeling-book) ✅
- ***Threat Modeling Manifesto (2020)*** — las cuatro preguntas<br>  ↳ documentación · [threatmodelingmanifesto.org](https://threatmodelingmanifesto.org) ✅
- **NIST SP 800-207 (2020), *Zero Trust Architecture*** — los principios de confianza cero aplicados a la arquitectura<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/207/final) ✅
- **Microsoft (2025), *STRIDE threat model*** — las seis categorías de amenaza aplicadas al diseño<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) ✅
- **Google (2024), *BeyondProd*** — confianza cero aplicada a cargas y canalizaciones<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/docs/security/beyondprod) ✅

## [190 — ADRs, fitness functions y gobierno de decisiones](../../classes/part-15-systems-architecture-engineering/190-adrs-fitness-functions-y-gobierno-de-decisiones/README.md)

- **Nygard (2011), *Documenting architecture decisions*** — el formato mínimo de un registro de decisión<br>  ↳ documentación · [cognitect.com](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) ✅
- **Ford et al. (2017), *Building Evolutionary Architectures*** — funciones de aptitud<br>  ↳ libro · [ISBN 9781491986363](https://openlibrary.org/isbn/9781491986363) ✅
- **ThoughtWorks (2025), *Technology Radar: lightweight ADRs*** — cuándo basta un ADR ligero<br>  ↳ documentación · [thoughtworks.com](https://thoughtworks.com/radar/techniques/lightweight-architecture-decision-records) ✅
- **ArchUnit (2025), *Testing architecture rules in the build*** — funciones de aptitud que hacen fallar la construcción<br>  ↳ documentación · [archunit.org](https://archunit.org) ✅
- **Open Policy Agent (2025), *Policy as code*** — comprobaciones ejecutables en la canalización<br>  ↳ documentación · [openpolicyagent.org](https://openpolicyagent.org/docs/latest) ✅

## [191 — Architecture review y comunicación con stakeholders](../../classes/part-15-systems-architecture-engineering/191-architecture-review-y-comunicacion-con-stakeholders/README.md)

- **Clements et al. (2001), *Evaluating Software Architectures: Methods and Case Studies*** — métodos de evaluación de arquitectura con casos reales<br>  ↳ libro · [ISBN 9780201704822](https://openlibrary.org/isbn/9780201704822) ✅
- **SEI (2000), *ATAM: Method for Architecture Evaluation*** — el procedimiento de evaluación por escenarios<br>  ↳ documentación · [insights.sei.cmu.edu](https://insights.sei.cmu.edu/library/atam-method-for-architecture-evaluation) ✅
- **Bass et al. (2021), *Software Architecture in Practice*** — vocabulario de atributos de calidad para conducir la revisión<br>  ↳ libro · [ISBN 9780136885672](https://openlibrary.org/isbn/9780136885672) ✅
- **Brown (2019), *Software Architecture for Developers, vol. 2*** — comunicación por audiencias<br>  ↳ documentación · [leanpub.com](https://leanpub.com/visualising-software-architecture) ✅
- **Google (2025), *Architecture review practices*** — cómo conducir la revisión con los interesados<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework) ✅

## [192 — Proyecto: arquitectura completa de CloudShop](../../classes/part-15-systems-architecture-engineering/192-proyecto-arquitectura-completa-de-cloudshop/README.md)

- **Bass et al. (2021), *Software Architecture in Practice*** — estructura de la documentación de arquitectura del proyecto<br>  ↳ libro · [ISBN 9780136885672](https://openlibrary.org/isbn/9780136885672) ✅
- **Ford et al. (2021), *Software Architecture: The Hard Parts*** — decisiones con compromisos explícitos<br>  ↳ libro · [ISBN 9781492086840](https://openlibrary.org/isbn/9781492086840) ✅
- **Kleppmann (2017), *Designing Data-Intensive Applications*** — decisiones de almacenamiento y replicación del caso<br>  ↳ documentación · [dataintensive.net](https://dataintensive.net) ✅
- **AWS (2025), *Well-Architected Framework*** — los pilares como lista de verificación del diseño<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) ✅
- **Google (2025), *Cloud Architecture Framework*** — contraste del diseño con el marco de Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework) ✅
