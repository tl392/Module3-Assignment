"""
runner

Entry point for wiring together all components.
"""
from app.calculator import Calculator
from app.operations import Add, Sub, Mul, Div
from app.repl import CalculatorREPL


def start_calculator() -> None:
    calc = Calculator.from_operations([Add(), Sub(), Mul(), Div()])
    CalculatorREPL.run(calc)
