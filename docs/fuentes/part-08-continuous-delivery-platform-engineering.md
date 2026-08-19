# Fuentes de la Parte 08 — Entrega continua y platform engineering

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-08-continuous-delivery-platform-engineering/README.md)

## [097 — Integración continua, trunk-based development y feedback](../../classes/part-08-continuous-delivery-platform-engineering/097-integracion-continua-trunk-based-development-y-feedback/README.md)

- **Jez Humble (2010), *Continuous Delivery*** — integración continua y línea principal desplegable<br>  ↳ documentación · [continuousdelivery.com](https://continuousdelivery.com) ✅
- **Martin Fowler (2023), *Patterns for managing source code branches*** — tiempo de vida de ramas y técnicas de división<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/articles/branching-patterns.html) ✅
- **Paul Hammant (2020), *Branch by abstraction*** — sustituir un componente sin rama larga<br>  ↳ documentación · [branchbyabstraction.com](https://branchbyabstraction.com) ✅
- **Google (2020), *Flaky tests at scale*** — causas, cuarentena y coste de la intermitencia<br>  ↳ documentación · [testing.googleblog.com](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html) ✅
- **Nicole Forsgren et al (2018), *Accelerate*** — tiempo de entrega, lotes pequeños y su efecto medido<br>  ↳ libro · [ISBN 9781942788379](https://openlibrary.org/isbn/9781942788379) ✅

## [098 — GitHub Actions: workflows, runners, permisos y caché](../../classes/part-08-continuous-delivery-platform-engineering/098-github-actions-workflows-runners-permisos-y-cache/README.md)

- **GitHub (2025), *Security hardening for GitHub Actions*** — disparadores, inyección, permisos y acciones de terceros<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) ✅
- **GitHub (2025), *About OpenID Connect in GitHub Actions*** — identidad federada y condiciones de confianza<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect) ✅
- **GitHub (2025), *Self-hosted runners: security considerations*** — riesgos y ejecutores efímeros<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners) ✅
- **GitHub (2025), *Caching dependencies*** — claves, claves de respaldo, alcance y expulsión<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows) ✅
- **OpenSSF (2025), *Scorecard checks for CI/CD*** — fijación por revisión, permisos y automatización de la revisión<br>  ↳ documentación · [github.com](https://github.com/ossf/scorecard/blob/main/docs/checks.md) ✅

## [099 — Artefactos inmutables, semver y promoción](../../classes/part-08-continuous-delivery-platform-engineering/099-artefactos-inmutables-semver-y-promocion/README.md)

- **Jez Humble (2010), *Continuous Delivery*** — gestión de artefactos y promoción entre entornos<br>  ↳ documentación · [continuousdelivery.com](https://continuousdelivery.com) ✅
- **Semantic Versioning (2013), *SemVer 2.0.0*** — el contrato que expresa una versión<br>  ↳ documentación · [semver.org](https://semver.org) ✅
- **Sigstore (2025), *In-toto attestations with cosign*** — evidencia adjunta a un artefacto por su huella<br>  ↳ documentación · [docs.sigstore.dev](https://docs.sigstore.dev/cosign/verifying/attestation) ✅
- **OCI (2025), *Referrers API*** — objetos asociados a un artefacto en el registro<br>  ↳ documentación · [github.com](https://github.com/opencontainers/distribution-spec/blob/main/spec.md) ✅
- **Google (2025), *Artifact Registry cleanup policies*** — retención y exclusión de lo que está en uso<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) ✅

## [100 — Pruebas, calidad y puertas de cambio](../../classes/part-08-continuous-delivery-platform-engineering/100-pruebas-calidad-y-puertas-de-cambio/README.md)

- **Martin Fowler (2012), *Test Pyramid*** — coste y confianza por nivel, y por qué la forma varía<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/TestPyramid.html) ✅
- **Ham Vocke (2018), *The practical test pyramid*** — niveles, dobles y contratos con ejemplos<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html) ✅
- **Pact (2025), *Consumer-driven contract testing*** — generación del contrato y verificación en el proveedor<br>  ↳ documentación · [docs.pact.io](https://docs.pact.io) ✅
- **Martin Fowler (2020), *Test coverage*** — por qué la cobertura como objetivo produce malas pruebas<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/TestCoverage.html) ✅
- **Google (2024), *Mutation testing at scale*** — medir si las pruebas comprueban, y su coste<br>  ↳ documentación · [research.google](https://research.google/pubs/state-of-mutation-testing-at-google) ✅

## [101 — SAST, SCA, secretos, SBOM y firma en pipeline](../../classes/part-08-continuous-delivery-platform-engineering/101-sast-sca-secretos-sbom-y-firma-en-pipeline/README.md)

- **OWASP (2025), *DevSecOps guideline: tooling and placement*** — familias de comprobación y dónde ejecutarlas<br>  ↳ documentación · [owasp.org](https://owasp.org/www-project-devsecops-guideline) ✅
- **OpenSSF (2025), *Scorecard and CI/CD security checks*** — comprobaciones automatizables sobre la canalización<br>  ↳ documentación · [github.com](https://github.com/ossf/scorecard/blob/main/docs/checks.md) ✅
- **CISA (2025), *Vulnerability Exploitability eXchange*** — declarar si una vulnerabilidad afecta y por qué<br>  ↳ documentación · [cisa.gov](https://www.cisa.gov/resources-tools/resources/minimum-requirements-vulnerability-exploitability-exchange-vex) ⏳
- **GitHub (2025), *Push protection for secrets*** — rechazar el envío antes de que el secreto entre en el historial<br>  ↳ documentación · [docs.github.com](https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations) ✅
- **Semgrep (2025), *Diff-aware scanning*** — bloquear solo hallazgos nuevos respecto de una referencia<br>  ↳ documentación · [semgrep.dev](https://semgrep.dev/docs/deployment/customize-ci-jobs) ✅

## [102 — Rolling, blue-green, canary y rollback](../../classes/part-08-continuous-delivery-platform-engineering/102-rolling-blue-green-canary-y-rollback/README.md)

- **Humble et al. (2010), *Continuous Delivery*** — despliegues azul-verde, canario y reversión<br>  ↳ libro · [ISBN 9780321670250](https://openlibrary.org/isbn/9780321670250) ✅
- **Google SRE (2025), *Canarying releases*** — control simultáneo, potencia del análisis y automatización del veredicto<br>  ↳ documentación · [sre.google](https://sre.google/workbook/canarying-releases) ✅
- **Kubernetes (2025), *Deployment strategies and rollbacks*** — mecánica de progresiva y reversión<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/deployment) ✅
- **Argo Rollouts (2025), *Analysis and progressive delivery*** — escalones, métricas y reversión automática<br>  ↳ documentación · [argo-rollouts.readthedocs.io](https://argo-rollouts.readthedocs.io/en/stable/features/analysis) ✅
- **Fowler (2025), *Parallel change (expand and contract)*** — cambiar un contrato sin romper la convivencia<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/ParallelChange.html) ✅

## [103 — GitOps con Argo CD o Flux](../../classes/part-08-continuous-delivery-platform-engineering/103-gitops-con-argo-cd-o-flux/README.md)

- **OpenGitOps (2025), *GitOps principles*** — declarativo, versionado, extraído automáticamente y reconciliado de forma continua<br>  ↳ documentación · [opengitops.dev](https://opengitops.dev) ✅
- **Argo CD (2025), *Diffing customization and resource pruning*** — propiedad de campo, exclusiones y protecciones de poda<br>  ↳ documentación · [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing) ✅
- **Flux (2025), *Bootstrap and reconciliation*** — agente dentro del clúster, intervalos y estado de sincronización<br>  ↳ documentación · [fluxcd.io](https://fluxcd.io/flux/installation/bootstrap) ✅
- **External Secrets Operator (2025), *SecretStore and ExternalSecret*** — declarar la referencia sin guardar el valor<br>  ↳ documentación · [external-secrets.io](https://external-secrets.io/latest/introduction/overview) ✅
- **CNCF (2025), *GitOps working group: multi-environment promotion*** — repositorio de entorno y promoción por huella<br>  ↳ documentación · [github.com](https://github.com/cncf/tag-app-delivery) ✅

## [104 — Ambientes efímeros y promoción entre entornos](../../classes/part-08-continuous-delivery-platform-engineering/104-ambientes-efimeros-y-promocion-entre-entornos/README.md)

- **Fowler (2025), *Test doubles and contract tests*** — dobles por contrato y verificación contra el servicio real<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/ContractTest.html) ✅
- **Argo CD (2025), *ApplicationSet: pull request generator*** — un entorno por cambio propuesto, y su destrucción al cerrarlo<br>  ↳ documentación · [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request) ✅
- **ICO (2025), *Anonymisation and re-identification risk*** — por qué sustituir identificadores directos no basta<br>  ↳ documentación · [ico.org.uk](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/introduction-to-anonymisation/) ✅
- **FinOps Foundation (2025), *Tagging and orphaned resource detection*** — encontrar lo que quedó vivo sin dueño<br>  ↳ documentación · [finops.org](https://www.finops.org/framework/previous-capabilities/utilization-efficiency/) ✅
- **Testcontainers (2025), *Ephemeral dependencies for tests*** — dependencias desechables con ciclo de vida acotado<br>  ↳ documentación · [testcontainers.com](https://testcontainers.com/guides) ✅

## [105 — Feature flags y separación deploy-release](../../classes/part-08-continuous-delivery-platform-engineering/105-feature-flags-y-separacion-deploy-release/README.md)

- **Hodgson (2025), *Feature toggles: types and lifecycle*** — clasificación por vida esperada y coste de mantenimiento<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/articles/feature-toggles.html) ✅
- **Humble et al. (2010), *Continuous Delivery*** — separar despliegue de activación y lanzamiento a oscuras<br>  ↳ libro · [ISBN 9780321670250](https://openlibrary.org/isbn/9780321670250) ✅
- **OpenFeature (2025), *Specification: evaluation, context and providers*** — evaluación local, contexto y valores por defecto<br>  ↳ documentación · [openfeature.dev](https://openfeature.dev/specification) ✅
- **Kohavi et al. (2020), *Trustworthy Online Controlled Experiments*** — asignación estable y validez de los experimentos<br>  ↳ documentación · [experimentguide.com](https://experimentguide.com) ✅
- **Google SRE (2025), *Graceful degradation*** — apagar y degradar como respuesta operativa durante un incidente<br>  ↳ documentación · [sre.google](https://sre.google/workbook/managing-load) ✅

## [106 — Platform engineering e Internal Developer Platform](../../classes/part-08-continuous-delivery-platform-engineering/106-platform-engineering-e-internal-developer-platform/README.md)

- **Skelton et al. (2019), *Team Topologies*** — equipo de plataforma y su relación con los equipos de producto<br>  ↳ documentación · [teamtopologies.com](https://teamtopologies.com/book) ✅
- **CNCF (2025), *Platforms white paper*** — plataforma como producto, capacidades e interfaces<br>  ↳ documentación · [tag-app-delivery.cncf.io](https://tag-app-delivery.cncf.io/whitepapers/platforms) ✅
- **Thoughtworks (2025), *Platform as a product and the paved road*** — camino asfaltado, salida y medición de adopción<br>  ↳ documentación · [thoughtworks.com](https://thoughtworks.com/insights/blog/platforms) ✅
- **Backstage (2025), *Software catalog and scaffolder*** — catálogo, plantillas y autoservicio<br>  ↳ documentación · [backstage.io](https://backstage.io/docs/features/software-catalog) ✅
- **Google (2025), *Internal developer platforms and golden paths*** — estandarizar lo que no diferencia<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/devops) ✅

## [107 — Developer experience, DORA y carga cognitiva](../../classes/part-08-continuous-delivery-platform-engineering/107-developer-experience-dora-y-carga-cognitiva/README.md)

- **Forsgren et al. (2018), *Accelerate*** — definición de las cuatro medidas y su relación<br>  ↳ libro · [ISBN 9781942788379](https://openlibrary.org/isbn/9781942788379) ✅
- **DORA (2025), *State of DevOps report*** — evolución de las medidas y advertencias sobre su uso<br>  ↳ documentación · [dora.dev](https://dora.dev/research) ✅
- **Forsgren et al. (2021), *The SPACE of developer productivity*** — por qué una sola dimensión no basta<br>  ↳ documentación · [queue.acm.org](https://queue.acm.org/detail.cfm?id=3454124) ✅
- **Google (2025), *Engineering productivity research: flaky tests*** — coste de la inestabilidad sobre la confianza en las puertas<br>  ↳ documentación · [testing.googleblog.com](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) ✅
- **Strathern (1997), *Improving ratings: audit in the British university system*** — formulación de la ley de Goodhart aplicada a indicadores<br>  ↳ artículo · [doi:10.1111/1468-0009.00035](https://doi.org/10.1111/1468-0009.00035) ✅

## [108 — Proyecto: fábrica de software multi-cloud](../../classes/part-08-continuous-delivery-platform-engineering/108-proyecto-fabrica-de-software-multi-cloud/README.md)

- **Forsgren et al. (2018), *Accelerate*** — capacidades de entrega y su efecto conjunto<br>  ↳ libro · [ISBN 9781942788379](https://openlibrary.org/isbn/9781942788379) ✅
- **CNCF (2025), *Platforms white paper*** — la fábrica como producto interno y sus interfaces<br>  ↳ documentación · [tag-app-delivery.cncf.io](https://tag-app-delivery.cncf.io/whitepapers/platforms) ✅
- **SLSA (2025), *Levels and requirements*** — qué exige cada nivel de la cadena de construcción<br>  ↳ documentación · [slsa.dev](https://slsa.dev/spec/v1.0/levels) ✅
- **OpenGitOps (2025), *Principles*** — reconciliación continua como base del recorrido<br>  ↳ documentación · [opengitops.dev](https://opengitops.dev) ✅
- **Kim et al. (2016), *The DevOps Handbook*** — flujo, retroalimentación y aprendizaje continuo<br>  ↳ documentación · [itrevolution.com](https://itrevolution.com/product/the-devops-handbook-second-edition) ✅
