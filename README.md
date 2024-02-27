# Mocking Up The API & Running Them In Parallel & Getting Response ![pw](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

<p align="center">
<img height="500" src="https://user-images.githubusercontent.com/95698164/171858189-9de5d3ef-f177-49ac-9de6-6edb3441740b.png">
</p>

<p align="center">
  <a href="https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python" target="_bank">Blog</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python" target="_bank">Docs</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python" target="_bank">Learning Hub</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/newsletter/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python" target="_bank">Newsletter</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/certifications/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python" target="_bank">Certifications</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.youtube.com/c/LambdaTest" target="_bank">YouTube</a>
</p>
&emsp;
&emsp;
&emsp;

_Appium is a tool for automating native, mobile web, and hybrid applications on iOS, Android, and Windows platforms. It supports iOS native apps written in Objective-C or Swift and Android native apps written in Java or Kotlin. It also supports mobile web apps accessed using a mobile browser (Appium supports Safari on iOS and Chrome or the built-in 'Browser' app on Android). Perform Appium automation tests on [LambdaTest's online cloud](https://www.lambdatest.com/appium-mobile-testing?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)._

_Learn the basics of [Appium testing on the LambdaTest platform](https://www.lambdatest.com/support/docs/getting-started-with-appium-testing/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)._

[<img height="53" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)

## Table of Contents

- [Pre-requisites](#pre-requisites)
- [Run Your First Test](#run-your-first-test)
- [Executing The Tests](#executing-the-tests)

## Pre-requisites

Before you can start performing App automation testing with Appium, you would need to follow these steps:

- Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
- Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).

### Clone The Sample Project

Clone the LambdaTest’s [LT-appium-python](https://github.com/LambdaTest/LT-appium-python) and navigate to the code directory as shown below:

```bash
git clone https://github.com/ritamganguli/proxy_server_parallel/
cd proxy_server_parallel
```

Install the required dependencies by using the following command:

```bash
pip install mitm proxy
pip install selenium==3.12.0
pip install -r requirements.txt
```


## For Mocking UP API Response

1) Basically, first you need to set up the MITM proxy and accept all the certificates for it ( By default it allows only HTTP request)

Download Link: https://mitmproxy.org/ 

2) Mitm Proxy runs on port 8080 so please make sure that you stop all the activities like Jenkins which are running on port 8080

  ```bash
  .\jenkins.exe stop
  ```
  
  And to start back the Jenkins once testing is done
  
  ```bash
  .\jenkins.exe start
  ```
3) Start the proxy server script that you made in order to mock up the api's

    ```bash
    mitmproxy -s proxy.py
    ```
4) Start up the tunnel and pass up the proxy host and the proxy port over there
    ```bash
      ./LT --user {acoount_id} --key {acees_key} --proxy-port 8080 -v --shared-tunnel --proxy-host localhost --ingress-only --mitm
      ```

5) Start testing your testcase over lambdatest
   ```bash
      python proxy2.py
      ```


Code Logic

```
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
        mock_data = mock_data_map.get(script_name, []) #basically we pass this test name over the script name and the data comes accordingly 
        mock_response = json.dumps(mock_data).encode("utf-8")
        flow.response = http.Response.make(200, mock_response, {"Content-Type": "application/json"})

```

For eg how we call the name

<img width="959" alt="image" src="https://github.com/ritamganguli/proxy_server_parallel/assets/35348707/d4acc229-f219-4e42-bc51-336e68084aa8">




## For Fetching Up API Response

1) Basically, first you need to set up the MITM proxy and accept all the certificates for it ( By default it allows only HTTP request)

Download Link: https://mitmproxy.org/ 

2) Mitm Proxy runs on port 8080 so please make sure that you stop all the activities like Jenkins which are running on port 8080

  ```bash
  .\jenkins.exe stop
  ```
  
  And to start back the Jenkins once testing is done
  
  ```bash
  .\jenkins.exe start
  ```
3) Start the proxy server script that you made in order to mock up the api's

    ```bash
    mitmproxy -s response.py
    ```
4) Start up the tunnel and pass up the proxy host and the proxy port over there
    ```bash
      ./LT --user {acoount_id} --key {acees_key} --proxy-port 8080 -v --shared-tunnel --proxy-host localhost --ingress-only --mitm
      ```

5) Start testing your testcase over lambdatest
   ```bash
      python proxy2.py
      ```

Code Logic
```
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
        save_responses(original_responses, 'api_original_responses.json') #---> Name of the file where original api response will be saved

        # Mock specific responses
        mock_data = get_mock_data(flow.request.pretty_url)

        # If mock data exists for the URL, proceed to mock response
        if mock_data is not None:
            mock_response = json.dumps(mock_data).encode("utf-8")
            flow.response = http.Response.make(200, mock_response, {"Content-Type": "application/json"})

            # Save mocked response
            mocked_responses[flow.request.pretty_url] = mock_data
            save_responses(mocked_responses, 'api_mocked_responses.json') #---> Name of the file where mocked api response will be saved

def get_mock_data(pretty_url):
    # Environment variable for script name
    script_name = os.getenv("SCRIPT_NAME", "ritam2")

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


```


## For Fetching Up API Along With Response

