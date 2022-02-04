# Test Calculate Coordinates
import pytest


@pytest.mark.parametrize("m, b, x1, expected", [
    (2, 1, 0, 1),
    (2, 1, 4, 9),
    (2, 1, -5, -9),
    (-2, -3, 0, -3),
    (-2, -3, 5, -13),
    (-2, -3, -9, 15),
    ])
def test_calc_coord(m, b, x1, expected):
    from calc_coord import y_coord_out
    answer = y_coord_out(m, b, x1)
    assert answer == expected
