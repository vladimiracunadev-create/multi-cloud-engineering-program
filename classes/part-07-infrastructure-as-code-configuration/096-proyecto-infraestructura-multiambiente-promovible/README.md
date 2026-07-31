# 096 — Proyecto: infraestructura multiambiente promovible

> [← Clase anterior](../../part-07-infrastructure-as-code-configuration/095-plantillas-golden-paths-y-catalogo-interno/README.md) · [Índice de la parte](../README.md) · [Clase siguiente →](../../part-08-continuous-delivery-platform-engineering/097-integracion-continua-trunk-based-development-y-feedback/README.md)

**Parte:** 07 — Infraestructura como código y configuración<br>
**Nivel:** intermedio-avanzado · **Horas estimadas:** 8<br>
**Laboratorio:** `capstone` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender y aplicar **proyecto: infraestructura multiambiente promovible** dentro de una plataforma cloud realista,
produciendo evidencia reproducible y una decisión que explicite seguridad, confiabilidad,
costo y operación. La meta no es memorizar nombres de servicios: es reconocer el problema,
seleccionar una solución proporcional y demostrar qué ocurrió.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Explicar** proyecto: infraestructura multiambiente promovible con vocabulario independiente del proveedor.
2. **Relacionar** sus componentes con el modelo mental de la parte.
3. **Ejecutar** un laboratorio local determinista y leer su contrato JSON.
4. **Evaluar** al menos una alternativa y justificar el trade-off elegido.
5. **Entregar** `plataforma-iac` con evidencia, límites y criterio de reversión.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `proyecto` | Define su papel en **proyecto: infraestructura multiambiente promovible** y cómo observarlo en un sistema real. |
| `infraestructura` | Define su papel en **proyecto: infraestructura multiambiente promovible** y cómo observarlo en un sistema real. |
| `multiambiente` | Define su papel en **proyecto: infraestructura multiambiente promovible** y cómo observarlo en un sistema real. |
| `promovible` | Define su papel en **proyecto: infraestructura multiambiente promovible** y cómo observarlo en un sistema real. |

## 🧠 Modelo mental

IaC trata la infraestructura como producto versionado: el plan explica intención, el estado conecta intención y realidad, y la revisión reduce cambios accidentales.

Aplicado a esta clase, separa siempre cuatro planos: **intención** (qué necesita el usuario),
**configuración** (qué declaramos), **estado observado** (qué existe de verdad) y
**evidencia** (cómo sabemos que cumple). Confundirlos produce diseños que se ven correctos
en un diagrama pero fallan al operar.

## 🗺️ Flujo de razonamiento

```mermaid
flowchart LR
    A["Necesidad y restricciones"] --> B["Diseño: Proyecto: infraestructura multiambiente promovible"]
    B --> C["Implementación reproducible"]
    C --> D["Estado observado"]
    D --> E{"¿Cumple seguridad, SLO y costo?"}
    E -- "No" --> B
    E -- "Sí" --> F["Evidencia y decisión registrada"]
```

## 📖 Desarrollo

### 1. Del requisito al mecanismo

Empieza por una frase medible: quién consume la capacidad, bajo qué carga, desde dónde,
con qué datos y qué impacto tendría un fallo. Después identifica el mecanismo de esta clase
que satisface cada restricción. Un producto cloud solo es una implementación posible; el
requisito permanece aunque cambies de AWS a Azure, Google Cloud o infraestructura propia.

### 2. Fronteras y responsabilidades

Documenta quién administra identidad, red, datos, runtime y observabilidad. Marca qué queda
en manos del proveedor y qué sigue siendo responsabilidad del equipo. Cada frontera debe
tener propietario, interfaz, señal operativa y forma de recuperación. Si una responsabilidad
no tiene dueño, el diseño todavía está incompleto.

### 3. Compensaciones que deben quedar visibles

| Dimensión | Pregunta de diseño |
|---|---|
| Confiabilidad | ¿Qué falla, cómo se detecta y cuánto tarda en recuperarse? |
| Seguridad | ¿Qué identidad actúa y cuál es el mínimo privilegio necesario? |
| Costo | ¿Cuál es la unidad de consumo y qué hace crecer la factura? |
| Operación | ¿Qué señal permite diagnosticarlo sin entrar manualmente al servidor? |
| Portabilidad | ¿Qué contrato es estándar y qué decisión es específica del proveedor? |

La respuesta correcta puede ser más simple que la arquitectura inicialmente imaginada. En
cloud, complejidad también consume presupuesto de error, tiempo de equipo y capacidad de
respuesta a incidentes.

