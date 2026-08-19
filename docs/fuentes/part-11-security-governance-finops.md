# Fuentes de la Parte 11 — Seguridad, gobierno, cumplimiento y FinOps

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-11-security-governance-finops/README.md)

## [133 — Zero Trust y defensa en profundidad](../../classes/part-11-security-governance-finops/133-zero-trust-y-defensa-en-profundidad/README.md)

- **NIST (2020), *SP 800-207: Zero Trust Architecture*** — principios, componentes y modelos de despliegue<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/207/final) ✅
- **Google (2025), *BeyondCorp: a new approach to enterprise security*** — acceso sin confianza en la red<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/beyondcorp) ✅
- **CISA (2025), *Zero Trust Maturity Model*** — orden de adopción por pilares<br>  ↳ documentación · [cisa.gov](https://www.cisa.gov/zero-trust-maturity-model) ⏳
- **MITRE (2025), *ATT&CK: lateral movement*** — técnicas reales de avance dentro de una red<br>  ↳ documentación · [attack.mitre.org](https://attack.mitre.org/tactics/TA0008) ✅
- **AWS (2025), *Security pillar: apply security at all layers*** — independencia de capas y separación por cuentas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) ✅

## [134 — Mínimo privilegio, acceso temporal y separación de funciones](../../classes/part-11-security-governance-finops/134-minimo-privilegio-acceso-temporal-y-separacion-de-funciones/README.md)

- **AWS (2025), *IAM Access Analyzer: policy generation from access activity*** — deducir permisos del uso registrado<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) ✅
- **Microsoft (2025), *Privileged Identity Management: just-in-time access*** — concesión temporal, aprobación y caducidad<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-configure) ✅
- **Google Cloud (2025), *Policy Intelligence and recommender*** — permisos concedidos y no usados<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/policy-intelligence/docs/role-recommendations-overview) ✅
- **NIST (2020), *SP 800-53: AC-5 separation of duties, AC-6 least privilege*** — definición y controles compensatorios<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) ✅
- **AWS (2025), *Permissions boundaries*** — techo que ninguna concesión delegada puede superar<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) ✅

## [135 — Segmentación, perímetro, WAF, DDoS y egress](../../classes/part-11-security-governance-finops/135-segmentacion-perimetro-waf-ddos-y-egress/README.md)

- **NIST (2016), *SP 800-125B / segmentación y microsegmentación*** — unidades de aislamiento y su aplicación<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/125/b/final) ✅
- **Kubernetes (2025), *Network policies*** — denegación por defecto y autorización entre cargas<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies) ✅
- **AWS (2025), *VPC endpoints and endpoint policies*** — acceso privado y restricción a cuentas propias<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) ✅
- **OWASP (2025), *Web application firewall: benefits and limitations*** — qué filtra y qué no<br>  ↳ documentación · [owasp.org](https://owasp.org/www-community/Web_Application_Firewall) ✅
- **Cloudflare (2025), *DDoS: volumetric and application-layer attacks*** — diferencias y defensas aplicables<br>  ↳ documentación · [developers.cloudflare.com](https://developers.cloudflare.com/ddos-protection) ✅

## [136 — Cifrado, KMS, HSM, rotación y envelope encryption](../../classes/part-11-security-governance-finops/136-cifrado-kms-hsm-rotacion-y-envelope-encryption/README.md)

- **AWS (2025), *KMS: envelope encryption and data key caching*** — mecanismo, límites y caché<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) ✅
- **Google Cloud (2025), *Cloud KMS: key rotation and key destruction*** — qué implica rotar y el periodo de espera al destruir<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kms/docs/key-rotation) ✅
- **Azure (2025), *Key Vault: keys, secrets and access policies*** — separación entre uso y administración<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/key-vault/general/security-features) ✅
- **NIST (2020), *SP 800-57: key management recommendations*** — periodos de uso, rotación y custodia<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) ✅
- **OWASP (2025), *Transport layer security cheat sheet*** — cifrado interno y validación de certificados<br>  ↳ documentación · [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html) ✅

## [137 — Gestión de secretos y credenciales de workloads](../../classes/part-11-security-governance-finops/137-gestion-de-secretos-y-credenciales-de-workloads/README.md)

