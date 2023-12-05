import pytest
from Firesat23.app import lambda_handler

def test_lambda_handler():
    # Mock event and context
    event = {
        "uploadFrom": "2022-01-01T00:00:00+00:00"
    }
    context = {}

    # Call the lambda_handler function
    response = lambda_handler(event, context)

    # Check that the response is a dictionary with the correct keys
    assert isinstance(response, dict)
    assert "statusCode" in response
    assert "body" in response

    # Check that the status code is 200
    assert response["statusCode"] == 200

    # Check that the body is a dictionary (representing the whole database)
    assert isinstance(response["body"], dict)