# Вспомогательный комментарий для ревью (без изменения логики)



import allure

from locators.home_page_locators import HeaderLocators, MainPageLocators
from pages.base_page import BasePage


class Header(BasePage):
    """Действия с хедером сайта."""

    @allure.step('Клик по логотипу Яндекса в хедере')
    def click_yandex_logo(self):
        self.click(HeaderLocators.YANDEX_LOGO)

    @allure.step('Клик по логотипу Самоката в хедере')
    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    @allure.step('Открываем форму заказа по кнопке "Заказать" в хедере')
    def open_order_form_from_header(self):
        self.click(HeaderLocators.ORDER_BUTTON)

    @allure.step('Проверяем, что заголовок "Учебный тренажер" отображается')
    def is_training_title_visible(self) -> bool:
        return self.is_visible(HeaderLocators.TRAINING_TITLE)


class MainPage(BasePage):
    """Главная страница сервиса Самокат."""

    @allure.step('Принимаем cookie на главной странице')
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIES_ACCEPT_BUTTON)

    @allure.step('Прокручиваем до нижней кнопки "Заказать" и кликаем по ней')
    def open_order_form_from_main_button(self):
        self.scroll_to(MainPageLocators.MIDDLE_ORDER_BUTTON)
        self.click(MainPageLocators.MIDDLE_ORDER_BUTTON)



    @allure.step('Прокручиваем страницу до блока "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to(MainPageLocators.FAQ_TITLE)

    @allure.step('Открываем вопрос под номером {index} в блоке FAQ')
    def open_faq_question(self, index: int):
        self.scroll_to_faq()
        question_locator = MainPageLocators.FAQ_QUESTIONS[index]
        self.click(question_locator)

    @allure.step('Получаем текст ответа на вопрос под номером {index}')
    def get_faq_answer_text(self, index: int) -> str:
        self.open_faq_question(index)
        answer_locator = MainPageLocators.FAQ_ANSWERS[index]
        return self.get_text(answer_locator)
