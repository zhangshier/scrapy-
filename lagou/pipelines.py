# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class LagouPipeline(object):
    def __init__(self):
          client = pymongo.MongoClient()
          db = client[settings['MONGODB_DBNAME']]
          self.post = db[settings['MONGODB_DOCNAME']]
    def process_item(self, item, spider):
        book_info =dict(item)
        self.post.insert(book_info)
        return item

