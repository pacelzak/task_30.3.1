import email

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
load_dotenv()




@pytest.fixture(autouse=True)
def testing():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()

@pytest.fixture()
def go_my_pets(testing):

    wait = WebDriverWait(testing, 10)

    wait.until(EC.presence_of_element_located((By.ID, 'email')), message="Поле логин не стало кликабельной за 10 секунд").send_keys(os.getenv("email"))
    wait.until(EC.presence_of_element_located((By.ID, 'pass')), message="Поле пароль не стало кликабельной за 10 секунд").send_keys(os.getenv("password"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')),message="Кнопка входа не стала кликабельной за 10 секунд").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Мои питомцы"]')),message="Кнопка 'Мои питомцы' не стала кликабельной за 10 секунд").click()
    return testing

@pytest.fixture()
def pet_count(go_my_pets):

    driver = go_my_pets
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class=".col-sm-4 left"]')))
    return int(element.text.split('\n')[1].split(" ")[1])

