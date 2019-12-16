# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class QsSpiderSpider(scrapy.Spider):
    name = 'qs_spider'
    # allowed_domains = ['qiushibaike.com']
    allowed_domains = ['m.ishuo.cn']
    # start_urls = ['http://qiushibaike.com/text/page/2']
    start_urls = ['https://m.ishuo.cn/duanzi']
    base_urls = 'https://m.ishuo.cn/'

    def parse(self, response):
        subjects = response.xpath("//a[starts-with(@href, '/subject/')]")
        for item in subjects:
            url_sub = item.xpath("./@href").get()
            yield  {'url_sub': url_sub}