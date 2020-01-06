import pytest

def test_1():
    a = True
    assert a

def test_2():
    a = True
    assert not a

if __name__ == '__main__':
    pytest.main(["pytest_assert.py"])
