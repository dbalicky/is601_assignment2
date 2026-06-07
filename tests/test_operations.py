import pytest
from app.operations import add, sub, mult, div

def test_addition():
    assert add(2,3) == 5

def test_subtraction():
    assert sub(5,2) == 3

def test_multiplication():
    assert mult(2,2) == 4

def test_division_positive():
    assert div(2,2) == 1

def test_division_by_zero():
    with pytest.raises(ValueError, match = "Division by zero is not allowed"):
        assert div(2,0)