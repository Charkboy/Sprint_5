import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from data_generator import generate_email, generate_password, generate_name

class TestRegistration:

    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAIN))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

        email = generate_email()
        password = generate_password()
        name = generate_name()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # После регистрации перенаправляет на страницу входа
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        assert driver.find_element(*LoginPageLocators.EMAIL_INPUT).is_displayed()

    def test_registration_invalid_password_error(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

        email = generate_email()
        name = generate_name()
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
        assert error.is_displayed()