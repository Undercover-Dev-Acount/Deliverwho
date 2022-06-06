from My_Functions.functions import print_list
from unittest.mock import patch


@patch('builtins.print')
def test_print_list(mock_print):
        list = ['tests', 'tests', 'more tests']
        print_list(list)
        mock_print.assert_called_with(2, 'more tests')
        mock_print.assert_any_call(0, 'tests')
        mock_print.assert_any_call(1, 'tests')