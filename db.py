# 库存系统数据库使用mongodb
# 使用pymongo对mongodb进行操作
# 每个库房对应一个数据库，相关的数据内容在相应的数据包中添加

import pymongo
import json

# 读取用户配置文件
with open('conf/config.json', 'r') as conf:
    config = json.load(conf)

# 基于配置文件信息判断是否已经进行初始化
if config['init'] != 1:
    print("请先进行初始化\n")
    exit()
else:
    addr = config['db_addr']
    port = config['db_port']


# 对数据库进行操作
class mgdb:
    def __init__(self, db_name, col_name):
        self.client = pymongo.MongoClient(addr, port)
        self.db = self.client[db_name]
        self.col = self.db[col_name]
    
    # 新建数据库
    def new(self, db_name):
        self.client.create_database(db_name)
    
        
    # 查询数据
    def find(self, condition):
        return self.col.find(condition)
    
    # 插入数据
    def insert(self, data):
        self.col.insert(data)
        
    # 更新数据
    def update(self, condition, data):
        self.col.update(condition, data)
    
    # 删除数据
    def delete(self, condition):
        self.col.remove(condition)
