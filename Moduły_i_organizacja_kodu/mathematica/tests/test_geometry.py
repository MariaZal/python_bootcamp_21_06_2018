from mathematica.geometry.figures import triangle_area, square_area


def test_square():
    assert square_area(2) == 4
    assert square_area(3) == 9


def test_triangle():
    assert triangle_area(2, 2) == 2
    assert triangle_area(2, 3) == 3
