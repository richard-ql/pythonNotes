# -*- coding: utf-8 -*-
import scrapy
from ..items import AutohomeItem

class Bmw5SpiderSpider(scrapy.Spider):
    name = 'bmw5_spider'
    allowed_domains = ['https://car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/photolist/series/65/p1//']

    def parse(self, response):
        image_xpath = response.xpath("//div[@id='pa1']//img")
        for i in image_xpath:
            image_url = 'https:' + i.xpath('./@src').get()
            image_name = i.xpath('./@alt').get()
            item = AutohomeItem(name=image_name, url=image_url)
            yield item
