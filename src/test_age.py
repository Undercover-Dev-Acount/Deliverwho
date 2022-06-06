
from functions import age_check
from unittest.mock import patch

@patch('builtins.input')
def test_age_check(mock_input):
    mock_input.return_value = 18
    age = input
    min_age = 18

    expected = True 
    actual = age_check(age, min_age)

    assert expected == actual

@patch('builtins.input')
def test_under_age_check(mock_input):
    mock_input.return_value = 17
    age = input
    min_age = 18

    expected = False
    actual = age_check(age, min_age)

    assert expected == actual


@patch('builtins.input')
def test_not_int_check(mock_input):
    mock_input.return_value = 'what?'
    age = input
    min_age = 18

    expected = False
    actual = age_check(age, min_age)

    assert expected == actual