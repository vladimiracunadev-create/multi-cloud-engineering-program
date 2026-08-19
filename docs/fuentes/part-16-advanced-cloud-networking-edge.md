# Fuentes de la Parte 16 — Redes cloud avanzadas, conectividad híbrida y edge

Generado por `python scripts/verify-sources --write`. No editar a mano.

12 clases · **60 fuentes citadas**. Cada una indica el uso que esa
clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·
⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).

[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/part-16-advanced-cloud-networking-edge/README.md)

## [193 — CIDR, subnetting y planificación IP a escala](../../classes/part-16-advanced-cloud-networking-edge/193-cidr-subnetting-y-planificacion-ip-a-escala/README.md)

- ***RFC 4632*** — Classless Inter-Domain Routing (CIDR)<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc4632) ✅
- ***RFC 1918*** — Address allocation for private internets<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc1918) ✅
- ***RFC 6598*** — IANA-reserved IPv4 prefix for shared address space (100.64.0.0/10)<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc6598) ✅
- **AWS (2025), *VPC sizing and IP address planning*** — reservas y solapamientos al dimensionar rangos de direcciones<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) ✅
- **Microsoft (2025), *Plan for IP addressing in Azure landing zones*** — planificación de direccionamiento en zonas de aterrizaje<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/plan-for-ip-addressing) ✅

## [194 — Routing, BGP, tránsito y propagación de rutas](../../classes/part-16-advanced-cloud-networking-edge/194-routing-bgp-transito-y-propagacion-de-rutas/README.md)

- ***RFC 4271*** — A Border Gateway Protocol 4 (BGP-4)<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc4271) ✅
- **AWS (2025), *Route tables and route priority in VPC*** — prioridad de rutas dentro de la VPC<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/userguide/VpcSubnetRouting.html) ✅
- **Microsoft (2025), *Virtual network traffic routing*** — orden de resolución de rutas en la red virtual<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) ✅
- **Google Cloud (2025), *Routes and routing order*** — precedencia de rutas en Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/routes) ✅
- **Cloudflare (2025), *What is BGP? Route leaks and hijacks*** — fugas y secuestros de ruta como riesgo operativo<br>  ↳ documentación · [cloudflare.com](https://cloudflare.com/learning/security/glossary/bgp-hijacking) ✅

## [195 — DNS autoritativo, recursivo, split-horizon y DNSSEC](../../classes/part-16-advanced-cloud-networking-edge/195-dns-autoritativo-recursivo-split-horizon-y-dnssec/README.md)

- ***RFC 1034 y 1035*** — Domain names: concepts, facilities and implementation<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc1034) ✅
- ***RFC 2308*** — Negative caching of DNS queries<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc2308) ✅
- ***RFC 4033*** — DNS security introduction and requirements (DNSSEC)<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc4033) ✅
- **AWS (2025), *Route 53: private hosted zones and resolver endpoints*** — resolución partida entre red privada y pública<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) ✅
- **OWASP (2025), *Subdomain takeover*** — registros huérfanos<br>  ↳ documentación · [owasp.org](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/10-Test_for_Subdomain_Takeover) ✅

## [196 — Balanceo L4/L7, proxies, TLS y gestión de certificados](../../classes/part-16-advanced-cloud-networking-edge/196-balanceo-l4-l7-proxies-tls-y-gestion-de-certificados/README.md)

- **AWS (2025), *Elastic Load Balancing: types, health checks and connection draining*** — diferencias por capa y retirada ordenada de instancias<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) ✅
- **Envoy (2025), *Load balancing and outlier detection*** — expulsión automática de destinos que se degradan<br>  ↳ documentación · [envoyproxy.io](https://envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/overview) ✅
- ***RFC 8555*** — Automatic Certificate Management Environment (ACME)<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc8555) ✅
- **Mozilla (2025), *Server side TLS configuration guidelines*** — versiones de protocolo y conjuntos de cifrado admisibles<br>  ↳ documentación · [wiki.mozilla.org](https://wiki.mozilla.org/Security/Server_Side_TLS) ✅
- **Google (2016), *SRE Book: load balancing at the frontend*** — reparto de carga antes de llegar al servicio<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/load-balancing-frontend) ✅

## [197 — CDN, caché, origin shielding y edge compute](../../classes/part-16-advanced-cloud-networking-edge/197-cdn-cache-origin-shielding-y-edge-compute/README.md)

