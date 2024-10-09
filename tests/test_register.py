from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from generator import Generator
from locators.locators import RegisterLocators


class TestRegister:
    def test_register_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegisterLocators.NAME_INPUT).click()
        driver.find_element(*RegisterLocators.NAME_INPUT).send_keys('Мари')

        driver.find_element(*RegisterLocators.EMAIL_INPUT).click()
        driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(Generator.login_generate())

        driver.find_element(*RegisterLocators.PASSWORD_INPUT).click()
        driver.find_element(*RegisterLocators.PASSWORD_INPUT).send_keys(Generator.password_generate())

        driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_register_failed(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*RegisterLocators.NAME_INPUT).click()
        driver.find_element(*RegisterLocators.NAME_INPUT).send_keys('Мари')

        driver.find_element(*RegisterLocators.EMAIL_INPUT).click()
        driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys('marianna_mogil_14_qa_python852@yandex.ru')

        driver.find_element(*RegisterLocators.PASSWORD_INPUT).click()
        driver.find_element(*RegisterLocators.PASSWORD_INPUT).send_keys('1236')

        driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterLocators.ERROR_PASSWORD_MESSAGE))
        WebDriverWait(driver, 10)

        assert error_message.text == 'Некорректный пароль'
