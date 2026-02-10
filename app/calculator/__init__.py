"""
calculator

This module contains the Calculator class, which acts as the
core business-logic layer of the application.

Responsibilities:
- Store supported operations
- Validate operator symbols
- Delegate execution to the correct Operation object

"""

from __future__ import annotations
from typing import Iterable

from app.operations import Operation


class Calculator:
     """
    Calculator class responsible for performing calculations.

    It does NOT:
    - Handle user input
    - Print output

    It ONLY:
    - Maps symbols to Operation objects
    - Executes calculations
    """

    @classmethod
    def from_operations(cls, operations: Iterable[Operation]) -> "Calculator":
        """Create a Calculator from operation objects (no __init__)."""
        self = cls.__new__(cls)
        self._ops = {op.symbol: op for op in operations}
        return self

    def allowed_symbols(self) -> tuple[str, ...]:
        """Return supported operator symbols sorted for display."""
        return tuple(sorted(self._ops.keys()))

    def calculate(self, symbol: str, a: float, b: float) -> float:
        """Execute an operation by symbol."""
        op = self._ops.get(symbol)
        if op is None:
            allowed = ", ".join(self.allowed_symbols())
            raise ValueError(f"Unknown operator: {symbol!r}. Use one of: {allowed}")
        return op.execute(a, b)
