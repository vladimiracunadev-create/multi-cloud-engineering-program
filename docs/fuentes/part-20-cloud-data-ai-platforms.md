# Fuentes de la Parte 20 — Plataformas cloud de datos, analítica, IA y agentes

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-20-cloud-data-ai-platforms/README.md)

## [241 — Lakehouse, warehouse, mesh y contratos de datos](../../classes/part-20-cloud-data-ai-platforms/241-lakehouse-warehouse-mesh-y-contratos-de-datos/README.md)

- **Dehghani (2022), *Data Mesh: Delivering Data-Driven Value at Scale*** — la propuesta de malla de datos y sus cuatro principios<br>  ↳ libro · [ISBN 9788426735546](https://openlibrary.org/isbn/9788426735546) ✅
- **Armbrust et al. (2021), *Lakehouse: a new generation of open platforms*** — la arquitectura que une lago y almacén<br>  ↳ documentación · [cidrdb.org](https://cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) ✅
- **Delta Lake (2025), *Table format and transaction log*** — formato de tabla y registro de transacciones<br>  ↳ documentación · [docs.delta.io](https://docs.delta.io/latest/index.html) ✅
- **Apache Iceberg (2025), *Table specification*** — la especificación del formato de tabla abierto<br>  ↳ documentación · [iceberg.apache.org](https://iceberg.apache.org/spec) ✅
- ***Open Data Contract Standard (2025)*** — el estándar de contrato de datos entre productor y consumidor<br>  ↳ documentación · [bitol-io.github.io](https://bitol-io.github.io/open-data-contract-standard/latest) ✅

## [242 — Ingesta batch, CDC y streaming](../../classes/part-20-cloud-data-ai-platforms/242-ingesta-batch-cdc-y-streaming/README.md)

- **Kleppmann (2017), *Designing Data-Intensive Applications*** — flujos y captura de cambios<br>  ↳ libro · [ISBN 9781491903117](https://openlibrary.org/isbn/9781491903117) ✅
- **Debezium (2025), *Change data capture connectors*** — conectores de captura de cambios<br>  ↳ documentación · [debezium.io](https://debezium.io/documentation/reference/stable/index.html) ✅
- **Apache Beam (2025), *Streaming model: windows, watermarks and triggers*** — ventanas, marcas de agua y disparadores<br>  ↳ documentación · [beam.apache.org](https://beam.apache.org/documentation/programming-guide) ✅
- **Akidau et al. (2015), *The Dataflow Model*** — el modelo formal que unifica lote y flujo<br>  ↳ documentación · [research.google](https://research.google/pubs/pub43864) ✅
- **Google Cloud (2025), *Datastream: serverless change data capture*** — captura de cambios gestionada y sin servidor<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/datastream/docs/overview) ✅

## [243 — Orquestación, calidad, lineage y observabilidad de datos](../../classes/part-20-cloud-data-ai-platforms/243-orquestacion-calidad-lineage-y-observabilidad-de-datos/README.md)

- **Apache Airflow (2025), *Concepts: DAGs, data-aware scheduling and backfills*** — grafos de tareas, planificación por datos y reprocesos<br>  ↳ documentación · [airflow.apache.org](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html) ✅
- **Great Expectations (2025), *Data quality expectations*** — expectativas declarativas de calidad del dato<br>  ↳ documentación · [docs.greatexpectations.io](https://docs.greatexpectations.io) ✅
- **Moses et al. (2022), *Data Quality Fundamentals*** — dimensiones de calidad y detección de incidentes de datos<br>  ↳ libro · [ISBN 9781098112042](https://openlibrary.org/isbn/9781098112042) ✅
- **OpenLineage (2025), *Lineage specification*** — el estándar abierto para registrar linaje<br>  ↳ documentación · [openlineage.io](https://openlineage.io/docs) ✅
- **dbt (2025), *Tests, contracts and lineage*** — pruebas y contratos ejecutados junto a la transformación<br>  ↳ documentación · [docs.getdbt.com](https://docs.getdbt.com/docs/build/data-tests) ✅

## [244 — Feature stores, training pipelines y experiment tracking](../../classes/part-20-cloud-data-ai-platforms/244-feature-stores-training-pipelines-y-experiment-tracking/README.md)

- **Sculley et al. (2015), *Hidden technical debt in machine learning systems*** — por qué el código del modelo es la parte pequeña del sistema<br>  ↳ documentación · [papers.nips.cc](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) ✅
- **Feast (2025), *Feature store concepts and point-in-time joins*** — unión temporal correcta para no filtrar el futuro<br>  ↳ documentación · [docs.feast.dev](https://docs.feast.dev) ✅
- **Kapoor et al. (2023), *Leakage and the reproducibility crisis in ML-based science*** — la fuga de datos como causa de resultados irreproducibles<br>  ↳ documentación · [cell.com](https://www.cell.com/patterns/fulltext/S2666-3899(23)00159-9) ⏳
- **MLflow (2025), *Tracking experiments and model registry*** — seguimiento de experimentos y registro de modelos<br>  ↳ documentación · [mlflow.org](https://mlflow.org/docs/latest/tracking.html) ✅
- **Gebru et al. (2021), *Datasheets for datasets*** — documentar el origen y los sesgos del conjunto de datos<br>  ↳ artículo · [doi:10.1145/3458723](https://doi.org/10.1145/3458723) ✅

## [245 — Serving online, batch inference y escalado de modelos](../../classes/part-20-cloud-data-ai-platforms/245-serving-online-batch-inference-y-escalado-de-modelos/README.md)

- **NVIDIA (2025), *Triton Inference Server: dynamic batching and model concurrency*** — agrupación dinámica y concurrencia de modelos<br>  ↳ documentación · [docs.nvidia.com](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html) ✅
- **Google (2025), *Vertex AI: online and batch prediction*** — predicción en línea frente a predicción por lotes<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vertex-ai/docs/predictions/overview) ✅
- **Huyen (2022), *Designing Machine Learning Systems*** — diseño del sistema alrededor del modelo<br>  ↳ libro · [ISBN 9781098107963](https://openlibrary.org/isbn/9781098107963) ✅
- **Kohavi et al. (2020), *Trustworthy Online Controlled Experiments*** — diseño y lectura de experimentos controlados en línea<br>  ↳ documentación · [experimentguide.com](https://experimentguide.com) ✅
- **Covington et al. (2016), *Deep neural networks for YouTube recommendations*** — recuperación y ordenamiento<br>  ↳ documentación · [research.google](https://research.google/pubs/pub45530) ✅

## [246 — MLOps, registro, promoción, drift y rollback](../../classes/part-20-cloud-data-ai-platforms/246-mlops-registro-promocion-drift-y-rollback/README.md)

- **Sculley et al. (2015), *Hidden technical debt in machine learning systems*** — la deuda oculta que arrastra un sistema de aprendizaje<br>  ↳ documentación · [papers.nips.cc](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) ✅
- **Huyen (2022), *Designing Machine Learning Systems*** — data distribution shifts<br>  ↳ libro · [ISBN 9781098107963](https://openlibrary.org/isbn/9781098107963) ✅
- **Google (2025), *MLOps: continuous delivery and automation pipelines*** — los niveles de automatización de la entrega de modelos<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) ✅
- **MLflow (2025), *Model registry and stages*** — registro de modelos y promoción entre etapas<br>  ↳ documentación · [mlflow.org](https://mlflow.org/docs/latest/model-registry.html) ✅
- **Breck et al. (2017), *The ML test score: a rubric for ML production readiness*** — rúbrica de preparación para producción<br>  ↳ documentación · [research.google](https://research.google/pubs/pub46555) ✅

## [247 — Modelos fundacionales, tokens, embeddings y RAG](../../classes/part-20-cloud-data-ai-platforms/247-modelos-fundacionales-tokens-embeddings-y-rag/README.md)

- **Lewis et al. (2020), *Retrieval-augmented generation for knowledge-intensive NLP tasks*** — el mecanismo de recuperación aumentada y sus límites<br>  ↳ artículo · [doi:10.48550/arXiv.2005.11401](https://doi.org/10.48550/arXiv.2005.11401) ✅
- **Liu et al. (2023), *Lost in the middle: how language models use long contexts*** — por qué la posición dentro del contexto cambia el resultado<br>  ↳ artículo · [doi:10.48550/arXiv.2307.03172](https://doi.org/10.48550/arXiv.2307.03172) ✅
- **Malkov et al. (2018), *Efficient and robust approximate nearest neighbor search (HNSW)*** — búsqueda aproximada de vecinos para el índice vectorial<br>  ↳ artículo · [doi:10.48550/arXiv.1603.09320](https://doi.org/10.48550/arXiv.1603.09320) ✅
- **Karpukhin et al. (2020), *Dense passage retrieval for open-domain question answering*** — recuperación densa frente a recuperación léxica<br>  ↳ artículo · [doi:10.48550/arXiv.2004.04906](https://doi.org/10.48550/arXiv.2004.04906) ✅
- **Anthropic (2025), *Prompt engineering and long context tips*** — prácticas de construcción de la instrucción y del contexto<br>  ↳ documentación · [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) ✅

## [248 — Bedrock, Azure AI Foundry y Vertex AI](../../classes/part-20-cloud-data-ai-platforms/248-bedrock-azure-ai-foundry-y-vertex-ai/README.md)

- **AWS (2025), *Amazon Bedrock: data protection and model versions*** — protección de los datos y versiones del modelo<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) ✅
- **Microsoft (2025), *Azure AI Foundry: data privacy and model lifecycle*** — privacidad de los datos y ciclo de vida del modelo<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry) ✅
- **Google Cloud (2025), *Vertex AI: generative AI data governance and model versions*** — gobierno del dato y versiones del modelo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance) ✅
- **Anthropic (2025), *Claude API: models, versions and deprecations*** — versiones publicadas y política de retirada<br>  ↳ documentación · [docs.anthropic.com](https://docs.anthropic.com/en/docs/about-claude/models/overview) ✅
- **NIST (2024), *AI Risk Management Framework: Generative AI profile*** — el perfil de riesgo específico de la IA generativa<br>  ↳ documentación · [nist.gov](https://nist.gov/itl/ai-risk-management-framework) ✅

## [249 — Agentes, tools, memoria, permisos y guardrails](../../classes/part-20-cloud-data-ai-platforms/249-agentes-tools-memoria-permisos-y-guardrails/README.md)

- **OWASP (2025), *Top 10 for LLM applications: prompt injection and excessive agency*** — inyección de instrucciones y agencia excesiva<br>  ↳ documentación · [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications) ✅
- **Greshake et al. (2023), *Not what you've signed up for: indirect prompt injection*** — la inyección indirecta a través del contenido consultado<br>  ↳ artículo · [doi:10.48550/arXiv.2302.12173](https://doi.org/10.48550/arXiv.2302.12173) ✅
- **Anthropic (2025), *Tool use with Claude*** — el contrato de uso de herramientas por el agente<br>  ↳ documentación · [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) ✅
- **NIST (2024), *AI RMF Generative AI profile: risks of agentic systems*** — riesgos propios de los sistemas con agencia<br>  ↳ documentación · [nist.gov](https://nist.gov/itl/ai-risk-management-framework) ✅
- **Model Context Protocol (2025), *Specification: tools, resources and security*** — el protocolo de herramientas y sus consideraciones de seguridad<br>  ↳ documentación · [modelcontextprotocol.io](https://modelcontextprotocol.io) ✅

## [250 — Evaluación de IA, red teaming y observabilidad](../../classes/part-20-cloud-data-ai-platforms/250-evaluacion-de-ia-red-teaming-y-observabilidad/README.md)

- **Zheng et al. (2023), *Judging LLM-as-a-judge with MT-Bench and Chatbot Arena*** — usar un modelo como juez y sus sesgos conocidos<br>  ↳ artículo · [doi:10.48550/arXiv.2306.05685](https://doi.org/10.48550/arXiv.2306.05685) ✅
- **Es et al. (2023), *RAGAS: automated evaluation of retrieval augmented generation*** — métricas automáticas de calidad de la recuperación<br>  ↳ artículo · [doi:10.48550/arXiv.2309.15217](https://doi.org/10.48550/arXiv.2309.15217) ✅
- **Perez et al. (2022), *Red teaming language models with language models*** — generación automática de casos adversarios<br>  ↳ artículo · [doi:10.48550/arXiv.2202.03286](https://doi.org/10.48550/arXiv.2202.03286) ✅
- **NIST (2024), *AI RMF: measure and manage functions*** — las funciones de medición y gestión del marco<br>  ↳ documentación · [nist.gov](https://nist.gov/itl/ai-risk-management-framework) ✅
- **Anthropic (2025), *Building evaluations for Claude applications*** — construcción de un conjunto de evaluación propio<br>  ↳ documentación · [docs.anthropic.com](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests) ✅

## [251 — Privacidad, gobernanza, sostenibilidad y costo de IA](../../classes/part-20-cloud-data-ai-platforms/251-privacidad-gobernanza-sostenibilidad-y-costo-de-ia/README.md)

- **Mitchell et al. (2019), *Model cards for model reporting*** — ficha de modelo como documentación de alcance y límites<br>  ↳ artículo · [doi:10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596) ✅
- **NIST (2024), *AI Risk Management Framework*** — el marco de gestión de riesgo aplicado al sistema<br>  ↳ documentación · [nist.gov](https://nist.gov/itl/ai-risk-management-framework) ✅
- **ISO/IEC 42001 (2023), *Artificial intelligence management system*** — el sistema de gestión certificable para IA<br>  ↳ norma · [iso.org](https://www.iso.org/standard/81230.html) ⏳
- **Green Software Foundation (2025), *Software Carbon Intensity specification*** — medir la intensidad de carbono del software<br>  ↳ documentación · [sci.greensoftware.foundation](https://sci.greensoftware.foundation) ✅
- **Agencia Española de Protección de Datos (2025), *Guía sobre tratamientos con inteligencia artificial*** — obligaciones de protección de datos en tratamientos con IA<br>  ↳ documentación · [aepd.es](https://aepd.es/documento/adecuacion-rgpd-ia.pdf) ✅

## [252 — Proyecto: asistente operativo de CloudShop](../../classes/part-20-cloud-data-ai-platforms/252-proyecto-asistente-operativo-de-cloudshop/README.md)

- **Sculley et al. (2015), *Hidden technical debt in machine learning systems*** — la deuda oculta que el proyecto debe contener<br>  ↳ documentación · [papers.nips.cc](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) ✅
- **Huyen (2022), *Designing Machine Learning Systems*** — diseño del sistema alrededor del modelo<br>  ↳ libro · [ISBN 9781098107963](https://openlibrary.org/isbn/9781098107963) ✅
- **Moses et al. (2022), *Data Quality Fundamentals*** — control de calidad del dato que alimenta al asistente<br>  ↳ libro · [ISBN 9781098112042](https://openlibrary.org/isbn/9781098112042) ✅
- **NIST (2024), *AI Risk Management Framework*** — gestión del riesgo del asistente<br>  ↳ documentación · [nist.gov](https://nist.gov/itl/ai-risk-management-framework) ✅
- **Google (2025), *MLOps: continuous delivery and automation pipelines*** — automatización de la entrega del modelo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) ✅
