import unittest
import requests
from requests.cookies import RequestsCookieJar
"""
二、cookie组成结构

1.用抓包工具fidller只能看到cookie的name和value两个参数，实际上cookie还有其它参数

2.以下是一个完整的cookie组成结构

cookie ={u'domain': u'.cnblogs.com',
            u'name': u'.CNBlogsCookie',
            u'value': u'xxxx',
            u'expiry': 1491887887,
            u'path': u'/',
            u'httpOnly': True,
            u'secure': False}

name：cookie的名称

value：cookie对应的值，动态生成的

domain：服务器域名

expiry：Cookie有效终止日期

path：Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie

httpOnly：防脚本攻击

secure:在Cookie中标记该变量，表明只有当浏览器和Web Server之间的通信协议为加密认证协议时，

浏览器才向服务器提交相应的Cookie。当前这种协议只有一种，即为HTTPS。"""


class BoKeYuanTest(unittest.TestCase):
    def test_login(self):
        login_url = "https://home.cnblogs.com/"
        session = requests.session()
        session.headers = {
                "authority": "home.cnblogs.com",
                "method": "GET",
                "path": "/",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                "cache-control": "max-age=0",
                "cookie": "_ga=GA1.2.1015123569.1555483644; __utma=2642927.1015123569.1555483644.1564364476.1564364476.1; Hm_lvt_cc496f1e302e6c1e8e8c733c9495ab82=1593424414; __gads=ID=2009e6969e861338:T=1602743285:S=ALNI_MaIBx7uY28ek5E-nVbtzx5D6IuScA; _gid=GA1.2.348293854.1603682541; .Cnblogs.AspNetCore.Cookies=CfDJ8AHUmC2ZwXVKl7whpe9_lasOZ-jQogrDjxwnKNRVSrNJkGP2CeDqOBzmkg6-TzEZTQaushx0bpOk58Mo8gGas4Hz-Hj2h28aQVxrmRF0N5HPug13JRnX-9u7_aIXbUjvVth-fo7zxMeXqjo60ZzRltykayQN8XmwA7B0a-0CoF_47Vb92rIv3V4_QEr3SXevI5DUakbaUn69TzlY3vio22wY3vuYO-y2cnXYZnK341GMSEuRC-9LUYkt3gpMEKktlXxIK-cgSKHSaP-amTyjWIXWdaPz3TFrffp3QcRjY3Cj-H-G0DQi_rjt4ru07Qjd2gj3QBxdE22etIO8QzcXEbTH2rv2mL-dQj2ojJtML_eYgur_NKE5jmteXpDDvQ2wseKgPHi99SuxJTH11eeSGqpTwEB6fEVq8mLLoIiPg9uzfEuwaz79haXxdf0XJ_imYEEMZLBtcN8CfQ3NRVV0QVlVzhAKvCeZBrmArsNTYSmLIWA5mGx5lpCyN3zhuZTDT-JNDauVY6AEFwGKWh_sHA5Glg0fBwioVo5Cku4kD2kpK6x-3wylmnPSunp6xCW7Sw; .CNBlogsCookie=13BCEE5ACC2EC8910F24F9E7D7130B06942358D33D08E3FCC7ED1CA0AFE6DA0821A929E377B03E8D544FB613312F5F20645F74382C5BCD6ADDE46A1C43E8378C83C7B17EDB9C5D2FD6F7DBE2D9BFB08BA5DA9485",
                "referer": "https://account.cnblogs.com/signin?returnUrl=https:%2F%2Fhome.cnblogs.com%2F",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-site",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        r = session.request("GET",login_url)
        print(r.content.decode("utf-8"))
        session.headers.update({"path": "/news/"})
        session.headers.update({"referer": "https://ing.cnblogs.com/u/2191270"})
        news_url = "https://home.cnblogs.com/news/"
        r = session.request("GET", news_url)
        print(r.content.decode("utf-8"))
