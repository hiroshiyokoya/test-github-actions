import math_funcs


def test_square():
    x = 2
    ans = math_funcs.square(x)
    assert ans == 4


def test_square_root():
    x = 4
    ans = math_funcs.square_root(x)
    assert ans == 2


def test_cube():
    x = 2
    ans = math_funcs.cube(x)
    assert ans == 8
