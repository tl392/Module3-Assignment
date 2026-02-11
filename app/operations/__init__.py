"""
operations

This module defines all supported arithmetic operations
using Object-Oriented Programming principles.

Each operation:
- Is its own class
- Implements a common interface (Operation)
- Encapsulates its own calculation logic

This design enables polymorphism and follows the
Open/Closed Principle (easy to add new operations).
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Operation(ABC):
    """
    Abstract base class for all calculator operations.

    Every concrete operation must:
    - Define a symbol (e.g. '+', '-', '*', '/')
    - Implement the execute() method
    """

    symbol: str
    name: str

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Run the operation and return the result."""
        raise NotImplementedError # pragma: no cover


class Add(Operation):
    """Concrete addition operation."""

    symbol = "+"
    name = "add"

    def execute(self, a: float, b: float) -> float:
        return a + b


class Sub(Operation):
    """Concrete subtraction operation."""

    symbol = "-"
    name = "subtract"

    def execute(self, a: float, b: float) -> float:
        return a - b


class Mul(Operation):
    """Concrete multiplication operation."""

    symbol = "*"
    name = "multiply"

    def execute(self, a: float, b: float) -> float:
        return a * b


class Div(Operation):
    """Concrete division operation."""

    symbol = "/"
    name = "divide"

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
