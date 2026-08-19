# Fuentes de la Parte 00 — Fundamentos de computación, redes y Linux

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-00-foundations-computing-networking-linux/README.md)

## [001 — Computación digital y modelo mental de la nube](../../classes/part-00-foundations-computing-networking-linux/001-computacion-digital-y-modelo-mental-de-la-nube/README.md)

- **Mell et al. (2011), *The NIST Definition of Cloud Computing*** — las cinco características esenciales que separan nube de hosting renombrado<br>  ↳ artículo · [doi:10.6028/NIST.SP.800-145](https://doi.org/10.6028/NIST.SP.800-145) ✅
- **Dean (2009), *Latency Numbers Every Programmer Should Know*** — cifras de referencia de la jerarquía de memoria<br>  ↳ documentación · [static.googleusercontent.com](https://static.googleusercontent.com/media/research.google.com/en//people/jeff/stanford-295-talk.pdf) ✅
- **Kurose et al. (2021), *Computer Networking: A Top-Down Approach*** — retardo, pérdida y throughput<br>  ↳ libro · [ISBN 9781292405469](https://openlibrary.org/isbn/9781292405469) ✅
- **Barroso et al. (2018), *The Datacenter as a Computer*** — economía y utilización del centro de datos<br>  ↳ artículo · [doi:10.2200/S00874ED3V01Y201809CAC046](https://doi.org/10.2200/S00874ED3V01Y201809CAC046) ✅
- **Gray (2008), *Distributed Computing Economics*** — por qué conviene mover el cómputo hacia los datos<br>  ↳ artículo · [doi:10.1145/1394127.1394131](https://doi.org/10.1145/1394127.1394131) ✅

## [002 — Terminal, sistema de archivos, procesos y variables de entorno](../../classes/part-00-foundations-computing-networking-linux/002-terminal-sistema-de-archivos-procesos-y-variables-de-entorno/README.md)

- **The Open Group (2018), *POSIX.1-2017*** — semántica normativa de fork, execve y wait<br>  ↳ norma · [pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fork.html) ✅
- **Kerrisk, *signal(7)*** — Linux manual pages: catálogo de señales y semántica de SIGTERM y SIGKILL<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/signal.7.html) ✅
- **Kerrisk (2010), *The Linux Programming Interface*** — creación de procesos y ejecución de programas<br>  ↳ libro · _sin localizador_ ⏳
- **systemd (2024), *systemd.exec(5)*** — cómo se construye el entorno de un servicio<br>  ↳ documentación · [freedesktop.org](https://freedesktop.org/software/systemd/man/systemd.exec.html) ✅
- **Ward (2021), *How Linux Works*** — procesos, dispositivos y arranque<br>  ↳ libro · [ISBN 9798483731795](https://openlibrary.org/isbn/9798483731795) ✅

## [003 — Git, GitHub y trabajo reproducible](../../classes/part-00-foundations-computing-networking-linux/003-git-github-y-trabajo-reproducible/README.md)

- **Chacon et al. (2014), *Pro Git*** — objetos, referencias y modelo de almacenamiento<br>  ↳ documentación · [git-scm.com](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) ✅
- **Git (2024), *git-reset(1)*** — tabla oficial del efecto de cada modo sobre HEAD, índice y árbol de trabajo<br>  ↳ documentación · [git-scm.com](https://git-scm.com/docs/git-reset) ✅
- **Git (2024), *git-bisect(1)*** — búsqueda binaria automatizada sobre el historial<br>  ↳ documentación · [git-scm.com](https://git-scm.com/docs/git-bisect) ✅
- **Open Container Initiative (2024), *Image Specification*** — anotaciones estándar, incluida `org.opencontainers.image.revision`<br>  ↳ documentación · [github.com](https://github.com/opencontainers/image-spec/blob/main/annotations.md) ✅
- **Git (2024), *gitrevisions(7)*** — sintaxis de `HEAD@{n}`, `~` y `^` para navegar el grafo<br>  ↳ documentación · [git-scm.com](https://git-scm.com/docs/gitrevisions) ✅

## [004 — Python, JSON y automatización mínima](../../classes/part-00-foundations-computing-networking-linux/004-python-json-y-automatizacion-minima/README.md)

- **Bray (2017), *RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format*** — sección 6 sobre los límites de precisión numérica<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc8259) ✅
- **IEEE (2019), *Standard for Floating-Point Arithmetic (IEEE 754-2019)*** — por qué la aritmética en coma flotante no representa exactamente los decimales<br>  ↳ artículo · [doi:10.1109/IEEESTD.2019.8766229](https://doi.org/10.1109/IEEESTD.2019.8766229) ✅
- **Goldberg (1991), *What Every Computer Scientist Should Know About Floating-Point Arithmetic*** — los casos en que comparar flotantes directamente falla<br>  ↳ artículo · [doi:10.1145/103162.103163](https://doi.org/10.1145/103162.103163) ✅
- **Python Software Foundation (2024), *decimal*** — Decimal fixed-point and floating-point arithmetic<br>  ↳ documentación · [docs.python.org](https://docs.python.org/3/library/decimal.html) ✅
- **Brooker (2015), *Exponential Backoff and Jitter*** — datos comparados de las variantes de jitter<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter) ✅

## [005 — Redes por capas, TCP/IP, puertos y sockets](../../classes/part-00-foundations-computing-networking-linux/005-redes-por-capas-tcp-ip-puertos-y-sockets/README.md)

- **Kurose et al. (2021), *Computer Networking: A Top-Down Approach*** — transporte y capa de red<br>  ↳ libro · [ISBN 9781292405469](https://openlibrary.org/isbn/9781292405469) ✅
- **Postel (1981), *RFC 793: Transmission Control Protocol*** — saludo de tres vías y máquina de estados<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc793) ✅
- **Borman (2014), *RFC 7323: TCP Extensions for High Performance*** — window scaling y el producto ancho de banda × retardo<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc7323) ✅
- **Rescorla (2018), *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*** — saludo de 1-RTT<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc8446) ✅
- **Kerrisk, *ss(8)*** — estados de socket y parámetros del núcleo de Linux<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/tcp.7.html) ✅

## [006 — DNS, HTTP, HTTPS y TLS de extremo a extremo](../../classes/part-00-foundations-computing-networking-linux/006-dns-http-https-y-tls-de-extremo-a-extremo/README.md)

- **Mockapetris (1987), *RFC 1035: Domain Names*** — Implementation and Specification<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc1035) ✅
- **Rescorla (2018), *RFC 8446: TLS 1.3*** — saludo de 1-RTT, 0-RTT y sus riesgos de repetición<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc8446) ✅
- **Fielding et al. (2022), *RFC 9110: HTTP Semantics*** — semántica de códigos de estado<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc9110) ✅
- **Fielding (2022), *RFC 9111: HTTP Caching*** — `Cache-Control`, validadores y respuestas 304<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc9111) ✅
- **Grigorik (2013), *High Performance Browser Networking*** — coste en RTT de DNS, TCP y TLS<br>  ↳ documentación · [hpbn.co](https://hpbn.co) ✅

## [007 — Linux: usuarios, permisos, servicios y logs](../../classes/part-00-foundations-computing-networking-linux/007-linux-usuarios-permisos-servicios-y-logs/README.md)

- **Kerrisk, *capabilities(7)*** — catálogo completo de capacidades de Linux y sus implicaciones<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/capabilities.7.html) ✅
- **systemd (2024), *systemd.exec(5)*** — directivas de endurecimiento: `ProtectSystem`, `ReadWritePaths`, `NoNewPrivileges`<br>  ↳ documentación · [freedesktop.org](https://freedesktop.org/software/systemd/man/systemd.exec.html) ✅
- **systemd (2024), *systemd.service(5)*** — códigos de salida 200-241 y política de reinicio<br>  ↳ documentación · [freedesktop.org](https://freedesktop.org/software/systemd/man/systemd.service.html) ✅
- **systemd (2024), *journalctl(1)*** — filtrado por campos, prioridades y arranque<br>  ↳ documentación · [freedesktop.org](https://freedesktop.org/software/systemd/man/journalctl.html) ✅
- **Ward (2021), *How Linux Works*** — arranque, systemd y configuración del sistema<br>  ↳ libro · [ISBN 9798483731795](https://openlibrary.org/isbn/9798483731795) ✅

## [008 — Virtualización, hipervisores e imágenes](../../classes/part-00-foundations-computing-networking-linux/008-virtualizacion-hipervisores-e-imagenes/README.md)

- **Agache (2020), *Firecracker: Lightweight Virtualization for Serverless Applications*** — cifras de arranque y sobrecarga<br>  ↳ documentación · [usenix.org](https://usenix.org/conference/nsdi20/presentation/agache) ✅
- **Kerrisk, *namespaces(7)*** — los siete espacios de nombres de Linux y su semántica<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/namespaces.7.html) ✅
- **Kerrisk, *cgroups(7)*** — límites, contabilidad y jerarquía de control de recursos<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/cgroups.7.html) ✅
- **Open Container Initiative (2024), *Image Specification*** — manifiesto, capas y direccionamiento por digest<br>  ↳ documentación · [github.com](https://github.com/opencontainers/image-spec/blob/main/spec.md) ✅
- **Rice (2020), *Container Security*** — espacios de nombres, capacidades y vectores de escape<br>  ↳ libro · [ISBN 9781492056706](https://openlibrary.org/isbn/9781492056706) ✅

## [009 — APIs REST, autenticación y contratos](../../classes/part-00-foundations-computing-networking-linux/009-apis-rest-autenticacion-y-contratos/README.md)

- **Fielding et al. (2022), *RFC 9110: HTTP Semantics*** — métodos seguros e idempotentes<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc9110) ✅
- **Jena (2024), *The Idempotency-Key HTTP Header Field*** — semántica y manejo de reintentos<br>  ↳ norma · [datatracker.ietf.org](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header) ✅
- **OWASP (2023), *API Security Top 10*** — los fallos de autorización más frecuentes en APIs REST<br>  ↳ documentación · [owasp.org](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization) ✅
- **Wilde (2019), *RFC 8594: The Sunset HTTP Header Field*** — anunciar la retirada de un contrato<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc8594) ✅
- **Nottingham (2022), *RFC 9205: Building Protocols with HTTP*** — buenas prácticas de diseño sobre HTTP<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc9205) ✅

## [010 — Responsabilidad compartida y pensamiento de riesgo](../../classes/part-00-foundations-computing-networking-linux/010-responsabilidad-compartida-y-pensamiento-de-riesgo/README.md)

- **AWS (2024), *Shared Responsibility Model*** — reparto de controles por modelo de servicio<br>  ↳ documentación · [aws.amazon.com](https://aws.amazon.com/compliance/shared-responsibility-model) ✅
- **Microsoft (2024), *Shared responsibility in the cloud*** — tabla comparada IaaS/PaaS/SaaS<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) ✅
- **Cloud Security Alliance (2024), *Top Threats to Cloud Computing*** — taxonomía de amenazas con incidentes documentados<br>  ↳ documentación · [cloudsecurityalliance.org](https://cloudsecurityalliance.org/research/topics/top-threats) ✅
- **Shostack (2014), *Threat Modeling: Designing for Security*** — las cuatro preguntas y el uso de STRIDE<br>  ↳ libro · [ISBN 9781306427067](https://openlibrary.org/isbn/9781306427067) ✅
- **NIST (2018), *Framework for Improving Critical Infrastructure Cybersecurity*** — funciones identificar, proteger, detectar, responder y recuperar<br>  ↳ artículo · [doi:10.6028/NIST.CSWP.04162018](https://doi.org/10.6028/NIST.CSWP.04162018) ✅

## [011 — Costo, energía, capacidad y medición básica](../../classes/part-00-foundations-computing-networking-linux/011-costo-energia-capacidad-y-medicion-basica/README.md)

- **Little (1961), *A Proof for the Queuing Formula: L = λW*** — relación entre concurrencia, tasa de llegada y tiempo de servicio para dimensionar<br>  ↳ artículo · [doi:10.1287/opre.9.3.383](https://doi.org/10.1287/opre.9.3.383) ✅
- **Storment et al. (2023), *Cloud FinOps*** — unidad de coste, etiquetado y modelos de compromiso<br>  ↳ libro · [ISBN 9781492098355](https://openlibrary.org/isbn/9781492098355) ✅
- **Gunther (2007), *Guerrilla Capacity Planning*** — leyes de escalabilidad y el efecto de la utilización sobre la latencia<br>  ↳ libro · [ISBN 9783540261384](https://openlibrary.org/isbn/9783540261384) ✅
- **Barroso et al. (2018), *The Datacenter as a Computer*** — PUE, eficiencia y coste total<br>  ↳ artículo · [doi:10.2200/S00874ED3V01Y201809CAC046](https://doi.org/10.2200/S00874ED3V01Y201809CAC046) ✅
- **FinOps Foundation (2024), *FinOps Framework*** — capacidades de asignación, previsión y optimización de tasa<br>  ↳ documentación · [finops.org](https://finops.org/framework) ✅

## [012 — Proyecto: servicio local reproducible y observable](../../classes/part-00-foundations-computing-networking-linux/012-proyecto-servicio-local-reproducible-y-observable/README.md)

- **Beyer (2016), *Site Reliability Engineering*** — las cuatro señales doradas<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/monitoring-distributed-systems) ✅
- **Kubernetes (2024), *Configure Liveness, Readiness and Startup Probes*** — semántica y efectos de cada sonda<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes) ✅
- **Nygard (2018), *Release It!*** — patrones de estabilidad: timeouts, bulkheads y circuit breaker<br>  ↳ libro · [ISBN 9781680502398](https://openlibrary.org/isbn/9781680502398) ✅
- **Prometheus (2024), *Histograms and summaries*** — por qué los histogramas son agregables y los cuantiles precalculados no<br>  ↳ documentación · [prometheus.io](https://prometheus.io/docs/practices/histograms) ✅
- **Dean et al. (2013), *The Tail at Scale*** — por qué la latencia de cola gobierna la experiencia y no la media<br>  ↳ artículo · [doi:10.1145/2408776.2408794](https://doi.org/10.1145/2408776.2408794) ✅
