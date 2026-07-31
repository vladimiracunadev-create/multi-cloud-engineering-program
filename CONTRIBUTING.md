# Contribuir

## Flujo de trabajo

1. Crea una rama desde `main`.
2. Conserva el contrato de cada clase: `README.md`, `assessment.md`, `lesson.yaml` y `lab.py`.
3. Ejecuta las validaciones locales.
4. Abre un pull request con alcance, evidencia y riesgos conocidos.

```bash
python -m pip install -e ".[site]"
python scripts/validate_repository.py --strict
python scripts/generate_site.py
python scripts/validate_site.py
python -m unittest discover -s tests -v
```

Las contribuciones deben mantener la numeracion continua, la redaccion original, los labs
deterministas y la separacion explicita entre simulacion educativa y despliegue real.
