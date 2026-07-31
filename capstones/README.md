# CloudShop: proyecto integrador continuo

CloudShop es una plataforma de comercio electrónico deliberadamente pequeña. Su función es
obligar a integrar decisiones de identidad, red, cómputo, datos, entrega, operación y costo.

## Requisitos base

- catálogo y pedidos mediante API;
- datos personales restringidos a una región aprobada;
- 20 solicitudes/s base y 120 solicitudes/s de pico;
- SLO de lectura de 99,9 % mensual;
- RPO de 15 minutos y RTO de 60 minutos;
- presupuesto inicial de USD 600/mes;
- recuperación demostrable y acceso administrativo temporal.

## Hitos

| Parte | Incremento |
|---:|---|
| 00 | Servicio local reproducible |
| 01 | ADR de adopción y clasificación del workload |
| 02–04 | Implementaciones equivalentes por proveedor |
| 05 | Empaquetado OCI endurecido |
| 06 | Despliegue Kubernetes portable |
| 07 | Infraestructura multiambiente como código |
| 08 | Pipeline, promoción y rollback |
| 09 | Pedidos orientados a eventos |
| 10 | SLO, telemetría e incidente simulado |
| 11 | Guardrails, threat model y modelo de costos |
| 12 | Revisión de arquitectura y trade-offs |
| 13 | DR entre dos proveedores o nube híbrida |
| 14 | Defensa, portafolio y roadmap |

## Entrega final

El repositorio debe reconstruir la plataforma, mostrar una prueba de fallo y recuperación,
explicar costos por unidad, demostrar mínimo privilegio y contener un resumen ejecutivo de
dos páginas. La defensa dura 30 minutos: 10 de arquitectura, 10 de demostración y 10 de
preguntas adversariales.
