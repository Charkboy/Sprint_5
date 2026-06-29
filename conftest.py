import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import BASE_URL
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from data_generator import generate_email, generate_password, generate_name

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password()
    name = generate_name()

    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAIN))

    personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
    personal_account.click()

    register_link = wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK))
    register_link.click()

    # Заполнение формы
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

    # Клик по кнопке "Зарегистрироваться"
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Ждём, когда появится поле ввода email (признак страницы входа)
    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

    return {"email": email, "password": password, "name": name}