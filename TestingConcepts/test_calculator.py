### test_calculator.py -- file to test calculator.py using pytest
# assume calculator.py is in the same directory as this test file.
# assert statements are used to check if the output of the functions is as expected.
# if not, pytest will report a failure for that test case.

import pytest

from calculator import add, subtract, multiply, divide

def test_add():
    assert add(10, 20) == 30

def test_subtract():
    assert subtract(20, 10) == 10

def test_multiply():
    assert multiply(10, 5) == 50

def test_divide():
    assert divide(20, 5) == 4

# python -m pytest -v ---- RUN 
