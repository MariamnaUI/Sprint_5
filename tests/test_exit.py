from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LoginLocators, ProfileLocators


class TestExitAccount:
    def test_exit_account_click_exit_button(self, driver, open_profile):
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(ProfileLocators.EXIT_BUTTON))
        driver.find_element(*ProfileLocators.EXIT_BUTTON).click()

        login_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        assert login_button.is_displayed()
