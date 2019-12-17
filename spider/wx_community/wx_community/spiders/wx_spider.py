# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxSpiderSpider(CrawlSpider):
    name = 'wx_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),follow=True),
        Rule(LinkExtractor(allow=r'.+article.+\.html'), callback='parse_article', follow=False)
    )

    def parse_article(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()
        article_content = response.xpath('//td[@id="article_content"]//text()').getall()
        print("".join(article_content))

