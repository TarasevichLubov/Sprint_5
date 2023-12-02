from selenium.webdriver.common.by import By
from locators import page_brad, page_souse, page_filling


class TestBuilder:
    # Переход к разделу "Булки"
    def test_user_click_bred(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        if 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, page_brad).get_attribute('class'):
            driver.find_element(By.XPATH, page_souse).click()
        driver.find_element(By.XPATH, page_brad).click()
        selected_class = driver.find_element(By.XPATH, page_brad).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in selected_class

    # Переход к разделу "Соусы"
    def test_user_click_souse(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        if 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, page_souse).get_attribute('class'):
            driver.find_element(By.XPATH, page_brad).click()
        driver.find_element(By.XPATH, page_souse).click()
        selected_class = driver.find_element(By.XPATH, page_souse).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in selected_class

    # Переход к разделу "Начинки"
    def test_user_click_filling(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        if 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, page_filling).get_attribute('class'):
            driver.find_element(By.XPATH, page_brad).click()
        driver.find_element(By.XPATH, page_filling).click()
        selected_class = driver.find_element(By.XPATH, page_filling).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in selected_class
