import redis


red = redis.StrictRedis(
    host='localhost',
    port=6379,
    password='20020224.',
    db=0,
    decode_responses=True,
    charset='utf8',
)
# red.set('name', 'alex')
# red.mset({'age': 18, 'wife': 'none'})
# res = red.get('name')
# print(res)

# res = red.mget('name', 'age', 'wife')
# print(res)


# red.sadd('set', 'yan')
# res = red.scard('set')  # 数目
# print(res)
# res = red.smembers('set')  # 值
# print(res)


# res = red.rpush('push', 1, 2, 3)
# print(res)
# print(red.llen('push'))
# print(red.lrange('push', 0, -1))





