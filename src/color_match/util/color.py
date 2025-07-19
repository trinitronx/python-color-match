# -*- coding: utf-8 -*-
"""Utility functions for color manipulation and calculations."""

from basic_colormath.distance import get_delta_e_lab
from basic_colormath.distance import rgb_to_lab as convert_color_lab
from basic_colormath.type_hints import Hex, Lab, Rgb  # , RgbLike


def hex_to_rgb(hex_color: Hex) -> Rgb:
    """
    Convert a hex color string to an sRGBColor object.

    Args:
        hex_color (str): Hex color string, e.g., "#eb0028".
    Returns:
        sRGBColor: An sRGBColor object representing the color.
    """
    hex_color = hex_color.lstrip("#")
    r: float
    g: float
    b: float
    r, g, b = [float(int(hex_color[i : i + 2], 16)) for i in (0, 2, 4)]
    return (r, g, b)


def rgb_to_lab(rgb_color: Rgb) -> Lab:
    """
    Convert an sRGBColor object to a LabColor object.

    Args:
        rgb_color (sRGBColor): An sRGBColor object.
    Returns:
        LabColor: A LabColor object representing the color.
    """
    return convert_color_lab(rgb_color)


def calculate_delta_e(target_hex: Hex, possible_hex: Hex) -> float:
    """
    Calculate the Delta E (CIE 2000) between two hex color strings.

    Args:
        target_hex (str): Hex color string for the target color.
        possible_hex (str): Hex color string for the possible color match.
    Returns:
        float: The Delta E value between the two colors.
    """
    target_lab = rgb_to_lab(hex_to_rgb(target_hex))
    possible_lab = rgb_to_lab(hex_to_rgb(possible_hex))
    delta_e = get_delta_e_lab(target_lab, possible_lab)
    return delta_e
