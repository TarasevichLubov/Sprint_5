from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import e_mail, passwd
from locators import field_email, field_password, but_enter, account, button_exit


class TestUserLogout:
    # Выход по кнопке «Выйти» в личном кабинете.
    def test_user_enter_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, field_email).send_keys(e_mail)
        driver.find_element(By.XPATH, field_password).send_keys(passwd)
        driver.find_element(By.XPATH, but_enter).click()
        driver.find_element(By.XPATH, account).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, button_exit)))
        driver.find_element(By.XPATH, button_exit).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, but_enter)))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
