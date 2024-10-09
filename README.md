# Sprint_5

## Файлы
test_constructor.py - тесты на раздел "Конструктор"  
test_redirect_from_account_to_constructor.py - тесты на "Переход из личного кабинета в конструктор"    
test_account - тесты на "Переход в личный кабинет"  
test_login - тесты на "Вход"  
test_register.py - тесты на "Регистрация"  
test_exit.py - тесты на "Выход из аккаунта"  
conftest.py - файл с текстурами  
locators.py - файл с локаторами  
generator.py - файл с генератором логина и пароля  

### Краткое описание тестов
1. test_register_success - проверяет успешную регистрацию  
2. test_register_failed - проверяет ошибку для некорректного пароля  
3. test_login_main_button - проверяет вход по кнопке "Войти в аккаунт" на главной странице
4. test_login_personal_account_login_button - проверяет вход через кнопку "Личный кабинет"
5. test_login_register_login_button - проверяет вход через кнопку в форме регистрации
6. test_login_forgot_pass_login_button - проверяет вход через кнопку в форме восстановления пароля
7. test_click_account_not_authorized - проверяет переход по клику на "Личный кабинет" при отсутствии авторизации
8. test_click_account_authorized - проверяет переход по клику на "Личный кабинет" авторизированного пользователя
9. test_redirect_click_constructor - проверяет переход из личного кабинета в конструктор по клику на "Конструктор"
10. test_redirect_click_logo - проверяет переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
11. test_exit_account_click_exit_button - проверяет выход по кнопке "Выйти" в личном кабинете
12. test_constructor_buns_section - проверяет переход к разделу "Булки"
13. def test_constructor_sauces_section - проверяет переход к разделу "Соусы"
14. def test_constructor_fillings_section - проверяет переход к разделу "Начинки"
