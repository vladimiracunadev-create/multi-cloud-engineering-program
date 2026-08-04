# Changelog

## 2.2.0 — 2026-08-04

- **diagramas visibles en las tres superficies**: los 291 diagramas se
  pre-renderizan a SVG y PNG en el build. Antes el manual los imprimia como
  texto Mermaid y la aplicacion Android los dejaba en blanco, porque se traian
  de un CDN y no hay red; ahora no dependen de JavaScript ni de la red;
- **manuales divididos**: 24 cuadernos por parte y 3 por nube —AWS, Azure y
  Google Cloud—, generados por el mismo generador y desde las mismas fuentes;
- cada clase y cada parte enlazan su PDF desde el README y desde el portal, y
  el panel tiene una seccion de descargas con los 28 documentos;
- manual integral de 2.883 paginas, con los diagramas dentro;
- dependencias de generacion al dia: reportlab 5.0.0 y pypdf 6.14.2, ambas
  comprobadas contra el recuento de paginas antes de adoptarlas.

## 2.1.0 — 2026-08-04

- las 288 clases con contenido propio: cerradas las partes 21, 22 y 23;
- manual integral regenerado a 2.883 páginas desde las 607 fuentes;
- aplicación Android: APK firmada de 4,0 MiB que empaqueta el curso entero y
  funciona sin conexión, construida sin Gradle con las herramientas del SDK;
- navegación anterior/siguiente en las páginas de clase y parte, en el README de
  cada clase y con las flechas del teclado;
- las páginas de parte reescriben sus enlaces al sitio publicado: 358 enlaces
  rotos corregidos y verificación de enlaces sin fallos.

## 2.0.0 — 2026-07-31

- 24 partes, 288 clases y arquitectura de sistemas como dominio explícito;
- rutas productivas AWS, Azure y Google Cloud, apoyadas por 27 casos AWS auditados;
- CloudShop ejecutable, Docker, Kubernetes, Terraform y sandboxes con costo bloqueado;
- diagnóstico, checkpoints, banco por escenarios, exámenes por rol y kits académicos;
- aplicaciones web/móvil PWA y escritorio, ADRs, threat models, rutas profesionales y releases;
- gobierno comunitario, doble licencia, Dependabot, SBOM y validación ampliada.

## 1.1.0 — 2026-07-31

- portal rediseñado como experiencia educativa completa y responsive;
- 180 páginas de clase y 15 páginas de parte generadas desde el currículo;
- rutas profesionales, roadmap, búsqueda, favoritos, progreso y analítica visual;
- PWA, SEO, Open Graph, sitemap, robots y página 404;
- CI multi-OS/Python, auditoría de seguridad, CodeQL y despliegue de GitHub Pages;
- documentación de contribución, política de seguridad y metadatos About ampliados.

## 1.0.0 — 2026-07-31

- reconstrucción completa basada en los repositorios pedagógicos correctos del autor;
- 15 partes y 180 clases secuenciales;
- contrato uniforme de teoría, evaluación, metadatos y laboratorio;
- motor de laboratorios determinista, CLI, pruebas y validación estricta;
- rutas por rol, syllabus, metodología, rúbrica, bibliografía y CloudShop capstone;
- portal de estudio con búsqueda, filtros y progreso local.
