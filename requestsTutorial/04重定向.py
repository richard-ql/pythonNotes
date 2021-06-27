"""
一、重定向

1. (Redirect)就是通过各种方法将各种网络请求重新定个方向转到其它位置,从地址A跳转到地址B了。

2.重定向状态码:

--301 redirect: 301 代表永久性转移(Permanently Moved)

--302 redirect: 302 代表暂时性转移(Temporarily Moved )
"""


import requests


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
r = requests.get(url, headers=headers, allow_redirects=False)
print(r.status_code)
new_urls = r.headers["Location"]
print(new_urls)
