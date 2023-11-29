from selenium.webdriver.common.by import By


class TestBuilder:
    # Переход к разделу "Булки"
    def test_user_click_bulka(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        if 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                    ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[1]").get_attribute('class'):
            driver.find_element(By.XPATH,
                                ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]").click()
        driver.find_element(By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[1]").click()
        selected_class = driver.find_element(By.XPATH,
                    ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[1]").get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in selected_class

    # Переход к разделу "Соусы"
    def test_user_click_souse(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        if 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                    ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]").get_attribute('class'):
            driver.find_element(By.XPATH,
                                     ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]").click()
        driver.find_element(By.XPATH,
                                     ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]").click()
        selected_class = driver.find_element(By.XPATH,
                    ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]").get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in selected_class

    # Переход к разделу "Начинки"
    def test_user_click_filling(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        if 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                     ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]").get_attribute('class'):
            driver.find_element(By.XPATH,
                             ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]").click()
        driver.find_element(By.XPATH,
                                    ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]").click()
        selected_class = driver.find_element(By.XPATH,
                            ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]").get_attribute(
                    'class')
        assert 'tab_tab_type_current__2BEPc' in selected_class
