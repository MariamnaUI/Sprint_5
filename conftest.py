import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LoginLocators, MainPageLocators


# Инициализация драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 5)
    yield driver
    driver.quit()

# Авторизация
@pytest.fixture
def login(driver):
    email = 'mak2112@yandex.ru'
    password = '123654'

    driver.find_element(*LoginLocators.LOGIN_MAIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).click()
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT)).click()
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON)).click()

# Открытие страницы профиля
@pytest.fixture
def open_profile(driver, login):
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
