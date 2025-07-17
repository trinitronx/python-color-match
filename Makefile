rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))

files = test $(call rwildcard,src,*.py)
test_files = *

# For local development
test:
	pytest -s -v test/test_$(test_files).py --doctest-modules --cov python_nftables_monitor --cov-config=.coveragerc --cov-report term-missing

# For github actions
test-ci:
	pytest -s -v test/test_$(test_files).py --doctest-modules --cov python_nftables_monitor --cov-config=.coveragerc --cov-report=xml

lint:
	@echo "Running ruff..."
	@ruff check $(files)
	@echo "Running mypy..."
	@mypy $(files)

fix:
	ruff check --fix $(files)

install:
	pip install -U --editable .

install-all:
	pip install -U --editable .[,doc]

report:
	codecov

build: python_nftables_monitor
	rm -rf dist
	python -m build

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

.PHONY: test build
