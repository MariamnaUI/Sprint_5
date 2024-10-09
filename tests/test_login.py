from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LoginLocators, MainPageLocators


class TestLogin:
    def test_login_main_button(self, driver, login):
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.text == 'Оформить заказ'

    def test_login_personal_account_login_button(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains('/login'))

        email = 'marianna_mogil_14_qa_python852@yandex.ru'
        password = '123654'

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT)).click()
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON)).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.text == 'Оформить заказ'

    def test_login_register_login_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_LINK))
        driver.find_element(*LoginLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains('/login'))

        email = 'marianna_mogil_14_qa_python852@yandex.ru'
        password = '123654'

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT)).click()
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON)).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.text == 'Оформить заказ'

    def test_login_forgot_pass_login_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_LINK))
        driver.find_element(*LoginLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains('/login'))

        email = 'marianna_mogil_14_qa_python852@yandex.ru'
        password = '123654'

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT)).click()
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON)).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.text == 'Оформить заказ'
