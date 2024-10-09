from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LoginLocators, MainPageLocators, ProfileLocators


class TestClickAccount:
    def test_click_account_not_authorized(self,driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_MAIN_BUTTON))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains('/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_click_account_authorized(self,driver,login):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        profile_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfileLocators.PROFILE_BUTTON))
        assert profile_button.is_displayed()
