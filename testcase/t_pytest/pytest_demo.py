
import pytest

def func(x):
    return x+1


def test_a():
    print("------test_a------")
    assert func(3) == 5


def test_b():
    print("------test_b------")
    assert 1


if __name__ == '__main__':
    pytest.main(["-s","pytest_demo.py"])