1) Basically, first you need to set up the MITM proxy and accept all the certificates for it ( By default it allows only HTTP request)

Download Link: https://mitmproxy.org/ 

2) Mitm Proxy runs on port 8080 so please make sure that you stop all the activities like Jenkins which are running on port 8080

  ```bash
  .\jenkins.exe stop
  ```
  
  And to start back the Jenkins once testing is done
  
  ```bash
  .\jenkins.exe start
  ```
3) Start the proxy server script that you made in order to mock up the api's

    ```bash
    mitmproxy -s mock_fetch.py
    ```
4) Start up the tunnel and pass up the proxy host and the proxy port over there
    ```bash
      ./LT --user {acoount_id} --key {acees_key} --proxy-port 8080 -v --shared-tunnel --proxy-host localhost --ingress-only --mitm
      ```

5) Start testing your testcase over lambdatest
   ```bash
      python proxy4.py
      ```

Code Logic

```
def write_script(script_name, filename='ritam.py'):
    script_content = f"""
import os
import json
from mitmproxy import http

# Initialize dictionaries to hold responses
original_responses = {{}}
mocked_responses = {{}}

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
            flow.response = http.Response.make(200, mock_response, {{"Content-Type": "application/json"}})

            # Save mocked response
            mocked_responses[flow.request.pretty_url] = mock_data
            save_responses(mocked_responses, 'api_mocked_responses.json')

def get_mock_data(pretty_url):
    # Environment variable for script name
    script_name = os.getenv("SCRIPT_NAME", "{script_name}")

    mock_data_map = {{
        "ritam1": [{{"name": "Orange", "id": 1}}],
        "ritam2": [{{"name": "Banana", "id": 2}}],
        "ritam3": [{{"name": "Mango", "id": 3}}],
    }}

    if pretty_url == "https://demo.playwright.dev/api-mocking/api/v1/fruits":
        return mock_data_map.get(script_name)
    else:
        return None

def save_responses(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving the responses to {{filename}}: {{e}}")
"""

    # Write the formatted script content to the specified file
    with open(filename, 'w') as file:
        file.write(script_content)
```

How to use in other functions

```
from ritam3 import write_script

write_script('ritam3', 'mock_fetch.py')

```








**Info Note:**
If you are unable to run the automation script with the above mentioned commands try **'python'** command except for **'python3'**.

> Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on the [LambdaTest App Automation Dashboard](https://appautomation.lambdatest.com/build?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python).

> If you fail to run the tests, try creating virtual env and installing the dependencies in that environment to run the tests.
> Creating and activating a virtual environment
```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

## Additional Links

- [Advanced Configuration for Capabilities](https://www.lambdatest.com/support/docs/desired-capabilities-in-appium/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)
- [How to test locally hosted apps](https://www.lambdatest.com/support/docs/testing-locally-hosted-pages/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)
- [How to integrate LambdaTest with CI/CD](https://www.lambdatest.com/support/docs/integrations-with-ci-cd-tools/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)

## Documentation & Resources :books:

Visit the following links to learn more about LambdaTest's features, setup and tutorials around test automation, mobile app testing, responsive testing, and manual testing.

- [LambdaTest Documentation](https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)
- [LambdaTest Blog](https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)
- [LambdaTest Learning Hub](https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)

## LambdaTest Community :busts_in_silhouette:

The [LambdaTest Community](https://community.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python) allows people to interact with tech enthusiasts. Connect, ask questions, and learn from tech-savvy people. Discuss best practises in web development, testing, and DevOps with professionals from across the globe 🌎

## What's New At LambdaTest ❓

To stay updated with the latest features and product add-ons, visit [Changelog](https://changelog.lambdatest.com/)

## About LambdaTest

[LambdaTest](https://www.lambdatest.com?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python) is a leading test execution and orchestration platform that is fast, reliable, scalable, and secure. It allows users to run both manual and automated testing of web and mobile apps across 3000+ different browsers, operating systems, and real device combinations. Using LambdaTest, businesses can ensure quicker developer feedback and hence achieve faster go to market. Over 500 enterprises and 1 Million + users across 130+ countries rely on LambdaTest for their testing needs.

### Features

- Run Selenium, Cypress, Puppeteer, Playwright, and Appium automation tests across 3000+ real desktop and mobile environments.
- Real-time cross browser testing on 3000+ environments.
- Test on Real device cloud
- Blazing fast test automation with HyperExecute
- Accelerate testing, shorten job times and get faster feedback on code changes with Test At Scale.
- Smart Visual Regression Testing on cloud
- 120+ third-party integrations with your favorite tool for CI/CD, Project Management, Codeless Automation, and more.
- Automated Screenshot testing across multiple browsers in a single click.
- Local testing of web and mobile apps.
- Online Accessibility Testing across 3000+ desktop and mobile browsers, browser versions, and operating systems.
- Geolocation testing of web and mobile apps across 53+ countries.
- LT Browser - for responsive testing across 50+ pre-installed mobile, tablets, desktop, and laptop viewports

[<img height="53" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)

## We are here to help you :headphones:

- Got a query? we are available 24x7 to help. [Contact Us](mailto:support@lambdatest.com)
- For more info, visit - [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python)
