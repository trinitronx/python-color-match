from pytest import approx

from color_match.util.color import (  # Adjust the import if needed
    calculate_delta_e,
)


def test_calculate_delta_e():
    """
    Test the calculate_delta_e function from color_match module.
    """
    result = calculate_delta_e("#eb0028", "#d70000")
    assert isinstance(result, float)
    assert result == approx(7.345675004416438, rel=1e-2)
