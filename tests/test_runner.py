from app.runner import start_calculator


def test_start_calculator_wires_and_calls_repl(monkeypatch):
    captured = {}

    # Patch REPL.run so it doesn't start the real input loop
    def fake_run(calculator):
        captured["calculator"] = calculator

    monkeypatch.setattr("app.runner.CalculatorREPL.run", fake_run)

    start_calculator()

    calc = captured["calculator"]
    assert calc is not None
    assert calc.allowed_symbols() == ("*", "+", "-", "/")
