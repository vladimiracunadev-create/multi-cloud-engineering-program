# Investigación de repositorios pedagógicos base

## Alcance corregido

Este programa no se basó en repositorios técnicos generales del autor. Se reconstruyó a
partir de cuatro repositorios cuyo propósito explícito es enseñar mediante un recorrido
completo y verificable:

1. [Artificial Intelligence Evolution Program](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program)
2. [Blockchain Learning Path](https://github.com/vladimiracunadev-create/blockchain-learning-path)
3. [Python Data Science Program](https://github.com/vladimiracunadev-create/python-data-science-program)
4. [Modern Cybersecurity Program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program)

La revisión se hizo sobre sus README, índices, clases o módulos de muestra, metodología
docente, syllabus, rúbricas, rutas, contratos de clase y superficies de producto.

## Patrones observados y adaptación

| Patrón común | Evidencia observada | Aplicación en este programa |
|---|---|---|
| Progresión exhaustiva | 180 clases de IA, 232 de Data Science y 340 de ciberseguridad | 288 clases continuas en 24 partes |
| Contrato pedagógico | Objetivos, resultados, teoría, práctica, errores y referencias | Contrato obligatorio validado en cada README |
| Evidencia ejecutable | Notebooks, labs y entrypoints reutilizables | 180 `lab.py` sobre un motor determinista común |
| Evaluación objetiva | Retos y criterios de aceptación | `assessment.md` por clase y rúbrica transversal |
| Pauta bibliográfica | Libros por área y fuentes primarias | Bibliografía por parte y mapa libro → clases |
| Navegación | Índices por parte y enlaces anterior/siguiente | Navegación generada desde catálogo canónico |
| Varias audiencias | Alumno, docente, evaluador, institución | Guía docente, syllabus, rutas y arquitectura |
| Producto verificable | CLI, sitio, manual, apps y CI según el repo | CLI, portal, catálogo JSON, tests y CI |
| Honestidad de madurez | Estado verificable y límites explícitos | Simulación separada de validación cloud real |
| Proyecto acumulativo | Capstones y portafolio | CloudShop progresa en las 24 partes |

## Decisiones tomadas

Se eligieron 24 partes de 12 clases para conservar una progresión suficientemente granular
sin convertir cada servicio del proveedor en una clase aislada. Las partes 02–04 ofrecen
profundidad simétrica en AWS, Azure y Google Cloud. Desde la parte 05 el currículo vuelve a
contratos portables: OCI, Kubernetes, Terraform, entrega, datos, SRE y gobierno.

El patrón del Artificial Intelligence Evolution Program inspiró el catálogo canónico,
metadatos `lesson.yaml` y motores didácticos compartidos. Blockchain Learning Path aportó el
modelo mental, el laboratorio guiado y el reto verificable. Python Data Science Program
aportó la metodología docente, las superficies por audiencia y el énfasis en producto
educativo. Modern Cybersecurity Program aportó la escala de evaluación, rutas por rol,
evidencia operacional y límites éticos explícitos.

## Qué no se copió

No se copiaron textos, código ni materiales protegidos de los repositorios. Se reutilizó el
patrón pedagógico y de producto, adaptándolo al dominio cloud con redacción, currículo,
laboratorios y arquitectura propios.
