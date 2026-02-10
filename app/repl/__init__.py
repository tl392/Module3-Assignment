"""
repl

This module implements the Read–Eval–Print Loop (REPL).

Responsibilities:
- Prompt the user
- Handle invalid input gracefully
- Coordinate between parser and calculator
"""

from __future__ import annotations

from app.calculator import Calculator
from app.parser import InputParser


class CalculatorREPL:
    """Read-Eval-Print Loop for the calculator."""

    @staticmethod
    def _prompt_until_valid(prompt: str, parse_fn):
        """
        Keep prompting until parse_fn accepts the input.
        - parse_fn raises ValueError for invalid input
        - QuitCalculator propagates upward to end the REPL
        """
        while True:
            raw = input(prompt)
            try:
                return parse_fn(raw)
            except ValueError as e:
                print(e)

    @classmethod
    def run(cls, calculator: Calculator) -> None:
        """Start the calculator REPL."""
        allowed = ", ".join(calculator.allowed_symbols())
        print(f"""Allowed ops: {allowed}
              1. Type any operations which mentiond above and hit enter 
              2. Type any number and hit enter
              3. Type any number again hit enter
              
              Type q to quit the calculator""")

        while True:
            try:
                symbol = cls._prompt_until_valid("Operation: ", InputParser.parse_operator)

                # Validate operator using the calculator (single source of truth)
                if symbol not in calculator.allowed_symbols():
                    allowed2 = ", ".join(calculator.allowed_symbols())
                    print(f"Unknown operator: {symbol!r}. Use one of: {allowed2}")
                    continue

                a = cls._prompt_until_valid("First number: ", InputParser.parse_number)
                b = cls._prompt_until_valid("Second number: ", InputParser.parse_number)

                try:
                    result = calculator.calculate(symbol, a, b)
                    print(f"Result: {result}")
                except ZeroDivisionError as e:
                    print(e)

            except InputParser.QuitCalculator:
                print("Goodbye!")
                return
