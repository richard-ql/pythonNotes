# -*- coding: utf-8 -*-
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AutohomeItem


class Bmw5SpiderSpider(CrawlSpider):
    name = 'bmw5_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series-s41964/65.html']
    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series-s41964/65.+'),
             callback='parse_page',
             follow=True),
    )

    # def parse(self, response):
    #     title = response.xpath("//div[@class='uibox']")[1:]
    #     for item in title:
    #         image_name = item.xpath(".//div[@class='uibox-title']/a/text()").get()
    #         image_path = item.xpath(".//ul/li/a/img/@src").getall()
    #         image_url = [response.urljoin(image) for image in image_path]
    #         item = AutohomeItem(name=image_name, image_urls=image_url)
    #         yield item

    def parse_page(self, response):
        title = response.xpath("//div[@class='uibox']")[1:]
        s = ""
        s.isalnum()