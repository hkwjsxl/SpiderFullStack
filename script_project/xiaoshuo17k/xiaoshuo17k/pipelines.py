# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class Xiaoshuo17KPipeline:

    def open_spider(self, spider_name):
        self.conn = MongoClient(host='localhost', port=27017)
        self.db = self.conn['spider']

    def close_spider(self, spider_name):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        self.db['xiaoshuo17k'].insert_one({
            'num': item['num'],
            'kind': item['kind'],
            'book_name': item['book_name'],
        })
        print(item)
        return item
