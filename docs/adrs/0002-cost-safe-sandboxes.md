# ADR 0002: sandboxes con costo bloqueado por defecto

**Estado:** aceptado. **Decisión:** `deploy` exige `CLOUD_LAB_ALLOW_COST=1`; plan, verificación y
destroy siguen disponibles. Toda práctica real requiere identidad temporal, presupuesto, etiquetas
y expiración. **Consecuencia:** existe fricción intencional antes de crear recursos pagos.
