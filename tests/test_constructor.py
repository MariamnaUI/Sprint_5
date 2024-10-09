from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import ConstructorPage


class TestConstructor:
    def test_constructor_buns_section(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPage.HEADER_BURGER_INGREDIENTS))
        driver.find_element(*ConstructorPage.SAUCES_BURGER_INGREDIENTS_BUTTON).click()
        driver.find_element(*ConstructorPage.BUNS_BURGER_INGREDIENTS_BUTTON).click()

        buns_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPage.BUNS_BURGER_INGREDIENTS_SECTION))
        assert buns_section.is_displayed()

    def test_constructor_sauces_section(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPage.HEADER_BURGER_INGREDIENTS))
        driver.find_element(*ConstructorPage.SAUCES_BURGER_INGREDIENTS_BUTTON).click()

        sauces_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPage.SAUCES_BURGER_INGREDIENTS_SECTION))
        assert sauces_section.is_displayed()

    def test_constructor_fillings_section(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPage.HEADER_BURGER_INGREDIENTS))
        driver.find_element(*ConstructorPage.FILLINGS_BURGER_INGREDIENTS_BUTTON).click()

        fillings_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPage.FILLINGS_BURGER_INGREDIENTS_SECTION))
        assert fillings_section.is_displayed()
