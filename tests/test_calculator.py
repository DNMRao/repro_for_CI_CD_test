from src.calculator import add, subtract


def test_add():
    assert add(1, 3) == 4
    assert add(-2, 2) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4
