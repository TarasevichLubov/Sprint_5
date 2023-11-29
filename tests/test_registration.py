import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_user_registration(self, driver, fake_password, fake_login, fake_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Зарегистрироваться']")))
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(fake_login)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(fake_email)
        driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(fake_password)
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//main/div/form/button[text()='Войти']")))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    @pytest.mark.parametrize('password', [' ', '12345'])
    def test_password_exception_length_1_5(self, driver, fake_login, fake_email, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Зарегистрироваться']")))
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(fake_login)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(fake_email)
        driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(password)
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        str_message = (driver.find_element
                       (By.XPATH, ".//fieldset[3]//p[@class='input__error text_type_main-default']").text)
        assert (str_message == 'Некорректный пароль')

    def test_password_exception_length_0(self, driver, fake_login, fake_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, ".//button[text()='Зарегистрироваться']")))
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(fake_login)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(fake_email)
        driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys("")
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'
