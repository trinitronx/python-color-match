# -*- coding: utf-8 -*-
"""Utility functions for color manipulation and calculations."""

from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import LabColor, sRGBColor


def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip("#")
    rgb_tuple = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return sRGBColor(*rgb_tuple, is_upscaled=True)


def rgb_to_lab(rgb_color: sRGBColor):
    return convert_color(rgb_color, LabColor)


def calculate_delta_e(target_hex: str, possible_hex: str):
    target_lab = rgb_to_lab(hex_to_rgb(target_hex))
    possible_lab = rgb_to_lab(hex_to_rgb(possible_hex))
    delta_e = delta_e_cie2000(target_lab, possible_lab)
    return delta_e
