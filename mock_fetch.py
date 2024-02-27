
import os
import json
from mitmproxy import http

# Initialize dictionaries to hold responses
original_responses = {}
mocked_responses = {}

def set_script_name(name):
    os.environ["SCRIPT_NAME"] = name
    
def response(flow: http.HTTPFlow) -> None:
    # Check for domain of interest
    if "demo.playwright.dev/api-mocking" in flow.request.pretty_url:
        # Save original response
        original_responses[flow.request.pretty_url] = json.loads(flow.response.content)
        save_responses(original_responses, 'api_original_responses.json')

        # Mock specific responses
        mock_data = get_mock_data(flow.request.pretty_url)

        # If mock data exists for the URL, proceed to mock response
        if mock_data is not None:
            mock_response = json.dumps(mock_data).encode("utf-8")
            flow.response = http.Response.make(200, mock_response, {"Content-Type": "application/json"})

            # Save mocked response
            mocked_responses[flow.request.pretty_url] = mock_data
            save_responses(mocked_responses, 'api_mocked_responses.json')

def get_mock_data(pretty_url):
    # Environment variable for script name
    script_name = os.getenv("SCRIPT_NAME", "ritam3")

    mock_data_map = {
        "ritam1": [{"name": "Orange", "id": 1}],
        "ritam2": [{"name": "Banana", "id": 2}],
        "ritam3": [{"name": "Mango", "id": 3}],
    }

    if pretty_url == "https://demo.playwright.dev/api-mocking/api/v1/fruits":
        return mock_data_map.get(script_name)
    else:
        return None

def save_responses(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving the responses to {filename}: {e}")
