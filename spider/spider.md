# Scrapy

## 安装和新建scrapy项目

1. pip install scrapy 
2. windows下需要安装 pip install pypiwin32
3. 新建项目scrapy startproject qsbk
4. cd qsbk
5. 新建spider: scrapy genspider qs_spider "qiushibaike.com"

## 项目配置

+ Obey robots.txt rules 

    `ROBOTSTXT_OBEY = False`

+ Override the default request headers:

```python
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en', 
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0;Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/78.0.3904.108 Mobile Safari/537.36'
    }
```
***
## 启动scrapy

+ scrapy crawl qs_spider

## 创建crawl spider

+ scrapy genspider -t crawl example example.com
