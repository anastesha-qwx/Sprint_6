import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from helps.data import Urls


@pytest.fixture
def driver():
    """Инициализация и закрытие браузера Firefox для каждого теста."""
    options = Options()
    # options.add_argument("-headless")  # можно раскомментировать, если нужно без окна

    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.get(Urls.MAIN_PAGE)

    yield browser

    browser.quit()
