# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from pymysql.cursors import DictCursor
from pymongo import MongoClient
import redis


class GamePipeline:
    def open_spider(self, spider_name):
        self.f = open('game.csv', 'w', encoding='utf-8')

    def close_spider(self, spider_name):
        self.f.close()

    def process_item(self, item, spider):
        # print(item)
        self.f.write(item['title'])
        self.f.write(',')
        self.f.write(item['time'])
        self.f.write('\n')
        return item

class MySQLPipeline:
    def open_spider(self, spider_name):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='20020224.',
            charset='utf8',
            db='spider'
        )

    def close_spider(self, spider_name):
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cursor = self.conn.cursor(cursor=DictCursor)
            title = item["title"]
            time = item["time"]
            sql = f'insert into game4399(title, time) values (%s, %s)'
            self.cursor.execute(sql, (title, time))
        except Exception as e:
            print(e)
            if self.conn:
                self.conn.close()
            if self.cursor:
                self.cursor.close()
        return item


class MongoPipeline:
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
        title = item["title"]
        time = item["time"]
        self.db['game4399'].insert_one({'title': title, 'time': time})
        return item


class RedisPipeline:
    def open_spider(self, spider_name):
        self.red = redis.StrictRedis(
            db=0,
            password='20020224.',
            decode_responses=True
        )

    def close_spider(self, spider_name):
        if self.red:
            self.red.close()

    def process_item(self, item, spider):
        title = item["title"]
        time = item["time"]
        self.red.lpush('game4399', title, time)
        return item

