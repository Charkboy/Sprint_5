import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class TestConstructor:

    def test_switch_to_buns(self, driver):
        wait = WebDriverWait(driver, 10)
        element = driver.find_element(*MainPageLocators.BUNS_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        active = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert active.text == "Булки"

    def test_switch_to_sauces(self, driver):
        wait = WebDriverWait(driver, 10)
        element = driver.find_element(*MainPageLocators.SAUCES_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        active = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert active.text == "Соусы"

    def test_switch_to_fillings(self, driver):
        wait = WebDriverWait(driver, 10)
        element = driver.find_element(*MainPageLocators.FILLINGS_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        active = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert active.text == "Начинки"