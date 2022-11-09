from redis import StrictRedis


class Tianya2Pipeline:
    def process_item(self, item, spider):
        content = item['texts']
        if self.conn.sismember('ty_content', content):
            print('数据已存在！')
            pass
        else:
            self.conn.sadd('ty_content', content)
        return item

    def open_spider(self, spider):
        self.conn = StrictRedis(password='20020224.', db=1)

    def close_spider(self, spider):
        if self.conn:
            self.conn.close()


