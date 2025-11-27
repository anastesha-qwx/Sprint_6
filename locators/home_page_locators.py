from selenium.webdriver.common.by import By


class HeaderLocators:
    """Элементы шапки сайта Самоката."""
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

    # Важно: берём ровно первую кнопку «Заказать» по тексту
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Статус заказа']")

    ORDER_NUMBER_INPUT = (By.CSS_SELECTOR, "input[class*='Header_Input']")
    GO_BUTTON = (By.XPATH, "//input[contains(@class,'Header_Input')]/following::button[contains(@class,'Button')][1]")

    TRAINING_TITLE = (By.CSS_SELECTOR, "div.Home_Header__iJKdX")


class MainPageLocators:
    """Элементы основной части главной страницы."""
    MAIN_TITLE = (By.CSS_SELECTOR, "div.Home_Header__iJKdX")

    # Нижняя «Заказать» — вторая по тексту
    MIDDLE_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    COOKIES_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Для скролла к FAQ используем стабильный ID первого пункта
    FAQ_TITLE = (By.ID, "accordion__heading-0")

    FAQ_QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    FAQ_ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]
