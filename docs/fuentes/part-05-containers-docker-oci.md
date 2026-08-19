# Fuentes de la Parte 05 — Contenedores, Docker y OCI

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-05-containers-docker-oci/README.md)

## [061 — Imágenes, capas, registros y estándar OCI](../../classes/part-05-containers-docker-oci/061-imagenes-capas-registros-y-estandar-oci/README.md)

- **Open Container Initiative (2025), *Image Format Specification*** — manifiesto, configuración, capas e índice<br>  ↳ documentación · [github.com](https://github.com/opencontainers/image-spec/blob/main/spec.md) ✅
- **Open Container Initiative (2025), *Distribution Specification*** — API del registro, huellas y autenticación<br>  ↳ documentación · [github.com](https://github.com/opencontainers/distribution-spec/blob/main/spec.md) ✅
- **Open Container Initiative (2025), *Runtime Specification*** — paquete de sistema de ficheros y configuración de ejecución<br>  ↳ documentación · [github.com](https://github.com/opencontainers/runtime-spec/blob/main/spec.md) ✅
- **Docker (2025), *Multi-platform builds*** — buildx, índices de imágenes y construcción nativa frente a emulada<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/build/building/multi-platform) ✅
- **Docker (2025), *Image layers and storage drivers*** — sistema de ficheros de unión y ficheros de borrado<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/storage/drivers) ✅

## [062 — Dockerfile reproducible y builds multi-stage](../../classes/part-05-containers-docker-oci/062-dockerfile-reproducible-y-builds-multi-stage/README.md)

- **Docker (2025), *Dockerfile best practices*** — orden de instrucciones, caché y contexto<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/build/building/best-practices) ✅
- **Docker (2025), *Multi-stage builds*** — etapas, `--target` y copia entre etapas<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/build/building/multi-stage) ✅
- **Docker (2025), *Build secrets and cache mounts*** — `--mount=type=secret` y `type=cache`<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/build/building/secrets) ✅
- **Docker (2025), *Cache storage backends*** — caché compartida en registro para canalizaciones<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/build/cache/backends) ✅
- **Google (2025), *Distroless container images*** — bases sin intérprete de órdenes ni gestor de paquetes<br>  ↳ documentación · [github.com](https://github.com/GoogleContainerTools/distroless) ✅

## [063 — Namespaces, cgroups y runtime de contenedores](../../classes/part-05-containers-docker-oci/063-namespaces-cgroups-y-runtime-de-contenedores/README.md)

- **Linux (2025), *namespaces(7)*** — los siete espacios de nombres y su semántica<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/namespaces.7.html) ✅
- **Linux (2025), *cgroups(7)*** — `memory.max`, `cpu.max` e interfaces de eventos<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/cgroups.7.html) ✅
- **Linux (2025), *pid_namespaces(7)*** — semántica de señales del proceso número uno y recolección de huérfanos<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html) ✅
- **Open Container Initiative (2025), *Runtime Specification*** — configuración que aplica el tiempo de ejecución<br>  ↳ documentación · [github.com](https://github.com/opencontainers/runtime-spec/blob/main/config-linux.md) ✅
- **Google (2025), *gVisor: what is it*** — aislamiento con núcleo en espacio de usuario y sus compromisos<br>  ↳ documentación · [gvisor.dev](https://gvisor.dev/docs) ✅

## [064 — Volúmenes, bind mounts y persistencia](../../classes/part-05-containers-docker-oci/064-volumenes-bind-mounts-y-persistencia/README.md)

- **Docker (2025), *Manage data in Docker*** — volúmenes, montajes del anfitrión y montajes en memoria<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/storage) ✅
- **Docker (2025), *Storage drivers and copy-on-write*** — coste de la primera escritura sobre un fichero existente<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/storage/drivers) ✅
- **Linux (2025), *tmpfs*** — contabilidad de memoria y opciones de montaje<br>  ↳ documentación · [kernel.org](https://kernel.org/doc/html/latest/filesystems/tmpfs.html) ✅
- **Kubernetes (2025), *Persistent volumes and access modes*** — un escritor por volumen de bloque y sistemas compartidos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/storage/persistent-volumes) ✅
- **Docker (2025), *Back up, restore, or migrate data volumes*** — procedimiento y sus límites con motores en marcha<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/storage/volumes) ✅

