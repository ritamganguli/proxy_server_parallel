import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from ritam import create_proxy_script

# Assuming create_proxy_script function is defined in the same script or imported
create_proxy_script("ritam2")  # Call this with "ritam1", "ritam2", or "ritam3"

chrome_options = Options()
# Configure Selenium to use mitmproxy running on localhost:8080
chrome_options.add_argument('--proxy-server=http://localhost:8080')

# Automatically download and use the correct version of ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# Start mitmproxy with the proxy.py script before this step, for example:
# mitmproxy -s proxy.py

# Replace 'https://www.example.com' with the URL you wish to open
driver.get("https://demo.playwright.dev/api-mocking/")
time.sleep(30000)

# Your code here, for example, to interact with the website

# Close the browser window when done
driver.quit()
