# Вспомогательный комментарий для ревью (без изменения логики)

import allure

from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage


class DzenPage(BasePage):
    """Страница Дзена."""

    @allure.step('Ожидаем отображения кнопки "Главная" на Дзене')
    def wait_main_button(self):
        return self.wait_visible(DzenPageLocators.MAIN_BUTTON)
