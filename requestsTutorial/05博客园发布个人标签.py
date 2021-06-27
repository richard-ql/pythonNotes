import requests


session = requests.session()
url = "https://ing.cnblogs.com/ajax/ing/Publish"
session.headers = {
    "authority": "ing.cnblogs.com",
    "method": "POST",
    "path": "/ajax/ing/Publish",
    "scheme": "https",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "_ga=GA1.2.1015123569.1555483644; __utma=2642927.1015123569.1555483644.1564364476.1564364476.1; Hm_lvt_cc496f1e302e6c1e8e8c733c9495ab82=1593424414; __gads=ID=2009e6969e861338:T=1602743285:S=ALNI_MaIBx7uY28ek5E-nVbtzx5D6IuScA; _gid=GA1.2.348293854.1603682541; .Cnblogs.AspNetCore.Cookies=CfDJ8AHUmC2ZwXVKl7whpe9_lasOZ-jQogrDjxwnKNRVSrNJkGP2CeDqOBzmkg6-TzEZTQaushx0bpOk58Mo8gGas4Hz-Hj2h28aQVxrmRF0N5HPug13JRnX-9u7_aIXbUjvVth-fo7zxMeXqjo60ZzRltykayQN8XmwA7B0a-0CoF_47Vb92rIv3V4_QEr3SXevI5DUakbaUn69TzlY3vio22wY3vuYO-y2cnXYZnK341GMSEuRC-9LUYkt3gpMEKktlXxIK-cgSKHSaP-amTyjWIXWdaPz3TFrffp3QcRjY3Cj-H-G0DQi_rjt4ru07Qjd2gj3QBxdE22etIO8QzcXEbTH2rv2mL-dQj2ojJtML_eYgur_NKE5jmteXpDDvQ2wseKgPHi99SuxJTH11eeSGqpTwEB6fEVq8mLLoIiPg9uzfEuwaz79haXxdf0XJ_imYEEMZLBtcN8CfQ3NRVV0QVlVzhAKvCeZBrmArsNTYSmLIWA5mGx5lpCyN3zhuZTDT-JNDauVY6AEFwGKWh_sHA5Glg0fBwioVo5Cku4kD2kpK6x-3wylmnPSunp6xCW7Sw; .CNBlogsCookie=13BCEE5ACC2EC8910F24F9E7D7130B06942358D33D08E3FCC7ED1CA0AFE6DA0821A929E377B03E8D544FB613312F5F20645F74382C5BCD6ADDE46A1C43E8378C83C7B17EDB9C5D2FD6F7DBE2D9BFB08BA5DA9485",
    "origin": "https://ing.cnblogs.com",
    "referer": "https://ing.cnblogs.com/",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
payload = {
    "content": "4567",
    "publicFlag": 0,
}
# r = session.post(url, data=payload)
# print(r.json())
