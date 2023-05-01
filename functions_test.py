import math
import pytest
from functions import divide, sq
# testing the sq function
@pytest.mark.parametrize("values", [9,-1,"Hello!",True,3.0])
def test_sq(values):
    assert sq(values)


# Testing the divide function
@pytest.mark.parametrize("divalues",[["10","2"],["10","0"],["10","two"],["ten","10"]])
def test_divide(monkeypatch,capsys,divalues):
    def geninputs():
        for item in divalues:
            yield item
    GEN = geninputs()
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    if divalues[1] == "2":
        assert captured_stdout.strip() == "Your numbers divided is: 5.0"
    else:
        assert captured_stdout.strip() == "Cannot divide by zero or non number."