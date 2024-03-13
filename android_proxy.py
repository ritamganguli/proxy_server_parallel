import json
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Check if the request URL matches the one we want to redirect from
    if flow.request.pretty_url == "https://www.lambdatest.com/":
        # Change the request URL to the new target
        flow.request.url = "https://www.lambdatest.com/pricing"

def response(flow: http.HTTPFlow) -> None:
    # Capture the request URL and response content
    if flow.request.pretty_url == "https://www.lambdatest.com/pricing":
        captured_data = {
            "request_url": flow.request.pretty_url,
            "response_content": flow.response.content.decode('utf-8', 'ignore')  # Decoding to utf-8, ignoring errors
        }

        # Save to a JSON file
        with open("traffic_data.json", "w") as file:
            json.dump([captured_data], file, indent=4)
