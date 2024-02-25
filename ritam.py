import os

def create_proxy_script(script_name="ritam2"):
    """
    Creates or updates the proxy.py file with a specified script name for request interception.

    :param script_name: The name of the script to use for modifying requests, default is "ritam2".
    """
    # Define the content of the proxy.py file as a multi-line string with the dynamic script name
    proxy_py_content = f"""
import os
from mitmproxy import http
import json

def request(flow: http.HTTPFlow) -> None:
    script_name = os.getenv("SCRIPT_NAME", "{script_name}")  # Use the passed script name or default

    mock_data_map = {{
        "ritam1": [{{"name": "Orange", "id": 1}}],
        "ritam2": [{{"name": "Banana", "id": 2}}],
        "ritam3": [{{"name": "Mango", "id": 3}}],
    }}

    if flow.request.pretty_url == "https://demo.playwright.dev/api-mocking/api/v1/fruits":
        mock_data = mock_data_map.get(script_name, [])
        mock_response = json.dumps(mock_data).encode("utf-8")
        flow.response = http.Response.make(200, mock_response, {{"Content-Type": "application/json"}})
    """

    # Open a new file named proxy.py in write mode
    with open("proxy.py", "w") as file:
        # Write the content to the file
        file.write(proxy_py_content)

    print(f"proxy.py has been created and written successfully with script name set to {script_name}.")

# create_proxy_script("ritam1")

# Example usage:
# create_proxy_script("ritam1")

# Now, you can initialize your Selenium browser session here after setting the script name.
