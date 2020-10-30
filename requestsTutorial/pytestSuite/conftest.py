import time
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def login_cookies():
    user_data_dir = r"--user-data-dir=C:\Users\issuser\AppData\Local\Google\Chrome\User Data"
    option = webdriver.ChromeOptions()
    option.add_argument(user_data_dir)
    driver = webdriver.Chrome(options=option, executable_path="../chromedriver.exe")
    driver.get("https://www.cnblogs.com/")
    time.sleep(3)
    cookies = driver.get_cookies()
    print(cookies)
    driver.quit()
    return cookies
