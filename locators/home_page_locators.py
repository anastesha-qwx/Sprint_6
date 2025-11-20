from selenium.webdriver.common.by import By


class HeaderLocators:
    """Элементы шапки сайта Самоката."""
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Статус заказа']")
    ORDER_NUMBER_INPUT = (By.XPATH, "//input[contains(@class,'Header_Input')]")
    GO_BUTTON = (By.XPATH, "//button[text()='Go!']")
    TRACK_PLACEHOLDER_INPUT = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    TRAINING_TITLE = (By.XPATH, "//div[text()='Учебный тренажер']")


class MainPageLocators:
    """Элементы основной части главной страницы."""
    MAIN_TITLE = (By.XPATH, "//div[@class='Home_Header__iJKdX']")
    MIDDLE_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    COOKIES_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_TITLE = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Вопросы аккордеона
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

    # Ответы аккордеона
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