- ***RFC 9111*** — HTTP caching<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc9111) ✅
- ***RFC 5861*** — HTTP cache-control extensions for stale content<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc5861) ✅
- **AWS (2025), *CloudFront: cache key and origin shield*** — qué entra en la clave de caché y cómo se protege el origen<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-the-cache-key.html) ✅
- **Fastly (2025), *Purging with surrogate keys*** — invalidación selectiva por etiquetas de contenido<br>  ↳ documentación · [docs.fastly.com](https://docs.fastly.com/en/guides/working-with-surrogate-keys) ✅
- **Cloudflare (2025), *Cloudflare Workers: what edge compute is good for*** — qué conviene ejecutar en el borde y qué no<br>  ↳ documentación · [developers.cloudflare.com](https://developers.cloudflare.com/workers) ✅

## [198 — VPN, Direct Connect, ExpressRoute e Interconnect](../../classes/part-16-advanced-cloud-networking-edge/198-vpn-direct-connect-expressroute-e-interconnect/README.md)

- **AWS (2025), *Direct Connect resiliency recommendations*** — topologías redundantes del enlace y sus modos de fallo<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/directconnect/latest/UserGuide/high_resiliency.html) ✅
- **Microsoft (2025), *ExpressRoute design for high availability*** — diseño de alta disponibilidad del enlace dedicado<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/expressroute/designing-for-high-availability-with-expressroute) ✅
- **Google Cloud (2025), *Cloud Interconnect and HA VPN topologies*** — las topologías equivalentes en Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/network-connectivity/docs/interconnect) ✅
- ***RFC 4459*** — MTU and fragmentation issues with in-the-network tunneling<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc4459) ✅
- ***RFC 7296*** — Internet Key Exchange Protocol Version 2 (IKEv2)<br>  ↳ norma · [rfc-editor.org](https://rfc-editor.org/rfc/rfc7296) ✅

## [199 — Transit Gateway, Virtual WAN y Network Connectivity Center](../../classes/part-16-advanced-cloud-networking-edge/199-transit-gateway-virtual-wan-y-network-connectivity-center/README.md)

- **AWS (2025), *Transit Gateway route tables and segmentation*** — segmentación del tránsito mediante tablas de ruta<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) ✅
- **Microsoft (2025), *Virtual WAN architecture and routing*** — el servicio equivalente gestionado en Azure<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about) ✅
- **Google Cloud (2025), *Network Connectivity Center*** — el servicio equivalente en Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/network-connectivity/docs/network-connectivity-center) ✅
- **AWS (2025), *Building a scalable and secure multi-VPC network infrastructure*** — patrón de referencia para interconectar muchas VPC<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) ✅
- **Microsoft (2025), *Cloud Adoption Framework: network topology and connectivity*** — criterios de topología de red en la adopción<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/network-topology-and-connectivity) ✅

## [200 — Private endpoints, service networking y egress control](../../classes/part-16-advanced-cloud-networking-edge/200-private-endpoints-service-networking-y-egress-control/README.md)

