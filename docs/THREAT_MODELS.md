# Modelos de amenazas

| Superficie | Amenaza | Control | Evidencia |
|---|---|---|---|
| Portal | XSS/contenido manipulado | generación escapada, CSP en hosting | validación HTML |
| CI/CD | credencial persistente | OIDC, permisos mínimos, entornos | claims y logs |
| CloudShop | entrada maliciosa | validación, límites, usuario sin privilegios | tests y logs JSON |
| IaC | secretos/drift | escaneo, plan, estado aislado | SARIF y plan |
| Laboratorio | gasto o recurso huérfano | cost gate, TTL, etiquetas y destroy | reporte de inventario |
