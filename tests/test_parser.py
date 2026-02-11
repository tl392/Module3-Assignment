import pytest
from app.parser import InputParser


@pytest.mark.parametrize("text", ["q", "Q", " quit ", "EXIT", "exit"])
def test_is_quit_positive(text):
    assert InputParser.is_quit(text) is True


@pytest.mark.parametrize("text", ["qq", "quite", "+", "1", ""])
def test_is_quit_negative(text):
    assert InputParser.is_quit(text) is False


@pytest.mark.parametrize("raw,expected", [
    ("+", "+"),
    ("  +  ", "+"),
    ("-", "-"),
    ("*", "*"),
    ("/", "/"),
    ("x", "x"),     # parser does not validate supported operators; Calculator does
])
def test_parse_operator_positive(raw, expected):
    assert InputParser.parse_operator(raw) == expected


@pytest.mark.parametrize("raw", ["", "   "])
def test_parse_operator_negative_empty(raw):
    with pytest.raises(ValueError, match="Operator cannot be empty"):
        InputParser.parse_operator(raw)


@pytest.mark.parametrize("raw", ["q", "quit", "exit", " EXIT "])
def test_parse_operator_negative_quit(raw):
    with pytest.raises(InputParser.QuitCalculator):
        InputParser.parse_operator(raw)


@pytest.mark.parametrize("raw,expected", [
    ("1", 1.0),
    (" 2.5 ", 2.5),
    ("-3", -3.0),
    ("0", 0.0),
])
def test_parse_number_positive(raw, expected):
    assert InputParser.parse_number(raw) == expected


@pytest.mark.parametrize("raw", ["abc", "1,2", "--", "two", ""])
def test_parse_number_negative_invalid(raw):
    with pytest.raises(ValueError, match="Invalid number"):
        InputParser.parse_number(raw)


@pytest.mark.parametrize("raw", ["q", "quit", "exit", " q "])
def test_parse_number_negative_quit(raw):
    with pytest.raises(InputParser.QuitCalculator):
        InputParser.parse_number(raw)
