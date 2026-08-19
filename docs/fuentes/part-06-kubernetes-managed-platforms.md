# Fuentes de la Parte 06 — Kubernetes y plataformas administradas

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-06-kubernetes-managed-platforms/README.md)

## [073 — API server, etcd, scheduler, controllers y kubelet](../../classes/part-06-kubernetes-managed-platforms/073-api-server-etcd-scheduler-controllers-y-kubelet/README.md)

- **Kubernetes (2025), *Cluster architecture*** — componentes del plano de control y del nodo<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/architecture) ✅
- **Kubernetes (2025), *Dynamic admission control*** — complementos que modifican y validan, y política de fallo<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers) ✅
- **Kubernetes (2025), *Node status and eviction timings*** — plazos de detección, retirada y expulsión<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/architecture/nodes) ✅
- **etcd (2025), *Operations guide: maintenance*** — cuota, compactación, desfragmentación y copias<br>  ↳ documentación · [etcd.io](https://etcd.io/docs/v3.5/op-guide/maintenance) ✅
- **Kubernetes (2025), *Custom resources and the operator pattern*** — extender el modelo con los mismos bucles<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/extend-kubernetes/operator) ✅

## [074 — Pods, ReplicaSets, Deployments y Jobs](../../classes/part-06-kubernetes-managed-platforms/074-pods-replicasets-deployments-y-jobs/README.md)

- **Kubernetes (2025), *Pods*** — qué comparten los contenedores y ciclo de vida conjunto<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/pods) ✅
- **Kubernetes (2025), *Sidecar containers*** — orden garantizado de arranque y terminación<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers) ✅
- **Kubernetes (2025), *Deployments*** — conjuntos de réplicas, estrategia, historial y vuelta atrás<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/deployment) ✅
- **Kubernetes (2025), *Jobs and automatic cleanup*** — reintentos, plazo y eliminación tras finalizar<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/job) ✅
- **Kubernetes (2025), *CronJob*** — concurrencia, plazo de arranque, zona horaria e historial<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs) ✅

## [075 — Services, DNS, Ingress y Gateway API](../../classes/part-06-kubernetes-managed-platforms/075-services-dns-ingress-y-gateway-api/README.md)

- **Kubernetes (2025), *Service*** — tipos, selectores, política de tráfico externo y servicios sin dirección<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/service) ✅
- **Kubernetes (2025), *EndpointSlices*** — la lista de destinos y su propagación<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices) ✅
- **Kubernetes (2025), *DNS for Services and Pods*** — nombres, sufijos de búsqueda y opción de puntos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service) ✅
- **Kubernetes (2025), *Gateway API*** — separación de papeles, reparto por peso y control de exposición<br>  ↳ documentación · [gateway-api.sigs.k8s.io](https://gateway-api.sigs.k8s.io) ✅
- **Kubernetes (2025), *Pod termination and endpoint removal*** — orden de la señal y de la retirada de destinos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/service) ✅

## [076 — ConfigMaps, Secrets y configuración externa](../../classes/part-06-kubernetes-managed-platforms/076-configmaps-secrets-y-configuracion-externa/README.md)

- **Kubernetes (2025), *ConfigMaps*** — consumo como variables y como volúmenes, y actualización<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/configuration/configmap) ✅
- **Kubernetes (2025), *Secrets*** — codificación, riesgos y buenas prácticas<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/configuration/secret) ✅
- **Kubernetes (2025), *Encrypting confidential data at rest*** — cifrado del almacén de estado<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data) ✅
- **Kubernetes (2025), *Immutable ConfigMaps and Secrets*** — versionado y efecto en el plano de control<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/configuration/configmap) ✅
- **Kubernetes SIG Storage (2025), *Secrets Store CSI Driver*** — montar secretos del gestor externo sin crearlos en el clúster<br>  ↳ documentación · [secrets-store-csi-driver.sigs.k8s.io](https://secrets-store-csi-driver.sigs.k8s.io) ✅

## [077 — Volumes, PersistentVolumes, CSI y StatefulSets](../../classes/part-06-kubernetes-managed-platforms/077-volumes-persistentvolumes-csi-y-statefulsets/README.md)

- **Kubernetes (2025), *Persistent Volumes*** — reclamaciones, políticas de recuperación y modos de acceso<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/storage/persistent-volumes) ✅
- **Kubernetes (2025), *Storage Classes and volume binding mode*** — aprovisionamiento inmediato frente a diferido<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/storage/storage-classes) ✅
- **Kubernetes (2025), *StatefulSets*** — identidad, orden, plantillas de reclamación y retención<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset) ✅
- **Kubernetes (2025), *Force delete StatefulSet pods*** — riesgos de forzar y confirmación previa<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod) ✅
- **Kubernetes (2025), *Volume snapshots*** — instantáneas, restauración y consistencia<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/storage/volume-snapshots) ✅

## [078 — Requests, limits, scheduling y autoscaling](../../classes/part-06-kubernetes-managed-platforms/078-requests-limits-scheduling-y-autoscaling/README.md)

- **Kubernetes (2025), *Quality of Service classes*** — cómo se calculan y su papel en la expulsión<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos) ✅
- **Kubernetes (2025), *Node-pressure eviction*** — señales del kubelet y orden de sacrificio<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction) ✅
- **Kubernetes (2025), *Pod topology spread constraints*** — desequilibrio máximo y comportamiento al no poder cumplirse<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints) ✅
- **Kubernetes (2025), *Horizontal Pod Autoscaler*** — fórmula, comportamiento y ventanas de estabilización<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale) ✅
- **Kubernetes autoscaler (2025), *Cluster Autoscaler FAQ*** — qué impide retirar un nodo<br>  ↳ documentación · [github.com](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md) ✅

