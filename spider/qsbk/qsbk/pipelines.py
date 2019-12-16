# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('subject_list.json', 'w', encoding='utf-8')

    def open_spider(self, spider):
        print('start spider......')

    def process_item(self, item, spider):
        item_json = json.dumps(item, ensure_ascii=False)
        self.fp.write(item_json + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('end spider........')
