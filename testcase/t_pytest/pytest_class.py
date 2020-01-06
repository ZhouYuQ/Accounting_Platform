import pytest

class TestClass:
    def setup_class(self):
        print("------setup----")

    def teardown_class(self):
        print("======teardown======")

    def test_a(self):
        print("test_a")


    def test_b(self):
        print("test_b")


if __name__ == '__main__':
    pytest.main(["-s","pytest_class.py"])
