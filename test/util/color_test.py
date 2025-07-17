# -*- coding: utf-8 -*-
"""Unit tests for color utility functions."""

from colormath.color_objects import BaseRGBColor, ColorBase, sRGBColor
from pytest import approx

from color_match.util.color import (  # Adjust the import if needed
    calculate_delta_e,
    hex_to_rgb,
)


class BaseRGBColor(ColorBase):
    def __eq__(self, other):
        if not isinstance(other, sRGBColor):
            return NotImplemented
        print(f"Comparing {self} with {other}")
        print(f"self.rgb_r: {self.rgb_r}, other.rgb_r: {other.rgb_r}")
        print(f"self.rgb_g: {self.rgb_g}, other.rgb_g: {other.rgb_g}")
        print(f"self.rgb_b: {self.rgb_b}, other.rgb_b: {other.rgb_b}")
        print(
            f"self.is_upscaled: {self.is_upscaled}, other.is_upscaled: {other.is_upscaled}"
        )
        return (
            self.rgb_r == other.rgb_r
            and self.rgb_g == other.rgb_g
            and self.rgb_b == other.rgb_b
            and self.is_upscaled == other.is_upscaled
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
    print(f"sRGBColor.__eq__: {result.__eq__}")
    assert isinstance(result, sRGBColor)
    assert result == sRGBColor(235, 0, 40, is_upscaled=True)