## 🔬 Ejemplo trabajado

Una plataforma de pedidos necesita aplicar **proyecto: infraestructura multiambiente promovible**. El equipo registra:

- demanda base de 20 solicitudes/s y pico de 120 solicitudes/s;
- SLO mensual de 99,9 % para operaciones de lectura;
- RPO de 15 minutos y RTO de 60 minutos;
- datos personales que no pueden salir de la región aprobada;
- presupuesto inicial de USD 600/mes.

La decisión se acepta solo si explica cómo la propuesta responde a esas cinco restricciones.
Se descarta cualquier alternativa que dependa de acceso administrativo permanente, no tenga
telemetría o cuyo costo no pueda atribuirse. El resultado esperado no es "usar servicio X",
sino una cadena trazable: requisito → mecanismo → prueba → señal → límite.

## 🧪 Laboratorio guiado

Ejecuta desde la raíz:

```bash
python classes/part-07-infrastructure-as-code-configuration/096-proyecto-infraestructura-multiambiente-promovible/lab.py
```

El laboratorio selecciona el motor de práctica **`capstone`** y produce
`lab_result.json`. El escenario, sus comprobaciones y el artefacto esperado corresponden a
esta clase; no requiere credenciales y deja explícito qué debe revalidarse en un sandbox real.

1. Lee `exercise.steps` y formula una predicción antes de ejecutar.
2. Ejecuta la práctica y verifica todos los elementos de `checks`.
3. Provoca el caso de `negative_test` y explica la señal observada.
4. Materializa `plataforma-iac` en `evidence/` usando la plantilla indicada.
5. Para proveedor real, sigue `sandbox.requires`, registra costo y ejecuta `destroy`.

### Evidencia esperada

El artefacto principal es un incremento integrado, demostrable y documentado. Además, la entrega debe incluir el comando ejecutado,
la salida estructurada y una conclusión que no exceda lo observado.

## 🏆 Reto verificable

Construye **`plataforma-iac`** para el caso CloudShop. Incluye una alternativa descartada,
un supuesto que pueda falsarse, una prueba de fallo y una decisión de rollback.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0 y genera JSON válido.
- [ ] La entrega conecta al menos tres requisitos con mecanismos verificables.
- [ ] Existe una prueba positiva y una prueba negativa con evidencia.
- [ ] Seguridad, costo y operación aparecen como decisiones, no como anexos.
- [ ] Se declara una limitación y una condición que obligaría a revisar el diseño.
- [ ] Otra persona puede repetir el recorrido sin conocimiento tácito.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El diseño enumera servicios pero no requisitos | Se comenzó por el catálogo del proveedor | Reescribe primero escenarios y restricciones medibles. |
| La demo funciona una vez y se declara lista | Se confundió ejecución con evidencia operacional | Añade repetición, fallo, telemetría y recuperación. |
| Todo tiene permisos administrativos | El laboratorio heredó credenciales humanas | Usa identidad de workload y prueba explícitamente la denegación. |
| No se puede explicar la factura | Faltan unidades y ownership de costo | Etiqueta, estima por unidad y define presupuesto o alerta. |
| La solución se llama multi-cloud pero replica todo | Portabilidad se confundió con duplicación | Define qué riesgo se mitiga y porta solo el contrato necesario. |

## 🛡️ Seguridad, ética y costo

Trabaja con cuentas propias o sandboxes autorizados. No publiques secretos, identificadores
reales ni datos personales. Antes de crear recursos pagos define presupuesto, etiquetas y
comando de destrucción; después verifica que no queden recursos huérfanos. Los ejemplos
locales enseñan contratos, pero no certifican cumplimiento ni disponibilidad de producción.

## ❓ Preguntas de comprobación

1. ¿Qué parte del diseño seguiría siendo válida en otro proveedor?
2. ¿Qué señal distinguiría saturación, fallo de dependencia y error de configuración?
3. ¿Cuál es la unidad de costo y quién puede actuar sobre ella?
4. ¿Qué permiso puede retirarse sin romper el caso de uso?
5. ¿Qué evidencia falta para afirmar que esto está listo para producción?

## 🔗 Referencias

- Infrastructure as Code — Kief Morris.
- Terraform: Up & Running — Yevgeniy Brikman.
- Ansible for DevOps — Jeff Geerling.
- Documentación oficial vigente del servicio implementado; registra URL y fecha de consulta.

---

> [Evaluación](assessment.md) · [Contrato de clase](lesson.yaml) · [Índice de la parte](../README.md)
