import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CompanyApi import CompanyApi


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser

    browser.quit()

@pytest.fixture
def client():
    return CompanyApi("https://x-clients-be.onrender.com")

@pytest.fixture(scope="session")
def client():
		return CompanyApi("https://x-clients-be.onrender.com")