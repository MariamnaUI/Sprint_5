from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import ConstructorPage, MainPageLocators


class TestRedirectFromAccountToConstructor:
    def test_redirect_click_constructor(self, driver, open_profile):
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        burger_ingredients = WebDriverWait(driver,5).until(EC.visibility_of_element_located(ConstructorPage.HEADER_BURGER_INGREDIENTS))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert burger_ingredients.text == 'Соберите бургер'

    def test_redirect_click_logo(self, driver, open_profile):
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()

        burger_ingredients = WebDriverWait(driver,5).until(EC.visibility_of_element_located(ConstructorPage.HEADER_BURGER_INGREDIENTS))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert burger_ingredients.text == 'Соберите бургер'