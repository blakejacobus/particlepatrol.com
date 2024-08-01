"""Test user input

Use io library (https://docs.python.org/3/library/io.html) and 
monkeypatch (https://docs.pytest.org/en/stable/how-to/monkeypatch.html) 
fixture to mock and test different input values.
"""

from io import StringIO
from src.input import input_zip


# RED
def test_no_input_zip(monkeypatch):
    """Test for no input value"""
    mock_input = StringIO("\n")  # no value provided
    monkeypatch.setattr("sys.stdin", mock_input)
    assert input_zip() == "zipCode=12345"
    return


# GREEN
def test_input_zip(monkeypatch):
    """Test for a valid input value"""
    mock_input = StringIO("12345\n")
    monkeypatch.setattr("sys.stdin", mock_input)
    assert input_zip() == "zipCode=12345"


# REFACTOR
"""
TODO
- Test for only numeric values
- Test for only 5 characters
- Test for a valid zip code (need database?)
"""
