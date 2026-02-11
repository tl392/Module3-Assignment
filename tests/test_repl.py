import pytest
from app.calculator import Calculator
from app.operations import Add, Sub, Mul, Div
from app.repl import CalculatorREPL


def make_calc():
    return Calculator.from_operations([Add(), Sub(), Mul(), Div()])


def run_repl(monkeypatch, capsys, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(it))
    CalculatorREPL.run(make_calc())
    return capsys.readouterr().out


def test_repl_positive_quit_immediately(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["q"])
    assert "Allowed ops:" in out
    assert "Goodbye!" in out


def test_repl_positive_add_then_quit(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["+", "2", "3", "q"])
    assert "Result: 5.0" in out
    assert "Goodbye!" in out


def test_repl_negative_invalid_operator_then_valid(monkeypatch, capsys):
    # invalid op -> retry -> valid op -> complete -> quit
    out = run_repl(monkeypatch, capsys, ["x", "+", "1", "2", "q"])
    assert "Unknown operator" in out
    assert "Result: 3.0" in out


def test_repl_negative_empty_operator_then_valid(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["", "+", "1", "2", "q"])
    assert "Operator cannot be empty." in out
    assert "Result: 3.0" in out


def test_repl_negative_invalid_first_number_then_valid(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["+", "abc", "2", "3", "q"])
    assert "Invalid number" in out
    assert "Result: 5.0" in out


def test_repl_negative_invalid_second_number_then_valid(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["+", "2", "xyz", "3", "q"])
    assert "Invalid number" in out
    assert "Result: 5.0" in out


def test_repl_negative_div_by_zero(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["/", "10", "0", "q"])
    assert "Cannot divide by zero." in out
    assert "Goodbye!" in out


def test_repl_negative_quit_at_operator_prompt(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["quit"])
    assert "Goodbye!" in out


def test_repl_negative_quit_at_first_number_prompt(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["+", "q"])
    assert "Goodbye!" in out


def test_repl_negative_quit_at_second_number_prompt(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["+", "1", "exit"])
    assert "Goodbye!" in out
