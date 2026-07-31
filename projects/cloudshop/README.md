# CloudShop

Aplicación de referencia acumulativa del programa. Expone salud, preparación y pedidos con
logs JSON, IDs de correlación, validación de entrada y una imagen sin privilegios.

```bash
python projects/cloudshop/app.py
curl http://localhost:8080/health/ready
docker compose up --build
```

Cada parte agrega una capacidad y conserva evidencia en `evidence/`: arquitectura, red,
identidad, datos, entrega, observabilidad, resiliencia, costo y recuperación.
