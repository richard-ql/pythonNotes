# -*- coding: utf-8 -*-
import scrapy

from ..items import ArticleItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath('//a[@class="info"]/img/@src').get()
        author = response.xpath('//p[@class="oneline"]/text()').get()
        content = response.xpath("//div[@class='note-content']").getall()
        pub_time = response.xpath('//div[@class="article-info"]/div[@class="meta"]/span[2]/text()').get()
        origin_url = response.url
        yield ArticleItem(
            title=title,
            avatar=avatar,
            author=author,
            content=content,
            pub_time=pub_time,
            origin_url=origin_url)
