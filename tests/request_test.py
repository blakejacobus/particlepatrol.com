"""Test API calls

Validate the responses received from the API using mock inputs
"""

from src.request import request


# RED
def test_invalid_request():
    """Test whether invalid input returns empty list"""
    output = request(zip="abc")
    assert len(output) > 0


# GREEN
def test_empty_request():
    """Test whether invalid zip code returns empty list"""
    output = request(zip=12345)
    assert len(output) == 0


# GREEN
def test_response_type():
    """Test that raw output/response is list type"""
    output = request(zip="abc")
    assert isinstance(output, list)
