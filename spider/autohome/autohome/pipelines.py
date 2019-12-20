# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import datetime

from urllib import request
from .settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline


class AutohomePipeline(object):
    def __init__(self):
        self.image_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.image_file_path):
            os.mkdir(self.image_file_path)

    def process_item(self, item, spider):
        image_path = os.path.join(self.image_file_path, item['name'])
        if not os.path.exists(image_path):
            os.mkdir(image_path)
        for ul in item['url']:
            name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
            path = os.path.join(image_path, name)
            request.urlretrieve(ul, path)
        return item

class AutoHomeImagesPipelines(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(AutoHomeImagesPipelines, self).get_media_requests(item, info)
        for request in request_objs:
            request.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        path = super(AutoHomeImagesPipelines, self).file_path(request, response, info)
        category = request.item.get('name')
        category_path = os.path.join(IMAGES_STORE, category)
        image_name = path.replace('full/', '')
        image_path = os.path.join(category_path, image_name)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        return image_path
