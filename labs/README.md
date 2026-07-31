# Laboratorios ejecutables

Cada una de las 288 clases incluye `lab.py`. Los entrypoints seleccionan una familia de
práctica en `src/multicloud_program/labs.py` y generan un contrato JSON 2.0 verificable.

## Por qué existe un núcleo local

- permite empezar sin tarjeta, créditos ni permisos empresariales;
- evita que una interfaz gráfica sustituya la comprensión del mecanismo;
- hace las evaluaciones reproducibles en Windows, macOS, Linux y CI;
- separa dominio conceptual de nombres comerciales;
- prepara la misma evidencia que luego debe obtenerse en un sandbox real.

## Ejecutar

```bash
python classes/part-00-foundations-computing-networking-linux/001-computacion-digital-y-modelo-mental-de-la-nube/lab.py
python classes/part-10-observability-sre-reliability/126-sli-slo-sla-y-presupuesto-de-error/lab.py --seed 42
```

La salida contiene `scenario`, `decision`, `evidence`, `cost_units`, `negative_test` y
`limitations`. La misma semilla debe producir exactamente el mismo resultado.

## Extensión a proveedor

1. Conserva el escenario y criterio de aceptación.
2. Implementa en una cuenta sandbox autorizada.
3. Usa identidad temporal y mínimo privilegio.
4. Define presupuesto y etiquetas antes de crear recursos.
5. Captura estado mediante API o CLI, no solo pantallas.
6. Ejecuta prueba negativa y recuperación.
7. Destruye recursos y verifica costo residual.

Un laboratorio cloud real no se marca aprobado hasta demostrar que no dejó recursos huérfanos.
