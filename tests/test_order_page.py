# Вспомогательный комментарий для ревью (без изменения логики)

import allure
import pytest

from helps.data import ORDER_USERS, Urls
from pages.home_page import Header, MainPage


class TestOrderFlow:

    @allure.title('Позитивный сценарий заказа самоката через кнопку "Заказать" в хедере')
    @allure.description(
        '1) Принимаем cookie; '
        '2) Нажимаем "Заказать" в хедере; '
        '3) Заполняем форму "Для кого самокат"; '
        '4) Заполняем форму "Про аренду"; '
        '5) Подтверждаем заказ; '
        '6) Переходим на страницу статуса заказа; '
        '7) По клику на логотип "Самокат" возвращаемся на главную; '
        '8) Проверяем, что показано окно "Заказ оформлен" и произошёл переход на главную страницу.'
    )
    @pytest.mark.parametrize("user", ORDER_USERS)
    def test_order_from_header(self, driver, create_order, user):
        header = Header(driver)
        main_page = MainPage(driver)

        main_page.accept_cookies()
        header.open_order_form_from_header()

        # Заполняем форму заказа и подтверждаем заказ через фикстуру
        order_page = create_order(user)

        # Проверка успешной модалки
        assert order_page.is_success_modal_visible()

        # Переход на страницу статуса заказа
        order_page.open_status_page()
        assert order_page.current_url().startswith(Urls.TRACK_PAGE)

        # Возврат на главную по лого «Самокат»
        header.click_scooter_logo()
        assert header.current_url() == Urls.MAIN_PAGE

    @allure.title('Позитивный сценарий заказа самоката через нижнюю кнопку "Заказать"')
    @allure.description(
        '1) Принимаем cookie; '
        '2) Скроллим до нижней кнопки "Заказать" на главной и кликаем; '
        '3) Заполняем форму "Для кого самокат"; '
        '4) Заполняем форму "Про аренду"; '
        '5) Подтверждаем заказ; '
        '6) Переходим на страницу статуса заказа; '
        '7) По клику на логотип "Самокат" возвращаемся на главную; '
        '8) Проверяем, что показано окно "Заказ оформлен" и произошёл переход на главную страницу.'
    )
    @pytest.mark.parametrize("user", ORDER_USERS)
    def test_order_from_main_button(self, driver, create_order, user):
        header = Header(driver)
        main_page = MainPage(driver)

        main_page.accept_cookies()
        main_page.open_order_form_from_main_button()

        # Заполняем форму заказа и подтверждаем заказ через фикстуру
        order_page = create_order(user)

        # Проверка успешной модалки
        assert order_page.is_success_modal_visible()

        # Переход на страницу статуса заказа
        order_page.open_status_page()
        assert order_page.current_url().startswith(Urls.TRACK_PAGE)

        # Возврат на главную по лого «Самокат»
        header.click_scooter_logo()
        assert header.current_url() == Urls.MAIN_PAGE


