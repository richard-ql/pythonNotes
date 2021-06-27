import requests
from collections import Counter

def get_page(page_num:str) -> dict:
    session = requests.session()
    session.headers = {
        'Host':'match.yuanrenxue.com',
        'Connection':'keep-alive',
        'Accept':'application/json,text/javascript,*/*;q=0.01',
        'User-Agent':'Mozilla/5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.111Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'http//match.yuanrenxue.com/match/3',
        'Accept-Encoding':'gzip,deflate',
        'Accept-Language':'zh-CN,zh;q=0.9'
    }
    url = f"http://match.yuanrenxue.com/api/match/3?page={page_num}"
    url_logo = "http://match.yuanrenxue.com/logo"
    session.post(url_logo)
    r = session.get(url=url)
    return r.json()

def main():
    result = []
    for i in range(1, 6):
        content = get_page(str(i))
        for d in content.get("data"):
            result.append(d.get("value"))
    return Counter(result).most_common(1)

if __name__=="__main__":
    r = main()
    print(r)
