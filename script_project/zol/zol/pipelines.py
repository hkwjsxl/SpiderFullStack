# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


class ZolPipeline:
    def open_spider(self, spider_name):
        self.conn = MongoClient(
            host='localhost',
            port=27017
        )
        self.db = self.conn['spider']

    def close_spider(self, spider_name):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        self.db['zoltu'].insert_one({
            'img_name': item['img_name'],
            'file_path': item['file_path']

        })
        return item


class DownImgPipline(ImagesPipeline):
    # 发送请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['src'])

    # 存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        file_path = 'zol_file'
        file_name = item['img_name']
        real_path = os.path.join(file_path, file_name)
        item['file_path'] = real_path
        return real_path

    # 对item进行更新
    def item_completed(self, results, item, info):
        print(results)
        return item



