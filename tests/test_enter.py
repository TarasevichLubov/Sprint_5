from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import e_mail, passwd


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной странице
    def test_user_login_enter_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(e_mail)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(passwd)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))
        button_zakaz = driver.find_element(By.XPATH,".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert button_zakaz == 'Оформить заказ'
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//ul/li[3]/button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//ul/li[3]/button[text()='Выход']").click()

    # Вход через кнопку «Личный кабинет»
    def test_user_login_enter_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(e_mail)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(passwd)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))

        button_zakaz = (driver.find_element
            (By.XPATH, ".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text)
        assert button_zakaz == 'Оформить заказ'

        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//ul/li[3]/button[text()='Выход']").click()

    # Вход через кнопку на форме регистрации
    def test_user_login_enter_form_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(e_mail)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(passwd)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))

        button_zakaz = driver.find_element(By.XPATH, ".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert button_zakaz == 'Оформить заказ'
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//ul/li[3]/button[text()='Выход']").click()

    # Вход через кнопку в форме восстановления пароля.
    def test_user_login_enter_form_forgot_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(e_mail)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(passwd)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH,
             ".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))

        button_zakaz = driver.find_element(By.XPATH,
                                               ".//section[2]//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert button_zakaz == 'Оформить заказ'

        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//ul/li[3]/button[text()='Выход']").click()
