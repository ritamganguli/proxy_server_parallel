
import os
from mitmproxy import http
import json

def request(flow: http.HTTPFlow) -> None:
    script_name = os.getenv("SCRIPT_NAME", "ritam3")  # Use the passed script name or default

    mock_data_map = {
        "ritam1": [{"name": "Orange", "id": 1}],
        "ritam2": [{"name": "Banana", "id": 2}],
        "ritam3": [{"name": "Mango", "id": 3}],
    }

    if flow.request.pretty_url == "https://demo.playwright.dev/api-mocking/api/v1/fruits":
        mock_data = mock_data_map.get(script_name, [])
        mock_response = json.dumps(mock_data).encode("utf-8")
        flow.response = http.Response.make(200, mock_response, {"Content-Type": "application/json"})
    