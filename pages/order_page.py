import allure

from helps.data import OrderUser
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Страница оформления заказа самоката."""

    # Блок для кого самокат

    @allure.step('Заполняем поле "Имя" значением: {first_name}')
    def fill_first_name(self, first_name: str):
        self.type_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step('Заполняем поле "Фамилия" значением: {last_name}')
    def fill_last_name(self, last_name: str):
        self.type_text(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step('Заполняем поле "Адрес" значением: {address}')
    def fill_address(self, address: str):
        self.type_text(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбираем станцию метро: {metro}')
    def select_metro(self, metro: str):
        self.click(OrderPageLocators.METRO_INPUT)
        self.type_text(OrderPageLocators.METRO_INPUT, metro)
        self.click(OrderPageLocators.METRO_OPTION)

    @allure.step('Заполняем поле "Телефон" значением: {phone}')
    def fill_phone(self, phone: str):
        self.type_text(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Переходим со страницы "Для кого самокат" на страницу "Про аренду"')
    def go_to_rent_step(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем блок "Для кого самокат"')
    def fill_recipient_block(self, user: OrderUser):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_address(user.address)
        self.select_metro(user.metro)
        self.fill_phone(user.phone)
        self.go_to_rent_step()

    #  Блок аренды

    @allure.step('Указываем дату доставки: {delivery_date}')
    def set_delivery_date(self, delivery_date: str):
        self.click(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.type_text(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)

    @allure.step('Выбираем срок аренды "трое суток"')
    def choose_three_days_rent(self):
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENT_PERIOD_THREE_DAYS)

    @allure.step('Отмечаем чёрный цвет самоката')
    def select_black_color(self):
        self.click(OrderPageLocators.BLACK_COLOR_CHECKBOX)

    @allure.step('Заполняем комментарий курьеру')
    def fill_comment(self, comment: str):
        self.type_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Нажимаем кнопку "Заказать" на шаге аренды')
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Заполняем блок "Про аренду"')
    def fill_rent_block(self, user: OrderUser):
        self.set_delivery_date(user.delivery_date)
        self.choose_three_days_rent()
        self.select_black_color()
        self.fill_comment(user.comment)
        self.submit_order()

    #  Модалки 

    @allure.step('Подтверждаем оформление заказа')
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step('Проверяем, что модалка с текстом "Заказ оформлен" отображается')
    def is_success_modal_visible(self) -> bool:
        return self.is_visible(OrderPageLocators.SUCCESS_TITLE)

    @allure.step('Полный путь оформления заказа от данных клиента до подтверждения')
    def create_order(self, user: OrderUser):
        self.fill_recipient_block(user)
        self.fill_rent_block(user)
        self.confirm_order()
