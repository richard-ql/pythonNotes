# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exporters import JsonLinesItemExporter # JsonLinesItemExporter是逐行写入json文件
# JsonItemExporter是先存入列表在一次性写入json文件，内容大会占用很多内存


# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('subject_list.json', 'w', encoding='utf-8')
#
#     def open_spider(self, spider):
#         print('start spider......')
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(item, ensure_ascii=False)
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print('end spider........')

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('subject_list.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()

    def open_spider(self, spider):
        print('start spider......')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print('end spider........')
