import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (button_registration, field_reg_login, field_reg_email, field_reg_password, but_enter,
                      error_message_password_less_6)


class TestRegistration:
    def test_user_registration(self, driver, fake_password, fake_login, fake_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, button_registration)))
        driver.find_element(By.XPATH, field_reg_login).send_keys(fake_login)
        driver.find_element(By.XPATH, field_reg_email).send_keys(fake_email)
        driver.find_element(By.XPATH, field_reg_password).send_keys(fake_password)
        driver.find_element(By.XPATH, button_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, but_enter)))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    @pytest.mark.parametrize('password', [' ', '12345'])
    def test_password_exception_length_1_5(self, driver, fake_login, fake_email, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, button_registration)))
        driver.find_element(By.XPATH, field_reg_login).send_keys(fake_login)
        driver.find_element(By.XPATH, field_reg_email).send_keys(fake_email)
        driver.find_element(By.XPATH, field_reg_password).send_keys(password)
        driver.find_element(By.XPATH, button_registration).click()
        str_message = (driver.find_element
                       (By.XPATH, error_message_password_less_6).text)
        assert (str_message == 'Некорректный пароль')

    def test_password_exception_length_0(self, driver, fake_login, fake_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, button_registration)))
        driver.find_element(By.XPATH, field_reg_login).send_keys(fake_login)
        driver.find_element(By.XPATH, field_reg_email).send_keys(fake_email)
        driver.find_element(By.XPATH, field_reg_password).send_keys("")
        driver.find_element(By.XPATH, button_registration).click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'
