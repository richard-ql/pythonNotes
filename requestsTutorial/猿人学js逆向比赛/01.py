"""
http://match.yuanrenxue.com/match/12
"""

import base64
import requests

def get_numbers(page: int) -> int:
    m = base64.b64encode(("yuanrenxue"+ str(page)).encode("utf-8"))
    m = m.decode("utf-8")
    url = f"http://match.yuanrenxue.com/api/match/12?page={str(page)}&m={m}"
    print(url)
    headers = {
        "User-Agent": "yuanrenxue.project"
    }
    r = requests.request("GET", url=url, headers=headers)
    assert r.status_code == 200
    content = r.json()
    assert content['state'] == 'success'
    print(content)
    ans = 0
    for el in content['data']:
        ans += int(el['value'])
    return ans


if __name__=="__main__":
    total = 0
    for i in range(1, 6):
        total += get_numbers(i)
    print(total)
