import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators
from config import BASE_URL

class TestLogin:

    def test_login_main_button(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert "Оформить заказ" in driver.page_source

    def test_login_via_personal_account(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert "Оформить заказ" in driver.page_source

    def test_login_via_registration_form(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        # На странице регистрации есть ссылка "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert "Оформить заказ" in driver.page_source

    def test_login_via_forgot_password_form(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()
        # На странице восстановления пароля есть ссылка "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert "Оформить заказ" in driver.page_source