## [065 — Redes bridge, DNS interno y publicación de puertos](../../classes/part-05-containers-docker-oci/065-redes-bridge-dns-interno-y-publicacion-de-puertos/README.md)

- **Docker (2025), *Networking overview*** — puentes, redes definidas por el usuario y resolución de nombres<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/network) ✅
- **Docker (2025), *Packet filtering and firewalls*** — cadenas de traducción y su relación con el cortafuegos del anfitrión<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/network/packet-filtering-firewalls) ✅
- **Docker (2025), *Network drivers and options*** — modo anfitrión, ninguno, compartido y opciones de unidad máxima<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/network/drivers) ✅
- **Linux (2025), *veth(4)*** — pares de interfaces virtuales<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man4/veth.4.html) ✅
- **Cloudflare (2024), *Path MTU discovery in practice*** — por qué falla el descubrimiento y cómo se manifiesta<br>  ↳ documentación · [blog.cloudflare.com](https://blog.cloudflare.com/path-mtu-discovery-in-practice) ✅

## [066 — Docker Compose y aplicaciones multiservicio](../../classes/part-05-containers-docker-oci/066-docker-compose-y-aplicaciones-multiservicio/README.md)

- **Docker (2025), *Compose file reference*** — servicios, dependencias, perfiles y secretos<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/reference/compose-file) ✅
- **Docker (2025), *Control startup order*** — `depends_on`, condiciones y comprobaciones de estado<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/compose/how-tos/startup-order) ✅
- **Docker (2025), *Merge Compose files*** — superposición, `override` y variables de entorno<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge) ✅
- **Docker (2025), *Compose Develop specification*** — sincronización de código para desarrollo<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/compose/how-tos/file-watch) ✅
- **Docker (2025), *Use secrets in Compose*** — secretos como ficheros en vez de variables de entorno<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/compose/how-tos/use-secrets) ✅

## [067 — Registros, SBOM, firma y procedencia de imágenes](../../classes/part-05-containers-docker-oci/067-registros-sbom-firma-y-procedencia-de-imagenes/README.md)

