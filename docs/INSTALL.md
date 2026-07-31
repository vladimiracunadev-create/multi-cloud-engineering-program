# Instalación

Requisitos: Python 3.11+, Git y opcionalmente Docker/Terraform. Ejecuta `python -m pip install -e ".[site]"`,
`python scripts/validate_repository.py --strict` y `python -m unittest discover -s tests -v`.
Para el entorno completo usa `docker compose up --build` o abre el devcontainer.
