# Вспомогательный комментарий для ревью (без изменения логики)



import allure
import pytest

from helps.data import Urls, FAQ_ANSWERS
from pages.dzen_page import DzenPage
from pages.home_page import Header, MainPage


class TestMainPageHeader:

    @allure.title('Переход на главную страницу Самоката по клику на логотип "Самокат"')
    @allure.description(
        '1) Открываем форму заказа из хедера; '
        '2) Кликаем по логотипу Самоката; '
        '3) Проверяем, что вернулись на главную и виден заголовок "Учебный тренажер".'
    )
    def test_scooter_logo_opens_main_page(self, driver):
        header = Header(driver)
        main_page = MainPage(driver)

        main_page.accept_cookies()
        header.open_order_form_from_header()
        header.click_scooter_logo()

        assert header.current_url() == Urls.MAIN_PAGE
        assert header.is_training_title_visible()

    @allure.title('Переход на главную страницу Дзена по клику на логотип "Яндекс"')
    @allure.description(
        '1) Принимаем cookie; '
        '2) Кликаем по логотипу Яндекса; '
        '3) Переключаемся на новую вкладку; '
        '4) Ждём появления кнопки "Главная" и проверяем адрес страницы.'
    )
    def test_yandex_logo_opens_dzen(self, driver):
        header = Header(driver)
        main_page = MainPage(driver)
        dzen_page = DzenPage(driver)

        main_page.accept_cookies()
        header.click_yandex_logo()
        header.switch_to_new_tab()

        dzen_page.wait_main_button()
        assert header.current_url() == Urls.DZEN_MAIN

    @allure.title('Проверка текстов ответов в блоке "Вопросы о важном"')
    @allure.description(
        'Для каждого вопроса из блока FAQ: '
        '1) Скроллим к блоку; '
        '2) Кликаем по вопросу; '
        '3) Считываем текст ответа; '
        '4) Сравниваем его с ожидаемым.'
    )
    @pytest.mark.parametrize(
        "index, expected_answer",
        list(enumerate(FAQ_ANSWERS))
    )
    def test_faq_answers(self, driver, index, expected_answer):
        main_page = MainPage(driver)

        main_page.accept_cookies()
        answer_text = main_page.get_faq_answer_text(index)

        assert answer_text == expected_answer
