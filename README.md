# Python Color Match

Python Color Match is a library designed to help you compare and match colors
using the CIE 2000 Delta E formula. It provides a command-line utility to
calculate the perceived difference between target colors and find the closest
matches from a provided palette.

## Features

- **Delta E Calculation**: Uses the CIE 2000 Delta E formula to compute the
  perceptual difference between two colors.
- **Hex Color Support**: Accepts hex color strings as input, making it easy to
  integrate with web or graphic design workflows.
- **Palette Matching**: Finds the closest color matches from a palette of
  user-provided colors.
- **CLI Interface**: Includes a command-line interface for quick and easy batch
  color matching.
- **Unit Tests**: Comprehensive test coverage to ensure correctness and
  reliability.

## Installation

The command-line utility is currently available in pre-release or beta status.
To install the library, clone the repository and install the dependencies:

```bash
git clone https://github.com/trinitronx/python-color-match.git
cd python-color-match
pip install .
```

## Usage

### CLI Usage

Run the CLI to match colors from two files (one containing target colors and the
other containing the palette):

```bash
python -m color_match target_colors.txt palette_colors.txt
```

Example output:

```text
Target colors: ['#eb0028']
Palette colors: ['#cd3f45', '#d70000', '#ff0000', '#c70039', '#ff5733']
Closest matches for #eb0028:
  #cd3f45 with Delta E: 7.03
  #d70000 with Delta E: 7.35
  #ff0000 with Delta E: 7.78
  #c70039 with Delta E: 10.44
  #ff5733 with Delta E: 12.45
Color matching completed successfully.
```

### Library Usage

While this project is primarily designed as a CLI utility, it's possible to use
the library in your Python code:

```python
from color_match.util.color import calculate_delta_e

delta_e = calculate_delta_e("#eb0028", "#d70000")
print(f"Delta E: {delta_e:.2f}")
```

Currently, this is a convenience wrapper around the `colormath2` library, which
provides many more color math functions.

## Development

The project includes a `Makefile` with targets for dependency installation,
testing, build, and release.

### Install Dependencies

It's recommended to use a `virtualenv` tool such as `pyenv-virtualenv`,
`virtualenvwrapper`, `venv`, `conda`, or similar.  Instructions for using such a
tool is outside the scope of this documentation, so refer to the chosen tool's
docs for that prerequisite.  To install this project's dependencies & module in
[editable / development mode][2]:

```bash
make install-dev
```

This installs both `test` and `build` dependencies along with the module.

Alternatively, the `build` and `test` dependencies can be installed separately,
but still alongside the module with:

- `make install-build`, or
- `make install-test`

An `install` target also exists that installs just the module in editable
development mode.  The `install-*` targets are setup to depend on this one.

### Testing

Run the tests to verify the functionality:

```bash
make test
```

To run the tests in CI mode and generate an XML code coverage report:

```bash
make test-ci
```

To just run the `codecov` tool:

```bash
make report
```

Run the linter tools (`ruff`, `mypy`) with the `lint` target:

```bash
make lint
```

There is also a `fix` target to automatically fix all supported style warnings
from the Ruff linter:

```bash
make fix
```

To build a source distribution & wheel:

```bash
make build
```

To publish via `twine`:

```bash
make publish
```

To clean up build files:

```bash
make clean
```

Finally, there are some targets to build the C sub-project test fixtures:

- `make test-fixtures`: Just builds the sub-project with `meson` & `ninja`
- `make test-fixtures-install`: Installs the built binaries into
  `test/fixtures/bin` for use in development.

### Project Structure

This project uses the [`src` layout][1] structure.  Tests are located under
`test`, and the python module's code is located under `src`:

```text
 LICENSE
 Makefile
 pyproject.toml
󰂺 README.md
 src/
└──  color_match/
    ├──  __init__.py
    ├──  __main__.py
    ├──  color_match.py
    └──  util/
        ├──  __init__.py
        ├──  color.py
        └──  monkeypatch/
            └──  numpy_asscalar.py
 test/
├──  fixtures/
│   ├── 󰝴 build.ninja
│   ├──  foot-default-colors.c
│   ├──  foot-extra-theme-manjaro-sway-default-256color-palette.txt
│   ├──  Makefile
│   ├──  meson.build
│   └──  print-xterm-256-colors.c
├──  test_color_match.py
└──  util/
    └──  color_test.py
```

The sub-project under `test/fixtures` provides some examples for hexidecimal
color palette generation for `xterm-256color` terminals, and an example terminal
theme file.  These are currently unused in the test cases, but are provided as
examples for hex color file input for the `color_matcher` CLI.  They are not
included in the built & distributed wheel, but are included in the source
distribution for development purposes.

### Dependencies

- **colormath2**: For color space conversions and Delta E calculations.
- **numpy**: For numerical operations (used indirectly via `colormath2`).
- **pytest**: For running unit tests.

### License

This project is licensed under the [AGPLv3 License](LICENSE).

---

Feel free to contribute!

[1]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[2]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html