- **Sigstore (2025), *Keyless signing and verification with cosign*** — identidad federada y registro de transparencia<br>  ↳ documentación · [docs.sigstore.dev](https://docs.sigstore.dev/cosign/signing/overview) ✅
- **SLSA (2025), *Provenance and build levels*** — qué declara la procedencia y qué ataques cubre cada nivel<br>  ↳ documentación · [slsa.dev](https://slsa.dev/spec/v1.0/provenance) ✅
- **OCI (2025), *Referrers API in the distribution specification*** — artefactos asociados a una imagen por huella<br>  ↳ documentación · [github.com](https://github.com/opencontainers/distribution-spec/blob/main/spec.md) ✅
- **CISA (2024), *Minimum elements for a Software Bill of Materials*** — contenido mínimo y usos previstos<br>  ↳ documentación · [cisa.gov](https://www.cisa.gov/sbom) ⏳
- **Aqua Security (2025), *Trivy: filtering and ignore files*** — severidad, hallazgos sin corrección y excepciones con caducidad<br>  ↳ documentación · [trivy.dev](https://trivy.dev/latest/docs/configuration/filtering) ✅

## [068 — Límites, health checks y apagado ordenado](../../classes/part-05-containers-docker-oci/068-limites-health-checks-y-apagado-ordenado/README.md)

- **Kubernetes (2025), *Configure liveness, readiness and startup probes*** — semántica y parámetros de las tres<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes) ✅
- **Kubernetes (2025), *Pod lifecycle: termination*** — orden de la señal, retirada de destinos y plazo de gracia<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle) ✅
- **Kubernetes (2025), *Requests and limits*** — planificación frente a imposición, y efectos de cada una<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers) ✅
- **Docker (2025), *docker stop and signal handling*** — plazo, señales y comportamiento del proceso número uno<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/reference/cli/docker/container/stop) ✅
- **Google (2018), *The Site Reliability Workbook*** — errores durante despliegues y presupuesto de error<br>  ↳ documentación · [sre.google](https://sre.google/workbook/implementing-slos) ✅

## [069 — Rootless, capabilities, seccomp y secretos](../../classes/part-05-containers-docker-oci/069-rootless-capabilities-seccomp-y-secretos/README.md)

- **Linux (2025), *capabilities(7)*** — las piezas del poder del usuario cero y su semántica<br>  ↳ documentación · [man7.org](https://man7.org/linux/man-pages/man7/capabilities.7.html) ✅
- **Docker (2025), *Runtime privilege and Linux capabilities*** — conjunto por defecto y modo privilegiado<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/containers/run) ✅
- **Docker (2025), *Seccomp security profiles*** — perfil por defecto y consecuencias de desactivarlo<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/security/seccomp) ✅
- **Docker (2025), *Rootless mode*** — espacios de nombres de usuario, limitaciones y configuración<br>  ↳ documentación · [docs.docker.com](https://docs.docker.com/engine/security/rootless) ✅
- **NIST (2022), *SP 800-190: Application Container Security Guide*** — modelo de amenazas y controles por capa<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/190/final) ✅

## [070 — Diagnóstico de CPU, memoria, red y filesystem](../../classes/part-05-containers-docker-oci/070-diagnostico-de-cpu-memoria-red-y-filesystem/README.md)

- **Linux (2025), *Pressure Stall Information*** — `some` y `full` por recurso y por grupo de control<br>  ↳ documentación · [docs.kernel.org](https://docs.kernel.org/accounting/psi.html) ✅
- **Kubernetes (2025), *Debug running pods with ephemeral containers*** — `kubectl debug` y `--target`<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod) ✅
- **Brendan Gregg (2020), *Systems Performance*** — método de utilización, saturación y errores<br>  ↳ documentación · [brendangregg.com](https://brendangregg.com/systems-performance-2nd-edition-book.html) ✅
- **Linux (2025), *nf_conntrack sysctl*** — tamaño de la tabla, ocupación y descarte de paquetes<br>  ↳ documentación · [kernel.org](https://kernel.org/doc/html/latest/networking/nf_conntrack-sysctl.html) ✅
- **Go (2025), *Profiling Go programs with pprof*** — perfiles de CPU y memoria, y comparación entre instantes<br>  ↳ documentación · [go.dev](https://go.dev/blog/pprof) ✅

## [071 — Migración de una aplicación legacy a contenedores](../../classes/part-05-containers-docker-oci/071-migracion-de-una-aplicacion-legacy-a-contenedores/README.md)

- **Martin Fowler (2004), *StranglerFigApplication*** — sustitución progresiva en lugar de reemplazo único<br>  ↳ documentación · [martinfowler.com](https://martinfowler.com/bliki/StranglerFigApplication.html) ✅
- **Adam Wiggins (2017), *The Twelve-Factor App*** — configuración, procesos sin estado, registros y procesos administrativos<br>  ↳ documentación · [12factor.net](https://12factor.net) ✅
- **Kubernetes (2025), *CronJob concurrency policy*** — una sola ejecución y solapamiento<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs) ✅
- **Microsoft (2025), *Migrate applications to containers: assessment*** — inventario de dependencias y criterios de idoneidad<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/migrate/tutorial-app-containerization-aspnet-kubernetes) ✅
- **Sam Newman (2019), *Monolith to Microservices*** — patrones de convivencia y cambios de esquema compatibles<br>  ↳ documentación · [samnewman.io](https://samnewman.io/books/monolith-to-microservices) ✅

## [072 — Proyecto: stack OCI endurecido y observable](../../classes/part-05-containers-docker-oci/072-proyecto-stack-oci-endurecido-y-observable/README.md)

- **Open Container Initiative (2025), *Specifications overview*** — qué normaliza el conjunto y qué queda fuera<br>  ↳ norma · [opencontainers.org](https://opencontainers.org/release-notices/overview) ✅
- **NIST (2022), *SP 800-190: Application Container Security Guide*** — riesgos por capa y contramedidas<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/190/final) ✅
- **CNCF (2025), *Software Supply Chain Best Practices*** — inventario, firma, procedencia y verificación<br>  ↳ documentación · [github.com](https://github.com/cncf/tag-security/blob/main/community/working-groups/supply-chain-security/secure-software-factory/Secure_Software_Factory_Whitepaper.pdf) ✅
- **Linux (2025), *Pressure Stall Information*** — señales de saturación por recurso y por grupo de control<br>  ↳ documentación · [docs.kernel.org](https://docs.kernel.org/accounting/psi.html) ✅
- **Google (2018), *The Site Reliability Workbook*** — simulacros de fallo y lo que se aprende de cada uno<br>  ↳ documentación · [sre.google](https://sre.google/workbook/postmortem-culture) ✅
