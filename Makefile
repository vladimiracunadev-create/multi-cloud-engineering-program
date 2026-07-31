.PHONY: install generate validate test site cloudshop
install:
	python -m pip install -e ".[site]"
generate:
	python scripts/generate_course.py
	python scripts/generate_site.py
validate:
	python scripts/validate_repository.py --strict
	python scripts/validate_site.py
test:
	python -m unittest discover -s tests -v
site:
	python -m http.server 8080
cloudshop:
	python projects/cloudshop/app.py
