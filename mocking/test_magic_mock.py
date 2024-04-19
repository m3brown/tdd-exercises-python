import pytest
from unittest.mock import MagicMock
from user_profile import UserProfile


def test_user_profile_success():
    # Arrange
    #   create an instance of MagicMock
    mock_data_service = MagicMock()

    #   setup the mock to return a specific value when called
    mock_data_service.get_user_data.return_value = {"username": "john_doe", "age": 30}

    #   init UserProfile with the mocked service
    user_profile = UserProfile(data_service=mock_data_service)

    # Act
    #   call the method that uses the mocked service
    actual = user_profile.fetch_user_data()

    # Assert
    expected = {"username": "john_doe", "age": 30}
    #   check if the actual is the expected
    assert actual == expected


def test_user_profile_failure():
    # Arrange
    #   create an instance of MagicMock
    mock_data_service = MagicMock()

    #   setup the mock to raise an exception when called
    mock_data_service.get_user_data.side_effect = Exception("Failed to fetch data")

    #   init UserProfile with the mocked service
    user_profile = UserProfile(data_service=mock_data_service)

    # Act
    #   test the action with pytest
    with pytest.raises(Exception) as exc_info:
        user_profile.fetch_user_data()

    # Assert
    #   check if the correct message was raised
    assert str(exc_info.value) == "Failed to fetch data"
