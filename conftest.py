import logging
import requests
import yaml
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ваш существующий код

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser1 = testdata["browser"]

# Ваш существующий код

@pytest.fixture(scope="session")
def browser():
    if browser1 == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Ваш существующий код

# Определение функции test_post
def test_post(user_login):
    S = requests.Session()

    with open('config.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        address = data['address2']

    # Определите данные, которые вы хотите отправить в POST-запросе
    post_data = {
        'title': data['titlee'],
        'description': data['descriptionn'],
        'content': data['contentt']
    }

    # Определите заголовок с токеном X-Auth-Token
    headers = {'X-Auth-Token': user_login}

    # Выполните POST-запрос с использованием сессии requests
    response = S.post(url=address, headers=headers, data=post_data)

    # Выведите результат POST-запроса
    print(response.json())

# Пример вызова test_post с пользовательским логином
test_post('your_user_login_here')
