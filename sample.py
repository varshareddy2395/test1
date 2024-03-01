import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.google.com")

    time.sleep(5)

    # Find the search box and input a query
    search_box = browser.find_element("name", "q")
    search_box.send_keys("pytest with Selenium")

    # Submit the search
    search_box.send_keys(Keys.RETURN)

    # Verify that the search results page contains the expected text
    assert "pytest with Selenium" in browser.title

    time.sleep(5)

if __name__ == "__main__":
    pytest.main(["-v", "sample.py"])