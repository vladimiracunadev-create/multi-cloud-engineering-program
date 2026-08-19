# Fuentes de la Parte 07 — Infraestructura como código y configuración

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-07-infrastructure-as-code-configuration/README.md)

## [085 — Declarativo, imperativo, idempotencia y convergencia](../../classes/part-07-infrastructure-as-code-configuration/085-declarativo-imperativo-idempotencia-y-convergencia/README.md)

- **Kief Morris (2020), *Infrastructure as Code*** — principios, idempotencia y convergencia<br>  ↳ documentación · [infrastructure-as-code.com](https://infrastructure-as-code.com/book) ✅
- **Mark Burgess (2004), *Promise Theory and convergent operators*** — origen del concepto de convergencia en configuración<br>  ↳ documentación · [markburgess.org](https://markburgess.org/promises.html) ✅
- **HashiCorp (2025), *Drift detection and reconciliation*** — orígenes de la desviación y respuestas<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift) ✅
- **Kubernetes (2025), *Controllers and the reconciliation loop*** — el bucle como mecanismo de convergencia<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/architecture/controller) ✅
- **Bill Baker (2012), *Scaling SQL Server: pets vs cattle*** — origen de la distinción y su uso operativo<br>  ↳ documentación · [cloudscaling.com](https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle) ✅

## [086 — Terraform: HCL, providers, resources y grafo](../../classes/part-07-infrastructure-as-code-configuration/086-terraform-hcl-providers-resources-y-grafo/README.md)

- **HashiCorp (2025), *Resource behavior and the dependency graph*** — dependencias implícitas y explícitas<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/resources/behavior) ✅
- **HashiCorp (2025), *The lifecycle meta-argument*** — crear antes de destruir, ignorar cambios y protecciones<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle) ✅
- **HashiCorp (2025), *Provider configuration and aliases*** — varias configuraciones del mismo proveedor<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/providers/configuration) ✅
- **HashiCorp (2025), *Provider requirements and dependency lock file*** — fijar versiones y plataformas<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/files/dependency-lock) ✅
- **HashiCorp (2025), *Provisioners are a last resort*** — por qué evitarlos y qué usar en su lugar<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax) ✅

## [087 — Estado remoto, locking, cifrado y recuperación](../../classes/part-07-infrastructure-as-code-configuration/087-estado-remoto-locking-cifrado-y-recuperacion/README.md)

- **HashiCorp (2025), *State: purpose and remote backends*** — por qué existe y cómo se guarda<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state) ✅
- **HashiCorp (2025), *State locking*** — bloqueo, tiempos de espera y liberación forzada<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state/locking) ✅
- **HashiCorp (2025), *Import blocks and configuration generation*** — importar declarativamente y generar la configuración<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/import) ✅
- **HashiCorp (2025), *The moved block*** — refactorizar sin destruir ni recrear<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/moved) ✅
- **HashiCorp (2025), *Manipulating state with the CLI*** — listar, mostrar, mover y retirar recursos<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/cli/state) ✅

## [088 — Módulos, contratos, versiones y composición](../../classes/part-07-infrastructure-as-code-configuration/088-modulos-contratos-versiones-y-composicion/README.md)

- **HashiCorp (2025), *Module composition*** — profundidad, proveedores y patrones de composición<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/modules/develop/composition) ✅
- **HashiCorp (2025), *Module sources and versions*** — orígenes, revisiones y restricciones de versión<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/modules/sources) ✅
- **HashiCorp (2025), *Variable validation and custom conditions*** — validación en la planificación<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions) ✅
- **HashiCorp (2025), *Terraform test framework*** — pruebas que aplican y destruyen, y fallos esperados<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/tests) ✅
- **HashiCorp (2025), *Standard module structure*** — ejemplos, documentación y organización esperada<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/modules/develop/structure) ✅

## [089 — Variables, outputs, locals y data sources](../../classes/part-07-infrastructure-as-code-configuration/089-variables-outputs-locals-y-data-sources/README.md)