- **AWS (2025), *Building a data perimeter on AWS*** — perímetro de datos frente a la salida no autorizada<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) ✅
- **AWS (2025), *VPC endpoints and endpoint policies*** — acceso privado a servicios y política del punto de enlace<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) ✅
- **Microsoft (2025), *Azure Private Link and private endpoints*** — el mecanismo equivalente en Azure<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) ✅
- **Google Cloud (2025), *VPC Service Controls*** — perímetros de servicio<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc-service-controls/docs/overview) ✅
- **MITRE ATT&CK (2025), *Exfiltration over alternative protocol*** — la técnica de exfiltración que el control de egreso debe cortar<br>  ↳ documentación · [attack.mitre.org](https://attack.mitre.org/tactics/TA0010) ✅

## [201 — Service mesh, mTLS y gestión de tráfico este-oeste](../../classes/part-16-advanced-cloud-networking-edge/201-service-mesh-mtls-y-gestion-de-trafico-este-oeste/README.md)

- **Istio (2025), *Security: mutual TLS and authorization policies*** — mTLS y políticas de autorización entre servicios<br>  ↳ documentación · [istio.io](https://istio.io/latest/docs/concepts/security) ✅
- **Linkerd (2025), *Architecture and performance*** — coste en latencia y recursos del plano de datos<br>  ↳ documentación · [linkerd.io](https://linkerd.io/2/reference/architecture) ✅
- **SPIFFE (2025), *Workload identity specification*** — identidad de carga de trabajo verificable<br>  ↳ documentación · [spiffe.io](https://spiffe.io/docs/latest/spiffe-about/overview) ✅
- **Cilium (2025), *Service mesh without sidecars*** — alternativa sin sidecar y sus límites<br>  ↳ documentación · [cilium.io](https://cilium.io/use-cases/service-mesh) ✅
- **Google (2016), *SRE Book: addressing cascading failures*** — reintentos y presupuestos<br>  ↳ documentación · [sre.google](https://sre.google/sre-book/addressing-cascading-failures) ✅

## [202 — eBPF, flow logs, packet capture y diagnóstico](../../classes/part-16-advanced-cloud-networking-edge/202-ebpf-flow-logs-packet-capture-y-diagnostico/README.md)

- **AWS (2025), *VPC Flow Logs*** — campos, acciones y limitaciones<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) ✅
- **Cilium (2025), *Hubble: eBPF-based network observability*** — observabilidad de red sin modificar la aplicación<br>  ↳ documentación · [docs.cilium.io](https://docs.cilium.io/en/stable/overview/intro) ✅
- **Gregg (2019), *BPF Performance Tools*** — herramientas de diagnóstico basadas en eBPF<br>  ↳ documentación · [brendangregg.com](https://brendangregg.com/bpf-performance-tools-book.html) ✅
- **Wireshark (2025), *TCP analysis flags: retransmissions, zero window, resets*** — las señales de TCP que identifican la causa del problema<br>  ↳ documentación · [wireshark.org](https://wireshark.org/docs/wsug_html_chunked/ChAdvTCPAnalysis.html) ✅
- **Google Cloud (2025), *Packet Mirroring and network diagnostics*** — captura de tráfico para diagnóstico en Google Cloud<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/vpc/docs/packet-mirroring) ✅

## [203 — SD-WAN, 5G, IoT y operación desconectada](../../classes/part-16-advanced-cloud-networking-edge/203-sd-wan-5g-iot-y-operacion-desconectada/README.md)

- **Cisco (2025), *SD-WAN design guide*** — política central y selección de camino por aplicación<br>  ↳ documentación · [cisco.com](https://cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/index.html) ✅
- **3GPP (2025), *5G network slicing overview*** — segmentación de la red móvil por requisito de servicio<br>  ↳ documentación · [3gpp.org](https://3gpp.org/technologies/5g-system-overview) ✅
- **AWS (2025), *IoT Greengrass: local processing and offline operation*** — procesamiento local cuando no hay enlace disponible<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) ✅
- **Shapiro et al. (2011), *Conflict-free replicated data types*** — convergencia del estado tras la reconexión<br>  ↳ documentación · [inria.hal.science](https://inria.hal.science/inria-00609399) ✅
- **Microsoft (2025), *Azure IoT Edge deployment and safe rollout*** — despliegue progresivo y seguro en el borde<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/iot-edge/about-iot-edge) ✅

## [204 — Proyecto: red multi-región y multi-cloud](../../classes/part-16-advanced-cloud-networking-edge/204-proyecto-red-multi-region-y-multi-cloud/README.md)

- **AWS (2025), *Building a scalable and secure multi-VPC network infrastructure*** — referencia para la topología de red del proyecto<br>  ↳ documentación · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) ✅
- **Microsoft (2025), *Cloud Adoption Framework: network topology and connectivity*** — criterios de conectividad aplicados al diseño<br>  ↳ documentación · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/network-topology-and-connectivity) ✅
- **Google Cloud (2025), *Network design decisions in the Architecture Framework*** — decisiones de red del marco de arquitectura<br>  ↳ documentación · [cloud.google.com](https://cloud.google.com/architecture/framework) ✅
- **Beyer et al. (2018), *The Site Reliability Workbook*** — verificación con pruebas reales<br>  ↳ documentación · [sre.google](https://sre.google/workbook/table-of-contents) ✅
- **NIST SP 800-207 (2020), *Zero Trust Architecture*** — el criterio de confianza cero aplicado a la interconexión<br>  ↳ norma · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/207/final) ✅
