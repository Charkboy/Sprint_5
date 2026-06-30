import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, PersonalAccountLocators, LoginPageLocators
from config import BASE_URL

class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK))
        assert "Профиль" in driver.page_source

    def test_go_to_constructor_from_personal_account(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK))

        driver.find_element(*PersonalAccountLocators.CONSTRUCTOR_LINK).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert "Оформить заказ" in driver.page_source

    def test_go_to_main_via_logo_from_personal_account(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK))

        driver.find_element(*PersonalAccountLocators.LOGO).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert "Оформить заказ" in driver.page_source

    def test_logout_from_personal_account(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK))

        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        assert driver.find_element(*LoginPageLocators.EMAIL_INPUT).is_displayed()