- **HashiCorp Vault (2025), *Dynamic secrets and database secrets engine*** — credenciales creadas al usar, con caducidad<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/vault/docs/secrets/databases) ✅
- **AWS (2025), *Secrets Manager rotation strategies*** — ventana de dos credenciales y verificación<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) ✅
- **Kubernetes (2025), *Secrets: risks and mounted volumes*** — entrega por fichero frente a variable de entorno<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/configuration/secret) ✅
- **SPIFFE (2025), *Workload identity and the bootstrap problem*** — cómo demuestra una carga quién es sin un secreto previo<br>  ↳ documentación · [spiffe.io](https://spiffe.io/docs/latest/spiffe-about/overview) ✅
- **OWASP (2025), *Secrets management cheat sheet*** — inventario, entrega, rotación y respuesta a filtraciones<br>  ↳ documentación · [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) ✅

## [138 — Vulnerabilidades, imágenes y cadena de suministro](../../classes/part-11-security-governance-finops/138-vulnerabilidades-imagenes-y-cadena-de-suministro/README.md)

- **CISA (2025), *Known Exploited Vulnerabilities catalog*** — priorizar por explotación real observada<br>  ↳ documentación · [cisa.gov](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) ⏳
- **FIRST (2025), *EPSS: exploit prediction scoring system*** — probabilidad de explotación frente a gravedad<br>  ↳ documentación · [first.org](https://first.org/epss) ✅
- **Birsan (2021), *Dependency confusion*** — descripción del ataque y su prevención<br>  ↳ documentación · [medium.com](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) ✅
- **OpenSSF (2025), *Supply chain best practices: pinning, allow-listing and internal mirrors*** — controles sobre lo que se instala<br>  ↳ documentación · [best.openssf.org](https://best.openssf.org) ✅
- **Google (2025), *Distroless container images*** — imágenes mínimas y su efecto en el recuento de hallazgos<br>  ↳ documentación · [github.com](https://github.com/GoogleContainerTools/distroless) ✅

## [139 — CSPM, postura, policy as code y remediación](../../classes/part-11-security-governance-finops/139-cspm-postura-policy-as-code-y-remediacion/README.md)

- **AWS (2025), *Service control policies and organization-level guardrails*** — controles preventivos que no se rodean<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) ✅
- **Google Cloud (2025), *Organization policy constraints*** — restricciones aplicadas a toda la jerarquía<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/resource-manager/docs/organization-policy/overview) ✅
- **Azure (2025), *Azure Policy: effects, exemptions and remediation tasks*** — detección, excepciones y corrección<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/governance/policy/concepts/effects) ✅
- **Open Policy Agent (2025), *Policy testing*** — pruebas de reglas como código<br>  ↳ documentación · [openpolicyagent.org](https://openpolicyagent.org/docs/latest/policy-testing) ✅
- **CIS (2025), *Benchmarks for cloud providers*** — catálogos de reglas de configuración por defecto<br>  ↳ documentación · [cisecurity.org](https://cisecurity.org/cis-benchmarks) ✅

## [140 — Threat modeling con STRIDE y attack paths](../../classes/part-11-security-governance-finops/140-threat-modeling-con-stride-y-attack-paths/README.md)

- **Shostack (2014), *Threat Modeling: Designing for Security*** — las cuatro preguntas y la aplicación de la lista por elemento<br>  ↳ libro · [ISBN 9781306427067](https://openlibrary.org/isbn/9781306427067) ✅
- **Microsoft (2025), *STRIDE threat categories*** — definición de las seis categorías y su uso<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/security/develop/threat-modeling-tool-threats) ✅
- **OWASP (2025), *Threat modeling process*** — alcance, dinámica de la sesión y resultados accionables<br>  ↳ documentación · [owasp.org](https://owasp.org/www-community/Threat_Modeling_Process) ✅
- **MITRE (2025), *ATT&CK: tactics and techniques*** — pasos reales de una cadena de ataque<br>  ↳ documentación · [attack.mitre.org](https://attack.mitre.org) ✅
- **Threat Modeling Manifesto (2025), *Values and principles*** — por qué el resultado importa más que el documento<br>  ↳ documentación · [threatmodelingmanifesto.org](https://threatmodelingmanifesto.org) ✅

## [141 — Cumplimiento, residencia, privacidad y evidencia](../../classes/part-11-security-governance-finops/141-cumplimiento-residencia-privacidad-y-evidencia/README.md)

- **Unión Europea (2016), *Reglamento general de protección de datos*** — bases de tratamiento, minimización y derechos<br>  ↳ documentación · [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj) ✅
- **NIST (2020), *Privacy Framework*** — clasificación, minimización y controles de privacidad<br>  ↳ documentación · [nist.gov](https://nist.gov/privacy-framework) ✅
- **ISO/IEC (2022), *27001 e 27701: requisitos y evidencia*** — qué se audita y cómo se demuestra<br>  ↳ norma · [iso.org](https://www.iso.org/standard/27001) ⏳
- **Google Cloud (2025), *Data residency and sovereignty controls*** — límites reales, metadatos y plano de control<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework/security/data-residency-sovereignty) ✅
- **ENISA (2025), *Crypto-shredding and data deletion in immutable systems*** — borrado criptográfico y sus límites<br>  ↳ documentación · [enisa.europa.eu](https://enisa.europa.eu/publications) ✅

## [142 — FinOps: showback, chargeback, budgets y anomalías](../../classes/part-11-security-governance-finops/142-finops-showback-chargeback-budgets-y-anomalias/README.md)

- **FinOps Foundation (2025), *FinOps framework: capabilities*** — atribución, visibilidad, optimización y gobierno<br>  ↳ documentación · [finops.org](https://finops.org/framework) ✅
- **FinOps Foundation (2025), *Unit economics*** — coste por unidad de negocio como medida comparable<br>  ↳ documentación · [finops.org](https://finops.org/framework/capabilities/unit-economics) ✅
- **AWS (2025), *Cost allocation tags and cost anomaly detection*** — atribución y detección de desviaciones<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) ✅
- **Google Cloud (2025), *Billing budgets, forecasts and alerts*** — aviso por previsión frente a aviso por límite<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/billing/docs/how-to/budgets) ✅
- **Azure (2025), *Cost Management: showback and chargeback*** — mostrar frente a cobrar y sus efectos<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/cost-management-billing/finops) ✅

## [143 — Optimización de costo, capacidad y sostenibilidad](../../classes/part-11-security-governance-finops/143-optimizacion-de-costo-capacidad-y-sostenibilidad/README.md)

- **FinOps Foundation (2025), *Rate and usage optimization*** — escalera de optimización y orden de aplicación<br>  ↳ documentación · [finops.org](https://finops.org/framework/capabilities) ✅
- **AWS (2025), *Savings Plans, Reserved Instances and Spot best practices*** — instrumentos y su combinación por capas<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models) ✅
- **Google Cloud (2025), *Committed use discounts and Spot VMs*** — compromisos y capacidad interrumpible<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/compute/docs/instances/spot) ✅
- **Green Software Foundation (2025), *Software carbon intensity specification*** — intensidad por región y por hora<br>  ↳ documentación · [sci.greensoftware.foundation](https://sci.greensoftware.foundation) ✅
- **Microsoft (2025), *Sustainability in the cloud: emissions reporting caveats*** — límites de comparabilidad de las cifras<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/architecture/framework/sustainability) ✅

## [144 — Proyecto: landing zone con guardrails](../../classes/part-11-security-governance-finops/144-proyecto-landing-zone-con-guardrails/README.md)

- **AWS (2025), *Organizing your environment using multiple accounts*** — estructura, controles y cuentas de servicio<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment) ✅
- **Google Cloud (2025), *Landing zone design*** — jerarquía, identidad, red y controles de la organización<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/landing-zones) ✅
- **Microsoft (2025), *Cloud Adoption Framework: landing zones*** — áreas de diseño y su orden<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone) ✅
- **CIS (2025), *Foundations benchmarks*** — controles mínimos de una base de nube<br>  ↳ documentación · [cisecurity.org](https://cisecurity.org/cis-benchmarks) ✅
- **FinOps Foundation (2025), *Account and tagging strategy*** — atribución impuesta desde la estructura<br>  ↳ documentación · [finops.org](https://finops.org/framework/capabilities/allocation) ✅
