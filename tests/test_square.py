from src import square

def test_square():
    x = 2
    ans = square.square(x)
    assert ans == 4
