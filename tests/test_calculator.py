import pytest
from app.calculator import Calculator
from app.operations import Add, Sub, Mul, Div


def make_calc():
    return Calculator.from_operations([Add(), Sub(), Mul(), Div()])


@pytest.mark.parametrize(
    "op,a,b,expected",
    [
        ("+", 2, 3, 5),
        ("-", 10, 3, 7),
        ("*", 4, 2, 8),
        ("/", 9, 3, 3),
        ("/", 5, 2, 2.5),
    ],
)
def test_calculate_positive(op, a, b, expected):
    calc = make_calc()
    assert calc.calculate(op, a, b) == expected


def test_calculate_negative_unknown_operator():
    calc = make_calc()
    with pytest.raises(ValueError, match="Unknown operator"):
        calc.calculate("^", 1, 2)


def test_calculate_negative_div_by_zero():
    calc = make_calc()
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.calculate("/", 1, 0)


def test_allowed_symbols_positive_sorted():
    calc = make_calc()
    assert calc.allowed_symbols() == ("*", "+", "-", "/")
