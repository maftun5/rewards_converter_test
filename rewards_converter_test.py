import pytest
#  patch allows us to replace certain parts of our code temporarily, which is useful for testing functions that require
#  user input or print outputs.
from unittest.mock import patch
from rewards_converter import RewardsConverter, RewardValue

# A fixture to create a RewardsConverter object for testing
@pytest.fixture    #setup function that can be used by multiple tests
def converter():
    return RewardsConverter()     #returns an instance of the RewardsConverter class

# Test for valid input value
@patch('builtins.input', return_value='100')  # This line uses patch to simulate user input. We’re pretending
# that the user types in "100" when the program asks for input.
def test_get_input_value_valid(mock_input, converter): #mock_input is a mock object
    result = converter.get_input_value()
    assert result == 100.0

# Test for invalid input value
@patch('builtins.input', return_value='abc')
def test_get_input_value_invalid(mock_input, converter):
    result = converter.get_input_value()
    assert result == -1

# Test for valid cash value parsing
def test_parse_cash_value_valid(converter):
    """
    checks if the parse_cash_value method correctly converts a valid string ('50.5') to a float
    """
    result = converter.parse_cash_value('50.5')
    assert result == 50.5

# Test for invalid cash value parsing
def test_parse_cash_value_invalid(converter):
    result = converter.parse_cash_value('invalid')
    assert result == -1

# Test the conversion of cash value to miles
def test_reward_value_conversion():
    """
    Verifies that the RewardValue class correctly converts cash to miles.
    """
    reward = RewardValue(200)
    assert reward.get_miles_value() == 20000

# Test the conversion and display of miles
@patch('builtins.print')  # Mocking the print function to capture what the program prints during the test
def test_convert_and_display_miles(mock_print, converter):
    converter.convert_and_display_miles(150.5)
    mock_print.assert_any_call("Converting $150.5 to miles")
    mock_print.assert_any_call("$150.5 is worth 15050.0 miles")
