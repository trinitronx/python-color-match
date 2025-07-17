# -*- coding: utf-8 -*-
"""Main entry point for the color match library."""

from .util.color import calculate_delta_e


def main(target_colors_file: str, palette_colors_file: str) -> int:
    """
    Main function to run the color match process.

    Args:
        target_colors_file (str): Path to the file containing target colors.
        palette_colors_file (str): Path to the file containing palette colors.
    Returns:
        int: Exit code, 0 for success, 1 for failure.
    """
    print(
        f"This is only printed when running {__file__} directly, because the __name__ is {__name__}"
    )
    with open(target_colors_file, "r") as target_file:
        target_colors = target_file.read().strip().splitlines()
    with open(palette_colors_file, "r") as palette_file:
        palette_colors = palette_file.read().strip().splitlines()

    if not target_colors or not palette_colors:
        print("No colors found in one of the files.")
        return 1
    else:
        print(f"Target colors: {target_colors}")
        print(f"Palette colors: {palette_colors}")
        for target_hex in target_colors:
            results = []
            for possible_hex in palette_colors:
                delta_e = calculate_delta_e(target_hex, possible_hex)
                results.append((possible_hex, delta_e))
            results.sort(key=lambda x: x[1])  # Sort by Delta E value
            print(f"Closest matches for {target_hex}:")
            for color, delta_e in results[:5]:  # Show top 5 matches
                print(f"  {color} with Delta E: {delta_e:.2f}")
        print("Color matching completed successfully.")
        return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m color_match <arg1> <arg2>")
        exit(1)
    else:
        target_colors_file = sys.argv[1]
        palette_colors_file = sys.argv[2]
        print(f"Arguments received: {arg1}, {arg2}")
        main(target_colors_file, palette_colors_file)
        exit(0)
