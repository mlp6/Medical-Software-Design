from add import add
import pytest

def test_add_1():
    result = add(1, 2)
    assert result == 3

def test_add_2():
    result = add(2, 3)
    assert result == 5


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
])
def test_add_parametrize(a, b, expected):
    """
    test_add_parametrize is called with all of the input & expected output
    combinations specified in the decorator above.
    """
    assert add(a, b) == expected
    
