from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]') #Кнопка "Конструктор" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]') # Кнопка "Личный Кабинет" на главной странице
    LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # "Логотип" на главной странице
    ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') # Кнопка "Оформить заказ" на главной странице

class RegisterLocators:
    NAME_INPUT = (By.XPATH, '//fieldset[1]//div[1]//div[1]//input[1]') # Поле ввода "Имя"
    EMAIL_INPUT = (By.XPATH, '//fieldset[2]//div[1]//div[1]//input[1]') # "E-mail"
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]') # Поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]') # Кнопка "Зарегистрироваться"
    ERROR_PASSWORD_MESSAGE = (By.XPATH, '//p[@class="input__error text_type_main-default"]') # Ошибка при невалидном пароле

class LoginLocators:
    LOGIN_MAIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]') # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_LINK = (By.XPATH, '//a[contains(text(),"Войти")]') # Кнопка "Войти" ввиде ссылки
    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]') # "E-mail"
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]') # Поле ввода "Пароль"
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]') # Кнопка "Войти"

class ProfileLocators:
    PROFILE_BUTTON = (By.XPATH, '//a[contains(text(),"Профиль")]') # Кнопка "Профиль"
    EXIT_BUTTON = (By.XPATH, '//button[contains(text(),\'Выход\')]') # Кнопка "Выход"
    
class  ConstructorPage:
    HEADER_BURGER_INGREDIENTS = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]') #Заголовок таблицы конструктора
    BUNS_BURGER_INGREDIENTS_BUTTON = (By.XPATH, '//span[contains(text(),\'Булки\')]')  # Заголовок раздела "Булки"
    SAUCES_BURGER_INGREDIENTS_BUTTON = (By.XPATH, '//span[contains(text(),\'Соусы\')]')  # Заголовок раздела "Соусы"
    FILLINGS_BURGER_INGREDIENTS_BUTTON = (By.XPATH, '//span[contains(text(),\'Начинки\')]')  # Заголовок раздела "Начинки"
    BUNS_BURGER_INGREDIENTS_SECTION = (By.XPATH, '//h2[contains(text(),\'Булки\')]')  # Раздел "Булки"
    SAUCES_BURGER_INGREDIENTS_SECTION = (By.XPATH, '//h2[contains(text(),\'Соусы\')]')  # Раздел "Соусы"
    FILLINGS_BURGER_INGREDIENTS_SECTION = (By.XPATH, '//h2[contains(text(),\'Начинки\')]')  # Раздел "Начинки"
