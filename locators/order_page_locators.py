# Вспомогательный комментарий для ревью (без изменения логики)


from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы формы оформления заказа самоката."""

    # Блок «Для кого самокат»
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[text()='Парк культуры']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Блок «Про аренду»
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENT_PERIOD_THREE_DAYS = (By.XPATH, "//div[text()='трое суток']")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # Модалка подтверждения заказа
    CONFIRM_NO_BUTTON = (By.XPATH, "//button[text()='Нет']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Модалка успешного заказа
    SUCCESS_TITLE = (By.XPATH, "//div[text()='Заказ оформлен']")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
