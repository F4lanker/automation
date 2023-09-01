from selenium import webdriver

Chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=Chrome_options
    options.selonide.options.enableVNC = True

)
driver.get("http://www.google.com")
driver.quit()