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

## 使用scrapy shell 调式

+ scrapy shell "http://www.wxapp-union.com/article-5692-1.html"
+ response.xpath('//h1[@class="ph"]/text()').get()

## 调用scrapy files pipelines

1. 定义Item， 然后再item中定义2个属性，分别为file_urls 和 files， file_urls是用来存储需要下载文件的链接地址，是一个列表
类型。
2. 当文件下载完成后，会把下载文件的相关信息保存到item的files属性中，比如下载路径、文件的校验码等等。
3. 在配置文件settings.py中配置FILES_STORE=下载文件保存路径。
4. 启动files pipelines， 在ITEM_PIPELINES中配置 'scrapy.pipelines.files.FilesPipeline': 1。

## 调用scrapy images pipelines

1. 定义Item， 然后再item中定义2个属性，分别为image_urls 和 images， image_urls是用来存储需要下载文件的链接地址，是一个列
表类型。
2. 当文件下载完成后，会把下载文件的相关信息保存到item的images属性中，比如下载路径、文件的校验码等等。
3. 在配置文件settings.py中配置IMAGES_STORE=下载文件保存路径。
4. 启动files pipelines， 在ITEM_PIPELINES中配置 'scrapy.pipelines.images.ImagesPipeline': 1。
