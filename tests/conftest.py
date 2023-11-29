import random
import pytest
from tests.data import name
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def fake_login():
    login = name + str(random.randint(100, 999))
    return login


@pytest.fixture(scope="function")
def fake_email():
    email = name + str(random.randint(100, 999)) + '@testmail.ru'
    return email


@pytest.fixture(scope="function")
def fake_password():
    chars = '+-/*!&$#?=@\u003C\u003EabcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    num = 6
    f_password =''
    for i in range(num):
        f_password += random.choice(chars)
    return f_password