## [079 — Probes, rollouts, rollback y PodDisruptionBudget](../../classes/part-06-kubernetes-managed-platforms/079-probes-rollouts-rollback-y-poddisruptionbudget/README.md)

- **Kubernetes (2025), *Disruptions*** — voluntarias e involuntarias, y alcance del presupuesto<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/pods/disruptions) ✅
- **Kubernetes (2025), *Specifying a Disruption Budget*** — expresión, selector y estado<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/run-application/configure-pdb) ✅
- **Kubernetes (2025), *Safely drain a node*** — secuencia, opciones y bloqueos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node) ✅
- **Kubernetes (2025), *Configure probes*** — tipos, umbrales y tiempos de espera<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes) ✅
- **Google (2018), *The Site Reliability Workbook*** — despliegue progresivo y criterios de promoción<br>  ↳ documentación · [sre.google](https://sre.google/workbook/canarying-releases) ✅

## [080 — Namespaces, RBAC, NetworkPolicy y admission](../../classes/part-06-kubernetes-managed-platforms/080-namespaces-rbac-networkpolicy-y-admission/README.md)

- **Kubernetes (2025), *Using RBAC authorization*** — roles, vinculaciones, escalada y protecciones<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/reference/access-authn-authz/rbac) ✅
- **Kubernetes (2025), *Network policies*** — semántica de selección, direcciones y requisitos del complemento<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies) ✅
- **Kubernetes (2025), *Pod Security Admission*** — perfiles, modos y adopción por fases<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/security/pod-security-admission) ✅
- **Kubernetes (2025), *Validating Admission Policy*** — políticas con expresiones dentro del servidor de API<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy) ✅
- **Kubernetes (2025), *Multi-tenancy*** — límites del espacio de nombres como frontera y alternativas<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/security/multi-tenancy) ✅

## [081 — Helm, Kustomize y gestión de paquetes](../../classes/part-06-kubernetes-managed-platforms/081-helm-kustomize-y-gestion-de-paquetes/README.md)

- **Kubernetes (2025), *Declarative management with Kustomize*** — bases, capas, parches y generadores<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization) ✅
- **Helm (2025), *Charts and release lifecycle*** — plantillas, valores, historial y estados<br>  ↳ documentación · [helm.sh](https://helm.sh/docs/topics/charts) ✅
- **Helm (2025), *Custom Resource Definitions*** — por qué no se actualizan con el paquete<br>  ↳ documentación · [helm.sh](https://helm.sh/docs/chart_best_practices/custom_resource_definitions) ✅
- **Kubernetes (2025), *Server-Side Apply*** — gestores de campos y detección de conflictos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/reference/using-api/server-side-apply) ✅
- **Kustomize (2025), *Labels and selectors*** — etiquetas comunes y campos inmutables<br>  ↳ documentación · [kubectl.docs.kubernetes.io](https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/labels) ✅

## [082 — Logs, métricas, eventos y depuración](../../classes/part-06-kubernetes-managed-platforms/082-logs-metricas-eventos-y-depuracion/README.md)

- **Kubernetes (2025), *Events and their retention*** — origen, agregación y caducidad<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1) ✅
- **Kubernetes (2025), *Logging architecture*** — rotación en el nodo y necesidad de recolector<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/cluster-administration/logging) ✅
- **Kubernetes (2025), *Resource metrics pipeline*** — para qué sirve la fuente del escalado y qué no es<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline) ✅
- **kube-state-metrics (2025), *Documentation*** — métricas de estado de los objetos del clúster<br>  ↳ documentación · [github.com](https://github.com/kubernetes/kube-state-metrics/tree/main/docs) ✅
- **Kubernetes (2025), *Debug running pods*** — orden de diagnóstico y contenedores efímeros<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod) ✅

## [083 — EKS, AKS y GKE: similitudes y diferencias](../../classes/part-06-kubernetes-managed-platforms/083-eks-aks-y-gke-similitudes-y-diferencias/README.md)

- **Kubernetes (2025), *Version skew policy*** — desviación admitida entre plano de control y nodos<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/releases/version-skew-policy) ✅
- **Kubernetes (2025), *Deprecated API migration guide*** — versiones retiradas y cómo detectarlas<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/reference/using-api/deprecation-guide) ✅
- **AWS (2025), *Amazon EKS networking and IP address planning*** — direcciones por nodo y modos de asignación<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/eks/latest/userguide/eks-networking.html) ✅
- **Microsoft (2025), *AKS networking concepts*** — modelos de red y sus consecuencias de direccionamiento<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/concepts-network) ✅
- **Google Cloud (2025), *GKE cluster networking and IP allocation*** — rangos secundarios y límites por nodo<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) ✅

## [084 — Proyecto: plataforma Kubernetes portable](../../classes/part-06-kubernetes-managed-platforms/084-proyecto-plataforma-kubernetes-portable/README.md)

- **Kubernetes (2025), *Production environment checklist*** — consideraciones de un clúster operable<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/setup/production-environment) ✅
- **Kubernetes (2025), *Configuration best practices*** — decisiones que conviene tomar al crear<br>  ↳ documentación · [kubernetes.io](https://kubernetes.io/docs/concepts/configuration/overview) ✅
- **CNCF (2025), *Kubernetes cluster conformance*** — qué garantiza la conformidad y qué no<br>  ↳ documentación · [cncf.io](https://cncf.io/certification/software-conformance) ✅
- **Google (2018), *The Site Reliability Workbook*** — simulacros de fallo y hallazgos<br>  ↳ documentación · [sre.google](https://sre.google/workbook/postmortem-culture) ✅
- **Kubernetes (2025), *Descheduler*** — reequilibrado de pods tras cambios de topología<br>  ↳ documentación · [github.com](https://github.com/kubernetes-sigs/descheduler) ✅
