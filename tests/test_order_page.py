# Вспомогательный комментарий для ревью (без изменения логики)



import allure

from helps.data import ORDER_USERS
from pages.home_page import Header, MainPage
from pages.order_page import OrderPage


class TestOrderFlow:

    @allure.title('Позитивный сценарий заказа самоката через кнопку "Заказать" в хедере')
    @allure.description(
        '1) Принимаем cookie; '
        '2) Нажимаем "Заказать" в хедере; '
        '3) Заполняем форму "Для кого самокат"; '
        '4) Заполняем форму "Про аренду"; '
        '5) Подтверждаем заказ; '
        '6) Проверяем, что показано окно "Заказ оформлен".'
    )
    def test_order_from_header(self, driver):
        header = Header(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        header.open_order_form_from_header()

        user = ORDER_USERS[0]
        order_page.create_order(user)

        assert order_page.is_success_modal_visible()

    @allure.title('Позитивный сценарий заказа самоката через нижнюю кнопку "Заказать"')
    @allure.description(
        '1) Принимаем cookie; '
        '2) Скроллим до нижней кнопки "Заказать" на главной и кликаем; '
        '3) Заполняем форму "Для кого самокат"; '
        '4) Заполняем форму "Про аренду"; '
        '5) Подтверждаем заказ; '
        '6) Проверяем, что показано окно "Заказ оформлен".'
    )
    def test_order_from_main_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.open_order_form_from_main_button()

        user = ORDER_USERS[1]
        order_page.create_order(user)

        assert order_page.is_success_modal_visible()
