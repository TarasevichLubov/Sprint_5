from selenium.webdriver.common.by import By
from data import e_mail, passwd
from locators import account, field_email, field_password, but_enter, button_builder, logo


class TestPersonalAccount:
    # Переход по клику на «Личный кабинет».
    def test_user_click_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, account).click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Переход по клику на «Конструктор»
    def test_user_click_builder_in_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, field_email).send_keys(e_mail)
        driver.find_element(By.XPATH, field_password).send_keys(passwd)
        driver.find_element(By.XPATH, but_enter).click()
        driver.find_element(By.XPATH, account).click()
        driver.find_element(By.XPATH, button_builder).click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_user_logo_click(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, field_email).send_keys(e_mail)
        driver.find_element(By.XPATH, field_password).send_keys(passwd)
        driver.find_element(By.XPATH, but_enter).click()
        driver.find_element(By.XPATH, account).click()
        driver.find_element(By.XPATH, logo).click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
