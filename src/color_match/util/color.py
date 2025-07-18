# -*- coding: utf-8 -*-
"""Utility functions for color manipulation and calculations."""

from colormath2.color_conversions import convert_color
from colormath2.color_diff import delta_e_cie2000
from colormath2.color_objects import LabColor, sRGBColor


def hex_to_rgb(hex_color: str) -> sRGBColor:
    """
    Convert a hex color string to an sRGBColor object.

    Args:
        hex_color (str): Hex color string, e.g., "#eb0028".
    Returns:
        sRGBColor: An sRGBColor object representing the color.
    """
    hex_color = hex_color.lstrip("#")
    rgb_tuple = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return sRGBColor(*rgb_tuple, is_upscaled=True)


def rgb_to_lab(rgb_color: sRGBColor) -> LabColor:
    """
    Convert an sRGBColor object to a LabColor object.

    Args:
        rgb_color (sRGBColor): An sRGBColor object.
    Returns:
        LabColor: A LabColor object representing the color.
    """
    return convert_color(rgb_color, LabColor)


def calculate_delta_e(target_hex: str, possible_hex: str) -> float:
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
    delta_e = delta_e_cie2000(target_lab, possible_lab)
    return delta_e
