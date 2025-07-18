rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))

files = test $(call rwildcard,src,*.py)
test_files = *

package = color_match

# For local development
test:
	pytest -s -v

# For github actions
test-ci:
	pytest -s -v --cov-report=xml

test-fixtures:
	make -C test/fixtures

test-fixtures-install:
	make -C test/fixtures install

lint:
	@echo "Running ruff..."
	@ruff check $(files)
	@echo "Running mypy..."
	@mypy $(files)

fix:
	ruff check --fix $(files)

install:
	pip install -U --editable .
	which pyenv >/dev/null 2>&1 && pyenv rehash

INSTALL_GROUP_TARGETS = install-build install-test install-dev

$(INSTALL_GROUP_TARGETS): | install
install-%:
	pip install --group $*
	which pyenv >/dev/null 2>&1 && pyenv rehash

report:
	codecov

build:
	rm -rf dist
	python -m build --sdist --wheel

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

clean::
	rm -rf dist
	rm -rf src/*.egg-info
	make -C test/fixtures clean

.PHONY: test test-cli build clean lint fix install $(INSTALL_GROUP_TARGETS) report publish
