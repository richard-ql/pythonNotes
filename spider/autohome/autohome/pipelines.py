# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

from PIL import Image
from urllib import request

class AutohomePipeline(object):
    def process_item(self, item, spider):
        path = r'D:\pythonNotes\spider\autohome\bmw5-pic'
        name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        path = path + '\\' + name
        request.urlretrieve(item['url'], path)
        return item
