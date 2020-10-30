"""
requests本身虽然简单的方法post Mulitpart-Encoder文件，但是requests是先读取文件到内存，
然后在构造请求发送出去。
如果要发送一个非常大的文件 作为 multipart/form-data 请求时，为了避免把大文件读取到内存，
就需要用到数据流的方式，requests不支持这种方式，可以用第三方包requests_toolbelt
"""
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class TestUploadP:
    def test_upload(self):
        session = requests.session()
        url_upload = "https://upload.cnblogs.com/avatar/upload"
        # 上传个人头像, 此处有一个大坑，就是不能再headers里填写content-type
        session.headers.clear()
        session.headers = {
            "Host": "upload.cnblogs.com",
            "method": "POST",
            "path": "/avatar/upload",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            # "content-type": "multipart/form-data; boundary=----WebKitFormBoundary3nxbbQab7opAEl6d",
            "cookie": "_ga=GA1.2.1015123569.1555483644; __utma=2642927.1015123569.1555483644.1564364476.1564364476.1; Hm_lvt_cc496f1e302e6c1e8e8c733c9495ab82=1593424414; __gads=ID=2009e6969e861338:T=1602743285:S=ALNI_MaIBx7uY28ek5E-nVbtzx5D6IuScA; _gid=GA1.2.348293854.1603682541; .Cnblogs.AspNetCore.Cookies=CfDJ8AHUmC2ZwXVKl7whpe9_lasOZ-jQogrDjxwnKNRVSrNJkGP2CeDqOBzmkg6-TzEZTQaushx0bpOk58Mo8gGas4Hz-Hj2h28aQVxrmRF0N5HPug13JRnX-9u7_aIXbUjvVth-fo7zxMeXqjo60ZzRltykayQN8XmwA7B0a-0CoF_47Vb92rIv3V4_QEr3SXevI5DUakbaUn69TzlY3vio22wY3vuYO-y2cnXYZnK341GMSEuRC-9LUYkt3gpMEKktlXxIK-cgSKHSaP-amTyjWIXWdaPz3TFrffp3QcRjY3Cj-H-G0DQi_rjt4ru07Qjd2gj3QBxdE22etIO8QzcXEbTH2rv2mL-dQj2ojJtML_eYgur_NKE5jmteXpDDvQ2wseKgPHi99SuxJTH11eeSGqpTwEB6fEVq8mLLoIiPg9uzfEuwaz79haXxdf0XJ_imYEEMZLBtcN8CfQ3NRVV0QVlVzhAKvCeZBrmArsNTYSmLIWA5mGx5lpCyN3zhuZTDT-JNDauVY6AEFwGKWh_sHA5Glg0fBwioVo5Cku4kD2kpK6x-3wylmnPSunp6xCW7Sw; .CNBlogsCookie=13BCEE5ACC2EC8910F24F9E7D7130B06942358D33D08E3FCC7ED1CA0AFE6DA0821A929E377B03E8D544FB613312F5F20645F74382C5BCD6ADDE46A1C43E8378C83C7B17EDB9C5D2FD6F7DBE2D9BFB08BA5DA9485; _gat=1",
            "origin": "https://account.cnblogs.com",
            "referer": "https://account.cnblogs.com/settings/account/avatar",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": "CfDJ8AHUmC2ZwXVKl7whpe9_latkemwqbrb1RSDqwjp27uhF_yhNJH_K_TqmXXFdnUtV04AS4iIe7xiVIz1diFjyoiuCWawXTwAUwmWy8RSN_dA_-mSEIeSatiA2nma1kHW6XFNWtWdCdXrdqPto--kCQPDuP1BeXD2GAWWl_7-tzFfHog1TdSdoTQ80mOSTIGB4pg"
        }
        m = MultipartEncoder(
            fields={
                "avatar": ("docker.jpg", open("../docker.jpg", "rb"), "image/png")
            }
        )
        # 多文件上传用list
        # m = MultipartEncoder(
        #     fields=[
        #         ('source', ('f1.ext', f1, 'application/x-example-mimetype'),
        #          ('source', ('f2.ext', f2, 'application/x-example-mimetype'),
        #     ]
        # )
        r = session.request("POST",url_upload,data=m,headers={"Content-type": m.content_type})
        content = r.json()
        assert content["Success"] is True
        assert r.status_code == 200
