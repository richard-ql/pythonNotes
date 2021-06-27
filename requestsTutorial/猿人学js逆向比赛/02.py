# http://match.yuanrenxue.com/match/2
import requests
import execjs
import time


def get_page(cookie):
    url = f"http://match.yuanrenxue.com/api/match/2"
    c = "Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1604040834; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1604283263,1604367945,1604368948,1604369964; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1604369992;"
    headers = {
        "Host": "match.yuanrenxue.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://match.yuanrenxue.com/match/2",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": c + cookie
    }
    response = requests.request("GET", url=url, headers=headers)
    return response.json()

def get_cookie():
    with open("02cookie.js", encoding="utf-8", mode="r") as f:
        js_data = f.read()
    return execjs.compile(js_data).call("getCookie")

def main():
    # for i in range(1, 6):
    c = get_cookie()
    print(str(c))
    res = get_page(str(c))
    print(res)
    time.sleep(1)

if __name__=="__main__":
    # main()
    print(get_cookie())