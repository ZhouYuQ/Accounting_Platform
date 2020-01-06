import pytest

class TestDemo:

    data_list = [("xiaoming","123456"),("xiaohong","123456")]

    @pytest.mark.parametrize(("name","password"),data_list)
    def test_a(self,name,password):
        print("test_a")
        print(name,password)
        assert 1


if __name__ == '__main__':
    pytest.main(["-s","pytest_two.py"])