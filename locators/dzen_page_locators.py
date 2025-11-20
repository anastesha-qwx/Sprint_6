from selenium.webdriver.common.by import By


class DzenPageLocators:
    """Локаторы для главной страницы Дзена."""
    MAIN_BUTTON = (By.XPATH, "//span[text()='Главная']")
