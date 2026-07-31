# Runbook del programa

| Evento | Diagnóstico | Recuperación |
|---|---|---|
| Generación difiere | ejecutar generadores y `git diff` | corregir fuente canónica |
| Portal inválido | `python scripts/validate_site.py` | regenerar y revisar enlaces |
| CloudShop no está ready | revisar puerto y logs JSON | reiniciar proceso/contenedor |
| Sandbox dejó recursos | inventario por etiquetas | ejecutar `cloud_lab.py destroy` y verificar factura |
| Dependencia vulnerable | revisar advisory y alcance | actualizar, probar y publicar parche |
