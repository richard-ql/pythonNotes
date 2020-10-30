import requests
from requests.cookies import RequestsCookieJar


class TestBlog:
    def test_login_sucess(self,login_cookies):
        session = requests.session()
        c = RequestsCookieJar()
        for cookie in login_cookies:
            c.set(cookie['name'], cookie['value'])
        session.cookies.update(c)
        r = session.request("GET", "https://home.cnblogs.com/followers/")
        content = r.content.decode("utf-8")
        assert "qinla的主页" in content
