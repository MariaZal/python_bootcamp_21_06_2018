from mathematica.algebra.matrices import add_matrices, sub_matrices


def test_add_matriece():
    a = [[1, 2, 3], [1, 2, 3]]
    b = [[1, 2, 3], [1, 2, 3]]
    result = add_matrices(a, b)
    expected = [[2, 4, 9], [2, 4, 9]]
    result == expected


def test_sub_matriece():
    a = [[1, 2, 3], [1, 2, 3]]
    b = [[1, 2, 3], [1, 2, 3]]
    result = sub_matrices(a, b)
    expected = [[0, 0, 0], [0, 0, 0]]
    result == expected
