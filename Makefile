rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))

files = test $(call rwildcard,src,*.py)
test_files = *

package = color_match

# For local development
test:
	pytest -s -v test/test_$(test_files).py --doctest-modules --cov $(package) --cov-config=.coveragerc --cov-report term-missing

# For github actions
test-ci:
	pytest -s -v test/test_$(test_files).py --doctest-modules --cov $(package) --cov-config=.coveragerc --cov-report=xml

lint:
	@echo "Running ruff..."
	@ruff check $(files)
	@echo "Running mypy..."
	@mypy $(files)

fix:
	ruff check --fix $(files)

install:
	pip install -U --editable .
	which pyenv && pyenv rehash

install-test:
	pip install -U --editable .[test]
	which pyenv && pyenv rehash

install-all:
	pip install -U --editable .[test,doc]
	which pyenv && pyenv rehash

report:
	codecov

build:
	rm -rf dist
	python -m build

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

.PHONY: test build
