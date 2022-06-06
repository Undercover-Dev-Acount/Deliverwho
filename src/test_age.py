
from My_Functions.functions import age_check
from unittest.mock import patch

@patch('builtins.input')
def test_age_check(mock_input):
    mock_input.return_value = 18
    min_age = 18

    expected = True 
    actual = age_check(mock_input, min_age)

    assert expected == actual

@patch('builtins.input')
def test_under_age_check(mock_input):
    mock_input.return_value = 17
    min_age = 18

    expected = False
    actual = age_check(mock_input, min_age)

    assert expected == actual


@patch('builtins.input')
def test_not_int_check(mock_input):
    mock_input.return_value = 'what?'
    min_age = 18

    expected = False
    actual = age_check(mock_input, min_age)

    assert expected == actual