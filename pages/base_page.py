# Вспомогательный комментарий для ревью (без изменения логики)



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Object-ов."""

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.wait_clickable(locator).click()

    def type_text(self, locator, text: str):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    def scroll_to(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def current_url(self) -> str:
        return self.driver.current_url

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False
