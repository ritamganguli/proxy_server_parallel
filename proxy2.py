import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from ritam import create_proxy_script


create_proxy_script("ritam2") 

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key




# paste your capibility options below

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "win10"
lt_options = {}
lt_options["username"] = "shubhamr"
lt_options["accessKey"] = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"
lt_options["video"] = True
lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["build"] = "test_build"
lt_options["project"] = "unit_testing"
lt_options["smartUI.project"] = "test"
lt_options["name"] = "basic_unit_selinium"
lt_options["w3c"] = True
lt_options["tunnel"]=True
lt_options["plugin"] = "python-python"
options.set_capability("LT:Options", lt_options)


# Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
# Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
# Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
# Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot
# Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/


class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                "shubhamr", "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"
            ),
            options=options,
        )

    # """ You can write the test cases here """
    def test_demo_site(self):
        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get("https://demo.playwright.dev/api-mocking/")

        time.sleep(50)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()