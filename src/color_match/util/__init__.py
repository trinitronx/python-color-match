# -*- coding: utf-8 -*-
"""Color utility functions."""

from numpy import __version__ as numpy_version

if numpy_version >= "2.0":
    from .monkeypatch import numpy_asscalar as numpy_asscalar  # noqa F401

from . import color as color  # noqa F401
