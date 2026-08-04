# Arquitectura del sistema pedagógico

```mermaid
flowchart TB
  Source["Fuente curricular: 24 partes"] --> Generator["Generadores y validadores"]
  Generator --> Lessons["288 clases y evaluaciones"]
  Generator --> Portal["PWA y páginas de clase"]
  Generator --> Manual["Manuales PDF: integral, por parte y por nube"]
  Portal --> Apk["APK Android con el sitio empaquetado"]
  Lessons --> Labs["Motores de práctica por dominio"]
  Labs --> Local["CloudShop local"]
  Labs --> Sandbox["AWS / Azure / GCP con cost gate"]
  Local --> Evidence["Evidencia, checkpoints y certificados"]
  Sandbox --> Evidence
```

La arquitectura de aprendizaje usa una sola fuente versionada, salidas regenerables y una
frontera explícita entre práctica local, sandbox autorizado y producción.
