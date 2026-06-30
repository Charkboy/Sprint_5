from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__') and contains(@class, 'current')]//span")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")

class PersonalAccountLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")