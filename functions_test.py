import math
import pytest
from functions import *
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
        
# Testing the greet user function

@pytest.mark.parametrize("first,middle,last", [("Your", "Mom", "Mother"), ("Hello", "World", "!")])
def test_greetUser(capfd, first, middle, last):
    greetUser(first, middle, last)
    captured = capfd.readouterr()
    assert captured.out == f"Hello!\nWelcome to the program {first} {middle} {last}\nGlad to have you!\n"

@pytest.mark.parametrize("args", [("Your", "Mom", "Mother"), ("Hello", "World", "!")])
def test_greetUser_returns_none(args):
    assert greetUser(*args) == None

@pytest.mark.parametrize("args", [(123, 456, 789), (1, "two", 3)])
def test_greetUser_raises_type_error(args):
    with pytest.raises(TypeError):
        greetUser(*args)

@pytest.mark.parametrize("args", [("", "Middle", "Last"), ("First", "", "Last"), ("First", "Middle", "")])
def test_greetUser_with_empty_inputs(args, capsys):
    with pytest.raises(ValueError):
        greetUser(*args)
