from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы формы оформления заказа самоката."""

    # «Для кого самокат»
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[text()='Парк культуры']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # «Про аренду»
    DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CSS_SELECTOR, "div.Dropdown-control .Dropdown-arrow")
    RENT_PERIOD_THREE_DAYS = (By.XPATH, "//div[contains(@class,'Dropdown-option') and contains(.,'трое суток')]")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # Подтверждение
    CONFIRM_NO_BUTTON = (By.XPATH, "//button[text()='Нет']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Успешный заказ
    SUCCESS_TITLE = (By.XPATH, "//div[text()='Заказ оформлен']")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
