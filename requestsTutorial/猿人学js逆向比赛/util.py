import re

def cookies_to_dict(cookies: str):
    result = ""
    for s in cookies:
        if s == "\n":
            s = "',\n'"
        result += s
    result = re.sub(':',"':'", result)
    result = result[2:].replace(" ", "") + '\''
    return result


if __name__=="__main__":
    headers = """
    Host: match.yuanrenxue.com
    Connection: keep-alive
    Accept: application/json, text/javascript, */*; q=0.01
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
    X-Requested-With: XMLHttpRequest
    Referer: http://match.yuanrenxue.com/match/3
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cookie: Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1604453586; sessionid=2tu7mbyk6fdkvd5dlmykxmbk573ixhdr; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1604453595
    """
    print(cookies_to_dict(headers))
