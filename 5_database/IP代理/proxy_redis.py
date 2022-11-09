import random
import redis


class ProxyRedis:
    def __init__(self):
        self.red = redis.StrictRedis(
            host='localhost',
            port=6379,
            password='20020224.',
            db=1,
            charset='utf8',
            decode_responses=True,
        )

    def add_proxy_id(self, ip):
        # 是否已经存在
        if not self.red.zscore('proxy_ip', ip):  # 提数score
            self.red.zadd('proxy_ip', {ip: 10})
            print('采集到ip地址：', ip)
        else:
            print('ip地址已存在：', ip)

    def set_max_score(self, ip):
        self.red.zadd('proxy_ip', {ip: 20})  # 已存在在添加会覆盖score

    def get_all_proxy(self):
        return self.red.zrange('proxy_ip', 0, -1)

    def desc_incrby(self, ip):
        # 查询
        score = self.red.zscore('proxy_ip', ip)
        if score > 0:
            self.red.zincrby('proxy_id', -1, ip)  # -1
        else:
            self.red.zrem('proxy_id', ip)  # 删除

    def get_proxy(self):
        ips = self.red.zrangebyscore('proxy_id', 20, 20, 0, -1)
        if ips:
            return random.choice(ips)
        else:
            ips = self.red.zrangebyscore('proxy_id', 11, 19, 0, -1)
            if ips:
                return random.choice(ips)
            print('没了~~~')
            return



