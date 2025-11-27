# conftest с фикстурами для проекта Sprint_6 (UI-тесты Яндекс.Самоката)

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from helps.data import Urls
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    """Инициализация и закрытие браузера Firefox для каждого теста."""
    options = Options()
    # options.add_argument("-headless")  # можно раскомментировать для прогонов без окна

    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.get(Urls.MAIN_PAGE)

    yield browser

    browser.quit()


@pytest.fixture
def create_order(driver):
    """Фикстура, которая заполняет обе части формы заказа и подтверждает заказ.
    Возвращает объект OrderPage для дальнейших проверок.
    """
    order_page = OrderPage(driver)

    def _create_order(user):
        order_page.fill_recipient_block(user)
        order_page.fill_rent_block(user)
        order_page.confirm_order()
        return order_page

    return _create_order


