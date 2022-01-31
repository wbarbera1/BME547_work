# Test Calculate Coordinates

def test_calc_coord():
    from calc_coord import y_coord_out
    answer = y_coord_out(5)
    assert answer == 2.5