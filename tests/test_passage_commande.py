import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.login_page import LoginPage
from pages.commande_page import CommandePage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor="http://selenium-hub:4444/wd/hub",
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()
def test_sample():
    assert 1 == 1