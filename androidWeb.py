from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "Galaxy.*",
    "platformName": "Android",
    "platformVersion": "10",
    "isRealMobile": True,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "network":True,
    "visual": True,
    "video": True,
    "tunnel":True
}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = ""
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  "shubhamr"+":"+"dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"+"@mobile-hub.lambdatest.com/wd/hub")
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(10)
        driver.get("https://lambdatest.com/")
        time.sleep(5)
        driver.find_element_by_xpath("button[class='hidden desktop:block']").click()
        time.sleep(15)
        driver.quit()
    except:
        driver.quit()


startingTest()