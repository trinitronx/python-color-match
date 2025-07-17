# -*- coding: utf-8 -*-
"""Unit tests for the color_match module."""

import sys
from io import StringIO
from unittest.mock import mock_open, patch

from color_match.__main__ import main

MOCKED_FILE_DATA = {
    "target_colors.txt": "#eb0028\n#ff5733\n#c70039\n#900c3f\n#eb0028",
    "palette_colors.txt": "#ff5733\n#c70039\n#900c3f\n#cd3f45\n#870000\n#af0000\n#d70000\n#ff0000",
    "non_existent.txt": None,  # Indicates a file that should raise FileNotFoundError
}


def custom_mock_open_file(filename, *args, **kwargs):
    """
    Custom side effect function for mock_open.
    Returns a mock_open object with specific data based on the filename.
    """
    if filename in MOCKED_FILE_DATA:
        if MOCKED_FILE_DATA[filename] is None:
            raise FileNotFoundError(f"No such file or directory: '{filename}'")
        mock_file = mock_open(read_data=MOCKED_FILE_DATA[filename])
        # If you need to mock line-by-line iteration, you can also set __iter__.return_value
        mock_file.return_value.__iter__.return_value = MOCKED_FILE_DATA[
            filename
        ].splitlines(True)
        return mock_file.return_value
    else:
        # For files not explicitly mocked, you could return a default mock_open
        # or raise an error if strict mocking is desired.
        return mock_open().return_value


@patch("builtins.open", side_effect=custom_mock_open_file)
def test_main(mock_open):
    """
    Test the main entry point of the color_match module.
    """
    # This test will run the main function of the color_match module
    # to ensure that it can be executed without errors.
    # It does not check for specific output or behavior, just that it runs.
    # with patch("builtins.open", mock_open(read_data=)):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        sys.argv = ["color_match", "target_colors.txt", "palette_colors.txt"]
        exit_code = main("target_colors.txt", "palette_colors.txt")
        output = fake_out.getvalue().strip()
        assert exit_code == 0
        assert (
            "Target colors: {}".format(
                MOCKED_FILE_DATA["target_colors.txt"].split("\n")
            )
            in output
        )
        assert (
            "Palette colors: {}".format(
                MOCKED_FILE_DATA["palette_colors.txt"].split("\n")
            )
            in output
        )
        expected = """Closest matches for #eb0028:
              #cd3f45 with Delta E: 7.03
              #d70000 with Delta E: 7.35
              #ff0000 with Delta E: 7.78
              #c70039 with Delta E: 10.44
              #ff5733 with Delta E: 12.45
            """.replace("\n              ", "\n  ").rstrip()  # indent adjust
        assert expected in output
        assert "Closest matches for #ff5733:\n  #ff5733 with Delta E: 0.00" in output
        assert "Closest matches for #c70039:\n  #c70039 with Delta E: 0.00" in output
        assert "Closest matches for #900c3f:\n  #900c3f with Delta E: 0.00" in output
