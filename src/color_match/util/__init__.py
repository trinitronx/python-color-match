"""Color utility functions."""

print(f"{__file__} imported")
from numpy import __version__ as numpy_version

if numpy_version >= '2.0':
  from .monkeypatch import numpy_asscalar

from . import color

