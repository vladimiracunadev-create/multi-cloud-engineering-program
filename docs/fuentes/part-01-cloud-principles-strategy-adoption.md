# Fuentes de la Parte 01 — Principios, estrategia y adopción cloud

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-01-cloud-principles-strategy-adoption/README.md)

## [013 — Definición NIST y características esenciales de cloud](../../classes/part-01-cloud-principles-strategy-adoption/013-definicion-nist-y-caracteristicas-esenciales-de-cloud/README.md)

- **Mell et al. (2011), *The NIST Definition of Cloud Computing*** — las cinco características, tres modelos de servicio y cuatro de despliegue<br>  ↳ artículo · [doi:10.6028/NIST.SP.800-145](https://doi.org/10.6028/NIST.SP.800-145) ✅
- **Liu (2011), *NIST Cloud Computing Reference Architecture*** — actores, roles y sus relaciones<br>  ↳ artículo · [doi:10.6028/NIST.SP.500-292](https://doi.org/10.6028/NIST.SP.500-292) ✅
- **Hohpe (2020), *Cloud Strategy: A Decision-Based Approach*** — por qué la definición sirve para decidir y no para clasificar<br>  ↳ libro · [ISBN 9798665253046](https://openlibrary.org/isbn/9798665253046) ✅
- **Armbrust (2010), *A View of Cloud Computing*** — obstáculos y oportunidades, incluida la variabilidad de rendimiento<br>  ↳ artículo · [doi:10.1145/1721654.1721672](https://doi.org/10.1145/1721654.1721672) ✅
- **Barroso et al. (2018), *The Datacenter as a Computer*** — economía de la agrupación de recursos<br>  ↳ artículo · [doi:10.2200/S00874ED3V01Y201809CAC046](https://doi.org/10.2200/S00874ED3V01Y201809CAC046) ✅

## [014 — Regiones, zonas de disponibilidad, puntos de presencia y edge](../../classes/part-01-cloud-principles-strategy-adoption/014-regiones-zonas-de-disponibilidad-puntos-de-presencia-y-edge/README.md)

- **AWS (2024), *Regions, Availability Zones, and Local Zones*** — identificadores estables de zona y su mapeo por cuenta<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) ✅
- **Microsoft (2024), *Azure regions and availability zones*** — modelo de zonas y servicios con soporte por región<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) ✅
- **Google Cloud (2024), *Geography and regions*** — jerarquía región/zona y ubicación de recursos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/docs/geography-and-regions) ✅
- **Beyer (2016), *Site Reliability Engineering*** — independencia de dominios de fallo<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/addressing-cascading-failures) ✅
- **Brewer (2012), *CAP Twelve Years Later: How the Rules Have Changed*** — por qué la latencia entre regiones fuerza replicación asíncrona<br>  ↳ artículo · [doi:10.1109/MC.2012.37](https://doi.org/10.1109/MC.2012.37) ✅

## [015 — IaaS, PaaS, SaaS, CaaS y FaaS](../../classes/part-01-cloud-principles-strategy-adoption/015-iaas-paas-saas-caas-y-faas/README.md)

- **Mell et al. (2011), *The NIST Definition of Cloud Computing*** — los tres modelos de servicio originales<br>  ↳ artículo · [doi:10.6028/NIST.SP.800-145](https://doi.org/10.6028/NIST.SP.800-145) ✅
- **AWS (2024), *Lambda quotas*** — techo de duración, memoria, tamaño de paquete y concurrencia<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) ✅
- **Google Cloud (2024), *Cloud Run functions: quotas and limits*** — límites de la 1.ª y 2.ª generación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/functions/quotas) ✅
- **Jonas (2019), *Cloud Programming Simplified: A Berkeley View on Serverless Computing*** — límites estructurales del modelo de funciones<br>  ↳ artículo · [doi:10.48550/arXiv.1902.03383](https://doi.org/10.48550/arXiv.1902.03383) ✅
- **Hohpe (2020), *Cloud Strategy*** — descomposición del coste de salida en datos, API y operación<br>  ↳ libro · [ISBN 9798665253046](https://openlibrary.org/isbn/9798665253046) ✅

## [016 — Elasticidad, escalabilidad, disponibilidad y resiliencia](../../classes/part-01-cloud-principles-strategy-adoption/016-elasticidad-escalabilidad-disponibilidad-y-resiliencia/README.md)

- **Amdahl (1967), *Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities*** — el techo teórico que impone la fracción no paralelizable<br>  ↳ artículo · [doi:10.1145/1465482.1465560](https://doi.org/10.1145/1465482.1465560) ✅
- **Gunther (2007), *Guerrilla Capacity Planning*** — ley universal de escalabilidad y ajuste de σ y κ<br>  ↳ libro · [ISBN 9783540261384](https://openlibrary.org/isbn/9783540261384) ✅
- **Beyer (2016), *Site Reliability Engineering*** — degradación elegante y rechazo de carga<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/addressing-cascading-failures) ✅
- **Nygard (2018), *Release It!*** — patrones de estabilidad frente a fallo en cascada<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅
- **Fielding et al. (2022), *RFC 9110*** — código 429 y cabecera Retry-After<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc9110) ✅

## [017 — Tenancy, cuentas, suscripciones, proyectos y jerarquías](../../classes/part-01-cloud-principles-strategy-adoption/017-tenancy-cuentas-suscripciones-proyectos-y-jerarquias/README.md)

- **AWS (2024), *Organizations: service control policies*** — evaluación de políticas heredadas y servicios globales<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) ✅
- **Microsoft (2024), *Cloud Adoption Framework: resource organization*** — grupos de administración, suscripciones y grupos de recursos<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources) ✅
- **Google Cloud (2024), *Resource hierarchy*** — organización, carpetas, proyectos y herencia de políticas<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) ✅
- **AWS (2024), *Organizing your AWS environment using multiple accounts*** — criterios de separación por cuenta<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) ✅
- **Beyer (2018), *The Site Reliability Workbook*** — gestión de capacidad y cuotas<br>  ↳ documentación · [sre.google](https://sre.google/workbook/managing-load) ✅

## [018 — Identidad, roles, políticas y federación](../../classes/part-01-cloud-principles-strategy-adoption/018-identidad-roles-politicas-y-federacion/README.md)

- **AWS (2024), *Policy evaluation logic*** — orden de evaluación, denegación explícita e implícita<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) ✅
- **GitHub (2024), *About security hardening with OpenID Connect*** — declaraciones del token y condiciones de confianza<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) ✅
- **Sakimura (2014), *OpenID Connect Core 1.0*** — semántica de las declaraciones `sub` y `aud`<br>  ↳ documentación · [openid.net](https://openid.net/specs/openid-connect-core-1_0.html) ✅
- **NIST (2020), *Zero Trust Architecture*** — verificación por petición y credenciales de vida corta<br>  ↳ artículo · [doi:10.6028/NIST.SP.800-207](https://doi.org/10.6028/NIST.SP.800-207) ✅
- **Dotson (2023), *Practical Cloud Security*** — gestión de identidad y privilegio mínimo iterativo<br>  ↳ libro · [ISBN 9781098148171](https://openlibrary.org/isbn/9781098148171) ✅

## [019 — Modelo de responsabilidad compartida por servicio](../../classes/part-01-cloud-principles-strategy-adoption/019-modelo-de-responsabilidad-compartida-por-servicio/README.md)

- **AWS (2024), *Shared Responsibility Model*** — controles heredados, compartidos y propios del cliente<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/compliance/shared-responsibility-model) ✅
- **Microsoft (2024), *Shared responsibility in the cloud*** — reparto por modelo de servicio con tabla de controles<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) ✅
- **Cloud Security Alliance (2024), *Cloud Controls Matrix*** — catálogo de controles con reparto proveedor/cliente<br>  ↳ documentación · [cloudsecurityalliance.org](https://cloudsecurityalliance.org/research/cloud-controls-matrix) ✅
- **AICPA (2017), *SOC 2 Trust Services Criteria*** — estructura del informe y controles complementarios del usuario<br>  ↳ documentación · [aicpa-cima.com](https://aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) ✅
- **Dotson (2023), *Practical Cloud Security*** — construir la matriz de responsabilidad servicio a servicio<br>  ↳ libro · [ISBN 9781098148171](https://openlibrary.org/isbn/9781098148171) ✅

## [020 — TCO, costos variables, unit economics y FinOps](../../classes/part-01-cloud-principles-strategy-adoption/020-tco-costos-variables-unit-economics-y-finops/README.md)

- **Storment et al. (2023), *Cloud FinOps*** — modelo de coste unitario y previsión<br>  ↳ libro · [ISBN 9781492098355](https://openlibrary.org/isbn/9781492098355) ✅
- **FinOps Foundation (2024), *Unit Economics*** — definición y construcción de métricas por unidad de negocio<br>  ↳ documentación · [finops.org](https://finops.org/framework/capabilities/unit-economics) ✅
- **Brealey et al. (2020), *Principles of Corporate Finance*** — VAN, TIR y costes hundidos<br>  ↳ libro · [ISBN 9781260013900](https://openlibrary.org/isbn/9781260013900) ✅
- **Hohpe (2020), *Cloud Strategy*** — por qué el ahorro de la nube rara vez viene de donde se anuncia<br>  ↳ libro · [ISBN 9798665253046](https://openlibrary.org/isbn/9798665253046) ✅
- **Barroso et al. (2018), *The Datacenter as a Computer*** — TCO de un centro de datos<br>  ↳ artículo · [doi:10.2200/S00874ED3V01Y201809CAC046](https://doi.org/10.2200/S00874ED3V01Y201809CAC046) ✅

## [021 — Well-Architected y atributos de calidad](../../classes/part-01-cloud-principles-strategy-adoption/021-well-architected-y-atributos-de-calidad/README.md)

- **AWS (2024), *Well-Architected Framework*** — seis pilares, preguntas y proceso de revisión<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) ✅
- **Microsoft (2024), *Azure Well-Architected Framework*** — pilares y compromisos entre ellos<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/well-architected) ✅
- **Google Cloud (2024), *Architecture Framework*** — pilares y guía de diseño<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework) ✅
- **Bass et al. (2021), *Software Architecture in Practice*** — escenarios de atributos de calidad en seis partes<br>  ↳ libro · [ISBN 9780136885672](https://openlibrary.org/isbn/9780136885672) ✅
- **Richards et al. (2020), *Fundamentals of Software Architecture*** — «todo en arquitectura es un compromiso»<br>  ↳ libro · [ISBN 9781492043454](https://openlibrary.org/isbn/9781492043454) ✅

## [022 — Cloud Adoption Framework y modelo operativo](../../classes/part-01-cloud-principles-strategy-adoption/022-cloud-adoption-framework-y-modelo-operativo/README.md)

- **Conway (1968), *How Do Committees Invent?*** — por qué la arquitectura acaba reproduciendo el organigrama<br>  ↳ documentación · [melconway.com](https://melconway.com/Home/Committees_Paper.html) ✅
- **Skelton et al. (2019), *Team Topologies*** — cuatro tipos de equipo, carga cognitiva y maniobra de Conway inversa<br>  ↳ libro · [ISBN 9781942788829](https://openlibrary.org/isbn/9781942788829) ✅
- **Forsgren et al. (2018), *Accelerate*** — evidencia sobre estructura organizativa y rendimiento de entrega<br>  ↳ libro · [ISBN 9781942788379](https://openlibrary.org/isbn/9781942788379) ✅
- **Microsoft (2024), *Cloud Adoption Framework*** — fases de estrategia, planificación, preparación y adopción<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework) ✅
- **AWS (2024), *Cloud Adoption Framework*** — seis perspectivas, incluidas las de personas y gobierno<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/cloud-adoption-framework) ✅

## [023 — Descubrimiento y clasificación de workloads](../../classes/part-01-cloud-principles-strategy-adoption/023-descubrimiento-y-clasificacion-de-workloads/README.md)

- **AWS (2024), *Migration strategies: the 7 Rs*** — criterios de elección por estrategia<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html) ✅
- **Microsoft (2024), *Cloud Adoption Framework: assess workloads*** — inventario, dependencias y clasificación<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/plan/discover-existing-workload-inventory) ✅
- **McCrory (2010), *Data Gravity in the Clouds*** — por qué los datos atraen a las aplicaciones<br>  ↳ documentación · [datagravitas.com](https://datagravitas.com/2010/12/07/data-gravity-in-the-clouds) ✅
- **Google Cloud (2024), *Migration to Google Cloud: assess and discover workloads*** — descubrimiento y agrupación<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/migration-to-gcp-getting-started) ✅
- **Newman (2019), *Monolith to Microservices*** — identificar fronteras y grupos acoplados antes de partir<br>  ↳ libro · [ISBN 9781492047841](https://openlibrary.org/isbn/9781492047841) ✅

## [024 — Proyecto: decisión de migración sustentada con ADR](../../classes/part-01-cloud-principles-strategy-adoption/024-proyecto-decision-de-migracion-sustentada-con-adr/README.md)

- **Nygard (2011), *Documenting Architecture Decisions*** — formato original de los ADR<br>  ↳ documentación · [cognitect.com](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) ✅
- **Keeling et al. (2017), *Share the Load: Distribute Design Authority with Architecture Decision Records*** — cómo repartir autoridad de diseño mediante registros de decisión<br>  ↳ documentación · [agilealliance.org](https://agilealliance.org/resources/experience-reports/distribute-design-authority-with-architecture-decision-records) ✅
- **Bezos (2016), *Letter to Shareholders*** — decisiones de tipo 1 y tipo 2 según su reversibilidad<br>  ↳ documentación · [sec.gov](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm) ⏳
- **Ford et al. (2017), *Building Evolutionary Architectures*** — funciones de aptitud y decisiones con condición de revisión<br>  ↳ libro · [ISBN 9781491986363](https://openlibrary.org/isbn/9781491986363) ✅
- **Richards et al. (2020), *Fundamentals of Software Architecture*** — registro y comunicación de decisiones<br>  ↳ libro · [ISBN 9781492043454](https://openlibrary.org/isbn/9781492043454) ✅
