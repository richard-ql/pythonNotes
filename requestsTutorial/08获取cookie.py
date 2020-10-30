"""
Selenium启动浏览器时，默认是打开一个新用户，不会加载原有的配置以及插件。但有些时候我们可能需要加载默认配置。
1、在Chrome浏览器的地址栏输入：chrome://version/，查看个人资料路径并复制路径
2、加载配置数据

加载的用户配置路径后面的Default不需要，不然还是打开一个新用户。
在执行脚本时，确保没有谷歌浏览器打开，不然会报selenium.common.exceptions.WebDriverException:
Message: unknown error: Chrome failed to start: crashed

1、打开Firefox浏览器，进入右上角的帮助>故障排除信息，查看浏览器配置文件路径并复制此路径

"""
import time
import requests
from selenium import webdriver


class TestGetCookie:
    def test_get_cookie(self):
        user_data_dir = r"--user-data-dir=C:\Users\issuser\AppData\Local\Google\Chrome\User Data"
        option = webdriver.ChromeOptions()
        option.add_argument(user_data_dir)
        driver = webdriver.Chrome(chrome_options=option, executable_path="chromedriver.exe")
        driver.get("https://www.cnblogs.com/")
        time.sleep(3)
        cookies = driver.get_cookies()
        print(cookies)
        driver.quit()

        # firefox
        # # 配置文件路径
        # profile_path = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hjs10ncm.default'
        # # 加载配置数据
        # profile = webdriver.FirefoxProfile(profile_path)
        # # 启动浏览器配置
        # driver = webdriver.Firefox(firefox_profile=profile,
        #                            executable_path=r'D:\coship\Test_Framework\drivers\geckodriver.exe')
        # driver.get(r'https://www.cnblogs.com/')
        # driver.quit()

