from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# создание объекта опций
chrome_options = Options()
capabilities = {
    "browserName": "chrome",
    "selenoid:options": {
        "enableVNC": True
    }
}

# установка опции
chrome_options.add_argument("start-maximized")
capabilities.update(chrome_options.to_capabilities())


# инициализация драйвера с использованием опций
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=chrome_options)
# Пример простого теста
driver.get("https://www.google.com")
print(driver.title)
