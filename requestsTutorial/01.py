# 百度ip接口查询

"""
1.response的返回内容还有其它更多信息

-- r.status_code     #响应状态码
-- r.content           #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
-- r.headers          #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
-- r.json()             #Requests中内置的JSON解码器
-- r.url                  # 获取url
-- r.encoding         # 编码格式
-- r.cookies           # 获取cookie
-- r.raw                #返回原始响应体
-- r.text               #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
-- r.raise_for_status() #失败请求(非200响应)抛出异常
"""
import json
import requests
import unittest

class ApiTest(unittest.TestCase):
    def test_baiduIP(self):
        url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php"
        payload = {"query": "223.223.190.193", "resource_id": "5809"}
        r = requests.get(url=url, params=payload)
        # result = json.loads(r.content)
        result = r.json()
        location = result["Result"][0]["DisplayData"]["resultData"]["tplData"]["location"]
        self.assertEqual(r.status_code, 200)
        self.assertEqual(location, "北京市北京 电信")
        # 验证响应时间小于200ms, elapsed指发送requests第一个字节 到 解析完响应头域的时间差，并不包括处理响应body的时间。
        self.assertLessEqual(r.elapsed.total_seconds(), 0.5, msg="响应时间大于500ms")

    def test_tencentCourse(self):
        url = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list"
        payload = {"cid":"317690","count":"10","page":"0", "filter_rating":"0", "r":"0.3070749989993329"}
        # 腾讯课堂 headers 必须带Referer
        headers = {"Referer": "https://ke.qq.com/course/317690?course_id=317690"}
        r = requests.get(url, params=payload, headers=headers)
        # result = json.loads(r.content, encoding="utf-8")
        result =r.json()
        totalnum = result["result"]["total_num"]
        self.assertEqual(r.status_code, 200)
        self.assertEqual(totalnum, 151)
        # 验证响应时间小于200ms, elapsed指发送requests第一个字节 到 解析完响应头域的时间差，并不包括处理响应body的时间。
        self.assertLessEqual(r.elapsed.total_seconds(), 0.5, msg="响应时间大于500ms")
