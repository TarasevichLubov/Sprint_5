from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import e_mail, passwd


class TestUserLogout:

    #Выход по кнопке «Выйти» в личном кабинете.
    def test_user_enter_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(e_mail)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(passwd)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        driver.find_element(By.XPATH, "//div/header/nav/a[@class = 'AppHeader_header__link__3D_hX']").click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//div/nav/ul/li[3]/button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//div/nav/ul/li[3]/button[text()='Выход']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/form/button[text()='Войти']")))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