- **HashiCorp (2025), *Input variables and variable definition precedence*** — orden de las fuentes y carga automática<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/values/variables) ✅
- **HashiCorp (2025), *Optional object type attributes*** — campos opcionales con valores por defecto<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/expressions/type-constraints) ✅
- **HashiCorp (2025), *Checks and custom conditions*** — comprobaciones que no bloquean y aserciones<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/checks) ✅
- **HashiCorp (2025), *Output values and sensitive data*** — salidas, sensibilidad y su presencia en el estado<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/values/outputs) ✅
- **HashiCorp (2025), *Default tags in the AWS provider*** — etiquetado uniforme y su interacción con etiquetas locales<br>  ↳ documentación · [registry.terraform.io](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) ✅

## [090 — Plan, apply, drift, import y refactor con moved](../../classes/part-07-infrastructure-as-code-configuration/090-plan-apply-drift-import-y-refactor-con-moved/README.md)

- **HashiCorp (2025), *The core Terraform workflow*** — refresco, plan y aplicación<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/intro/core-workflow) ✅
- **HashiCorp (2025), *Managing resource drift*** — detección, refresco y aceptación de cambios externos<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift) ✅
- **HashiCorp (2025), *Command: plan and machine-readable output*** — códigos de salida y formato estructurado<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/cli/commands/plan) ✅
- **HashiCorp (2025), *Resource targeting*** — por qué es una operación excepcional<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/cli/commands/plan) ✅
- **HashiCorp (2025), *The removed block*** — dejar de gestionar un recurso sin destruirlo<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/resources/syntax) ✅

## [091 — Validación, lint, pruebas y policy as code](../../classes/part-07-infrastructure-as-code-configuration/091-validacion-lint-pruebas-y-policy-as-code/README.md)

- **Open Policy Agent (2025), *Terraform plan testing with Conftest*** — reglas contra el plan en formato estructurado<br>  ↳ documentación · [openpolicyagent.org](https://openpolicyagent.org/docs/latest/terraform) ✅
- **HashiCorp (2025), *Terraform JSON output format*** — estructura del plan para automatización<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/internals/json-format) ✅
- **TFLint (2025), *Rules and provider plugins*** — errores de proveedor y argumentos obsoletos<br>  ↳ documentación · [github.com](https://github.com/terraform-linters/tflint) ✅
- **HashiCorp (2025), *Terraform test framework*** — pruebas con creación real y fallos esperados<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/tests) ✅
- **Infracost (2025), *Cost estimation in pull requests*** — estimación sobre el plan y umbrales<br>  ↳ documentación · [infracost.io](https://infracost.io/docs) ✅

## [092 — Secretos y datos sensibles en IaC](../../classes/part-07-infrastructure-as-code-configuration/092-secretos-y-datos-sensibles-en-iac/README.md)

- **HashiCorp (2025), *Sensitive data in state*** — por qué el estado guarda los valores y cómo protegerlo<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state/sensitive-data) ✅
- **HashiCorp (2025), *Ephemeral values and write-only arguments*** — valores que no se guardan en el estado<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/manage-sensitive-data/ephemeral) ✅
- **AWS (2025), *Managed master user password for RDS*** — credencial generada y rotada por el servicio<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) ✅
- **Gitleaks (2025), *Scanning git history for secrets*** — detección en el historial, no solo en el árbol actual<br>  ↳ documentación · [github.com](https://github.com/gitleaks/gitleaks) ✅
- **Mozilla (2025), *SOPS: encrypted files in the repository*** — cifrado de valores y gestión de la clave<br>  ↳ documentación · [github.com](https://github.com/getsops/sops) ✅

## [093 — CloudFormation, Bicep, Pulumi y Terraform](../../classes/part-07-infrastructure-as-code-configuration/093-cloudformation-bicep-pulumi-y-terraform/README.md)

- **AWS (2025), *CloudFormation stack failure options and rollback*** — comportamiento ante fallo parcial<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-failure-options.html) ✅
- **Microsoft (2025), *Bicep vs ARM templates and deployment behaviour*** — motor gestionado y modos de despliegue<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) ✅
- **HashiCorp (2025), *Terraform: no partial rollback*** — por qué las plantillas deben ser reejecutables<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/resources/behavior) ✅
- **Pulumi (2025), *Programming model and preview*** — lenguajes generales con previsualización del cambio<br>  ↳ documentación · [pulumi.com](https://pulumi.com/docs/concepts) ✅
- **AWS (2025), *CDK: synthesized templates*** — generar plantillas nativas desde un lenguaje general<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/cdk/v2/guide/home.html) ✅

