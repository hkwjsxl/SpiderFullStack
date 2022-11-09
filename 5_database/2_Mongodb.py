from pymongo import MongoClient


conn = MongoClient(host='localhost', port=27017)
db = conn.spider
collection = db.lianjia
data = collection.find()
print(data)

