import pytest

class TestFunc:
    def setup(self):
        print("------setup----")

    def teardown(self):
        print("======teardown======")

    def test_a(self):
        print("test_a")


    def test_b(self):
        print("test_b")


if __name__ == '__main__':
    pytest.main(["-s","pytest_func.py"])
