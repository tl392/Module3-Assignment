"""
parser

This module handles ALL user input validation.

Why static methods?
- Parsing does not depend on object state
- These are pure utility functions
- Keeps responsibilities clearly separated
"""

from __future__ import annotations


class InputParser:
    """Static parsing helpers for operator and numeric input."""

    class QuitCalculator(Exception):
        """Raised when the user requests to quit (q/quit/exit)."""
        pass

    @staticmethod
    def is_quit(text: str) -> bool:
        """Return True if text is a quit command."""
        return text.strip().lower() in {"q", "quit", "exit"}

    @staticmethod
    def parse_operator(raw: str) -> str:
        """
        Parse the operator.
        Operator validity (supported ops) is checked by Calculator.
        """
        raw = raw.strip()
        if InputParser.is_quit(raw):
            raise InputParser.QuitCalculator
        if not raw:
            raise ValueError("Operator cannot be empty.")
        return raw

    @staticmethod
    def parse_number(raw: str) -> float:
        """Parse a number into float."""
        raw = raw.strip()
        if InputParser.is_quit(raw):
            raise InputParser.QuitCalculator
        try:
            return float(raw)
        except ValueError as exc:
            raise ValueError(f"Invalid number: {raw!r}. Please enter a numeric value.") from exc
