# -*- coding: utf-8 -*-
"""Unit tests for color utility functions."""

from colormath2.color_objects import sRGBColor
from pytest import approx
from testfixtures import compare

from color_match.util.color import (  # Adjust the import if needed
    calculate_delta_e,
    hex_to_rgb,
)


def test_calculate_delta_e():
    """
    Test the calculate_delta_e function from color_match module.
    """
    result = calculate_delta_e("#eb0028", "#d70000")
    assert isinstance(result, float)
    assert result == approx(7.345675004416438, rel=1e-2)


def test_hex_to_rgb():
    """
    Test the hex_to_rgb function from color_match module.
    """

    result = hex_to_rgb("#eb0028")
    assert isinstance(result, sRGBColor)
    compare(
        result,
        sRGBColor(235, 0, 40, is_upscaled=True),
        normalize=True,
    )
