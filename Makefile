format:
	venv/bin/yapf -i *.py bios_pnp/*.py

lint:
	venv/bin/pylint -rn *.py bios_pnp

test:
	venv/bin/python test.py

release: lint test
	rm -fr dist/
	venv/bin/python setup.py sdist bdist_wheel
	venv/bin/twine upload dist/*

.PHONY: format lint test
