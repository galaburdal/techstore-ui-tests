import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    chrome_bin = os.getenv("CHROME_BIN")
    if chrome_bin:
        options.binary_location = chrome_bin

    driver_path = os.getenv("CHROMEDRIVER")
    service = Service(executable_path=driver_path) if driver_path else Service()
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_page_load_timeout(30)
    yield browser
    browser.quit()
