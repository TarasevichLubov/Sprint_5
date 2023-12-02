from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import e_mail, passwd
from locators import button_enter_account, but_enter, field_email, field_password, button_order, account, href_enter


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной странице
    def test_user_login_enter_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, button_enter_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, but_enter)))
        driver.find_element(By.XPATH, field_email).send_keys(e_mail)
        driver.find_element(By.XPATH, field_password).send_keys(passwd)
        driver.find_element(By.XPATH, but_enter).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, button_order)))
        button_orders = driver.find_element(By.XPATH, button_order).text
        assert button_orders == 'Оформить заказ'

    # Вход через кнопку «Личный кабинет»
    def test_user_login_enter_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, but_enter)))
        driver.find_element(By.XPATH, field_email).send_keys(e_mail)
        driver.find_element(By.XPATH, field_password).send_keys(passwd)
        driver.find_element(By.XPATH, but_enter).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, button_order)))
        button_orders = driver.find_element(By.XPATH, button_order).text
        assert button_orders == 'Оформить заказ'

    # Вход через кнопку на форме регистрации
    def test_user_login_enter_form_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, href_enter).click()
        driver.find_element(By.XPATH, field_email).send_keys(e_mail)
        driver.find_element(By.XPATH, field_password).send_keys(passwd)
        driver.find_element(By.XPATH, but_enter).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, button_order)))
        button_orders = driver.find_element(By.XPATH, button_order).text
        assert button_orders == 'Оформить заказ'

    # Вход через кнопку в форме восстановления пароля.
    def test_user_login_enter_form_forgot_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, href_enter).click()
        driver.find_element(By.XPATH, field_email).send_keys(e_mail)
        driver.find_element(By.XPATH, field_password).send_keys(passwd)
        driver.find_element(By.XPATH, but_enter).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, button_order)))
        button_orders = driver.find_element(By.XPATH, button_order).text
        assert button_orders == 'Оформить заказ'
