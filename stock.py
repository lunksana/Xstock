# 基于 mongodb + python + Django 实现的库存系统
# 主要进行以下操作：
# 1. 查询库存
# 2. 调整库存，添加库存，减少库存
# 3. 简单的数据统计
# 4. 销售入库，客户管理，租赁管理
# ···

import os
import json
import pymongo
import time
from pprint import pprint

# 读取用户配置文件
try:
    with open('conf/config.json', 'r') as conf:
        config = json.load(conf)
except FileNotFoundError:
    exit('配置文件不存在')

# 对接数据库
# mongodb 无法直接创建空数据库，需要特别注意
try:
    client = pymongo.MongoClient(config['db_addr'], config['db_port'])
    db_list = client.list_database_names()
except pymongo.errors.ConnectionFailure:
    exit('数据库连接失败')

# 数据库操作
class sql():
    def __init__(self, db_name, col_name):
        self.db_name = db_name
        self.col_name = col_name
        self.db = client[db_name]
        self.col = self.db[col_name]
        if self.db.list_collections().count() == 0:
            self.db['init'].insert_one({'status': 1, 'time': time.time()})

# 查询数据，query数据支持模糊查询            
    def search(self, query: dict):
        return self.col.find(query)

# 增加数据    
    def add(self, data: dict):
        self.col.insert(data)

# 更新数据    
    def update(self, query: dict, data: dict):
        self.col.update(query, data)
    
# 删除数据
    def delete(self, query: dict):
        self.col.delete_one(query)

# python 网页构建
class html():
    def __init__(self, title, body):
        self.title = title
        self.body = body