## [094 — Ansible e imagen dorada para configuración](../../classes/part-07-infrastructure-as-code-configuration/094-ansible-e-imagen-dorada-para-configuracion/README.md)

- **HashiCorp (2025), *Packer: building machine images*** — construcción, aprovisionadores y publicación<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/packer/docs) ✅
- **Ansible (2025), *Desired state and idempotency*** — idempotencia por módulo y condiciones de omisión<br>  ↳ documentación · [docs.ansible.com](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html) ✅
- **Ansible (2025), *Check mode and diff mode*** — simulación de cambios y sus límites<br>  ↳ documentación · [docs.ansible.com](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html) ⏳
- **Ansible (2025), *Variable precedence*** — los más de veinte niveles y su orden<br>  ↳ documentación · [docs.ansible.com](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable) ⏳
- **Ansible (2025), *Rolling update strategies*** — ejecución por tandas y detención ante fallo<br>  ↳ documentación · [docs.ansible.com](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_strategies.html) ⏳

## [095 — Plantillas, golden paths y catálogo interno](../../classes/part-07-infrastructure-as-code-configuration/095-plantillas-golden-paths-y-catalogo-interno/README.md)

- **Evan Bottcher (2018), *What I talk about when I talk about platforms*** — la plataforma como producto y el camino asfaltado<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/articles/talk-about-platforms.html) ✅
- **Matthew Skelton (2019), *Team Topologies*** — equipos de plataforma y modos de interacción<br>  ↳ documentación · [teamtopologies.com](https://teamtopologies.com/book) ✅
- **Backstage (2025), *Software catalog and scaffolder*** — catálogo de servicios, propiedad y plantillas<br>  ↳ documentación · [backstage.io](https://backstage.io/docs/features/software-catalog) ✅
- **Google (2023), *DORA: platform engineering and developer experience*** — métricas de adopción y de tiempo de entrega<br>  ↳ documentación · [dora.dev](https://dora.dev/research) ✅
- **CNCF (2025), *Platforms White Paper*** — capacidades esperadas de una plataforma interna y sus señales<br>  ↳ documentación · [tag-app-delivery.cncf.io](https://tag-app-delivery.cncf.io/whitepapers/platforms) ✅

## [096 — Proyecto: infraestructura multiambiente promovible](../../classes/part-07-infrastructure-as-code-configuration/096-proyecto-infraestructura-multiambiente-promovible/README.md)

- **Kief Morris (2020), *Infrastructure as Code*** — entornos, promoción y organización del código<br>  ↳ documentación · [infrastructure-as-code.com](https://infrastructure-as-code.com/book) ✅
- **HashiCorp (2025), *Recommended practices for Terraform in production*** — estados, entornos y flujo de trabajo<br>  ↳ documentación · [developer.hashicorp.com](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) ✅
- **Google (2023), *DORA: change failure rate and lead time*** — métricas de entrega aplicadas a infraestructura<br>  ↳ documentación · [dora.dev](https://dora.dev/research) ✅
- **Nicole Forsgren et al (2018), *Accelerate*** — efecto de la visibilidad sobre el comportamiento del equipo<br>  ↳ documentación · [itrevolution.com](https://itrevolution.com/product/accelerate) ✅
- **OWASP (2025), *Infrastructure as Code security cheat sheet*** — controles y su coste de adopción<br>  ↳ documentación · [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html) ✅
