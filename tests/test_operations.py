import pytest
from app.operations import Add, Sub, Mul, Div


@pytest.mark.parametrize(
    "op,a,b,expected",
    [
        (Add(), 1, 2, 3),
        (Add(), -1, -2, -3),
        (Add(), 2.5, 0.5, 3.0),

        (Sub(), 5, 2, 3),
        (Sub(), 2, 5, -3),
        (Sub(), -2, -5, 3),

        (Mul(), 3, 2, 6),
        (Mul(), -3, 2, -6),
        (Mul(), 2.5, 2, 5.0),

        (Div(), 6, 2, 3),
        (Div(), 5, 2, 2.5),
        (Div(), -6, 2, -3),
    ],
)
def test_execute_positive(op, a, b, expected):
    assert op.execute(a, b) == expected


def test_div_negative_div_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        Div().execute(10, 0)
