

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




def test_count_pet(go_my_pets, pet_count):
    """Функция проверяет, что количество строк таблицы соответствует количеству питомцев
    в блоке статистики пользователя"""

    driver = go_my_pets
    wait = WebDriverWait(driver, 10)
    table = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    assert len(table) == pet_count, "Количество питомцев не совпадает"

def test_count_pet_with_photos(go_my_pets, pet_count):

    """Функция проверяет, что не менее 50% питомцев имеют фотографии"""
    driver = go_my_pets
    table = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr img')
    counter = 0
    for img in table:
        if img.get_attribute('src') == "":
            counter += 1
    assert (counter * 100) / int(pet_count) <= 50, f"Количество питомцев без фото {(counter * 100) / int(pet_count)}%"


def test_check_attribute(go_my_pets):

    """Функция проверяет, что у всех питомцев есть имя, возраст и порода"""
    driver = go_my_pets
    table = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    for pet in range(len(table)):
        data_pet = table[pet].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3, "Не у всех питомцев есть три параметра"

def test_unique_names(go_my_pets, pet_count):

    """Функция проверяет, что у всех питомцев разные имена."""
    driver = go_my_pets
    table = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    list_name = []
    for pet in range(len(table)):
        name = table[pet].text.replace('\n', '').replace('×', '').split(' ')[0].upper()
        if name not in list_name:
            list_name.append(name)
    assert len(list_name) == pet_count, "Не у всех питомцев разные имена"




def test_unique_pets(go_my_pets, pet_count):

    driver = go_my_pets
    table = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    list_pets = []
    for pet in range(len(table)):
        name = table[pet].text.replace('\n', '').replace('×', '').split(' ')
        if name not in list_pets:
            list_pets.append(name)
    assert len(list_pets) == pet_count, "Не все питомцы уникальны"







