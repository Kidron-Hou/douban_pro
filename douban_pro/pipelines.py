# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .settings import mongo_db_collection,mongo_db_name,mongo_host,mongo_port


# 保存至mongoDB
class DoubanProPipeline(object):

    def __init__(self):
        host = mongo_host
        port = mongo_port
        db_name = mongo_db_name
        db_collection = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[db_name]
        self.post = mydb[db_collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert_one(data)
        return item
