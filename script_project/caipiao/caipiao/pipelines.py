# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class CaipiaoPipeline:
    def open_spider(self, spider_name):
        self.conn = MongoClient(
            host='localhost',
            port=27017,
        )
        self.db = self.conn['spider']

    def close_spider(self, spider_name):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        print(item)
        self.db['caipiao2'].insert_one({
            'qihao': item['qihao'], 'red_ball': item['red_ball'], 'blue_ball': item['blue_ball']
        })
        return item
