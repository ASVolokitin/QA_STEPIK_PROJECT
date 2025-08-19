import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose interface language")
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nDefined preferred language: {language}")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name.strip().lower() == "chrome":
        print("\nStarting Chrome browser for test ...")
        browser = webdriver.Chrome(options=options)
    elif browser_name.strip().lower() == "firefox":
        print("\nStarting Firefox browser for test ...")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nQuitting browser ...")
    browser.quit()
    