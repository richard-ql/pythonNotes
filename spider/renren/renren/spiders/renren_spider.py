# -*- coding: utf-8 -*-
import scrapy


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['renren.com']

    def start_requests(self):
        url = "http://www.renren.com"
        data = {'email': '',
                'password': ''}
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        url = "http://www.renren.com/701923119/profile"
        request = scrapy.Request(url, callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open('profile.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)
