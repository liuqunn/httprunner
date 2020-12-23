import requests
import json
# import pymysql
# import os
# import time
# import sys
# import threading
# from dbutils.pooled_db import PooledDB,SharedDBConnection
# import csv

def return_token(username):
    url="https://b2.51ias.com/api.php"
    data={
    "password": "96e79218965eb72c92a549dd5a330112",
    "pid": "gloudphone",
    "type": "Android",
    "version": "420200722",
    "username": username,
    "deviceid": "R_vY1M5SOKlWTF1wHT0XPaC9SeA7H05j",
    "language": "zh",
    "lz": "73ccf97c9761f465e965427845ac2e8e",
    "hwdeviceid": "cf7c6cf6-8604-49e7-a748-5a733cf77c07",
    "m": "User",
    "a": "login",
    }
    res=requests.get(url,params=data)
    # print(res.text)
    res_json = json.loads(res.text)
    # print(res_json["user_info"]["device_info"]["login_token"])
    token = res_json["user_info"]["device_info"]["login_token"]
    return token

def judgment_ret(res):
    ret = json.loads(res.text)["ret"]
    if ret == "100000001":
        ret = 0
    elif ret == "100313003":
        ret = 0

    return ret

# return_token()

#使用locust做性能测试的时候，查询数据库时间会很长导致报错，所以不使用了
# POOL = PooledDB(
#     # 使用链接数据库的模块
#     creator=pymysql,
#     # 连接池允许的最大连接数，0和None表示不限制连接数
#     maxconnections=0,
#     # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
#     mincached=0,
#     # 链接池中最多闲置的链接，0和None不限制
#     maxcached=5,
#     # 链接池中最多共享的链接数量，0和None表示全部共享。
#     # 因为pymysql和MySQLdb等模块的 threadsafety都为1，
#     # 所有值无论设置为多少，maxcached永远为0，所以永远是所有链接都共享。
#     maxshared=0,
#     # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
#     blocking=True,
#     # 一个链接最多被重复使用的次数，None表示无限制
#     maxusage=None,
#     # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
#     setsession=[],
#     # ping MySQL服务端，检查是否服务可用。
#     #  如：0 = None = never, 1 = default = whenever it is requested,
#     # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
#     ping=0,
#     # 主机地址
#     host='rr-bp1c02r68219ep2kio.mysql.rds.aliyuncs.com',
#     # 端口
#     port=3306,
#     # 数据库用户名
#     user='dsyread0510',
#     # 数据库密码
#     password='PP_dhjh_234_q',
#     # 数据库名
#     database='cloudgaming',
#     # 字符编码
#     charset='utf8'
# )

# def get_token(account_id):
#     # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
#     # 否则则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
#     # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
#     # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
#     # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。

#     # 创建连接,POOL数据库连接池中          ,device_uuid,hwdeviceid
#     conn = POOL.connection()
#     # 创建游标
#     cursor = conn.cursor()
#     # SQL语句
#     sql = "SELECT login_token FROM `july_device` where bind_account = %d ORDER BY last_login_time DESC"%(int(account_id))
#     cursor.execute(sql)
#     # 执行结果
#     token = cursor.fetchall()[0][0]
#     # token = {}
#     # token["logintoken"] = result[0]
#     # token["device"] = result[1]
#     # token["hwdeviceid"] = result[2]
#     # 将conn释放,放回连接池
#     conn.close()
#     return token

# def get_deviceid(account_id):
#     # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
#     # 否则则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
#     # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
#     # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
#     # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。

#     # 创建连接,POOL数据库连接池中
#     conn = POOL.connection()
#     # 创建游标
#     cursor = conn.cursor()
#     # SQL语句
#     sql = "SELECT device_uuid FROM `july_device` where bind_account = %d ORDER BY last_login_time DESC"%(int(account_id))
#     cursor.execute(sql)
#     # 执行结果
#     deviceid = cursor.fetchall()[0][0]
#     # token = {}
#     # token["logintoken"] = result[0]
#     # token["device"] = result[1]
#     # token["hwdeviceid"] = result[2]
#     # 将conn释放,放回连接池
#     conn.close()
#     print(deviceid)
#     return deviceid

# def get_hwdeviceid(account_id):
#     # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
#     # 否则则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
#     # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
#     # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
#     # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。

#     # 创建连接,POOL数据库连接池中
#     conn = POOL.connection()
#     # 创建游标
#     cursor = conn.cursor()
#     # SQL语句
#     sql = "SELECT hwdeviceid FROM `july_device` where bind_account = %d ORDER BY last_login_time DESC"%(int(account_id))
#     cursor.execute(sql)
#     # 执行结果
#     hwdeviceid = cursor.fetchall()[0][0]
#     # token = {}
#     # token["logintoken"] = result[0]
#     # token["device"] = result[1]
#     # token["hwdeviceid"] = result[2]
#     # 将conn释放,放回连接池
#     conn.close()
#     print(hwdeviceid)
#     return hwdeviceid
    
# # 现在没有找到在用例里边通过一个函数接收三个返回值的办法，所以先这样拆开写，后期优化
# def get_token():
#     # print(result[0])
#     return result[0]

# def get_deviceid():
#     # print(result[1])
#     return result[1]

# def get_hwdeviceid():
#     # print(result[2])
#     return result[2]
   
# select_mysql(17307458)
# get_token()
# get_deviceid()
#数据库的单例模式学习使用
# class connmysql(object):
#     obj = None   #对象第一次为None
#     def __new__(cls, *args, **kwargs): #单例模式
#         if cls.obj is None:     #如果对象为None
#             cls.obj = super().__new__(cls)  # 就创建一个对象

#         return cls.obj  #否则直接返回
#     def __init__(self):
#         # 1. 链接数据库， 得到一个对象
#         try:
#             self.db=pymysql.connect(
#                 host='rr-bp1c02r68219ep2kio.mysql.rds.aliyuncs.com',
#                 port=3306,
#                 user='dsyread0510',
#                 passwd='PP_dhjh_234_q',
#                 db = "cloudgaming",
#                 charset='utf8'
#             )
#         except Ellipsis as e:
#             print(e)
#             os._exit(0)   # 如果第一步的链接失败，下面的所有代码都不用走，直接退出

#         self.cs=self.db.cursor()   #2.得到一个游标对象

#     def cha(self,account_id):
#         sql = "SELECT login_token FROM `july_device` where bind_account = %d ORDER BY last_login_time DESC"%(account_id)
#         """负责查询功能"""
#         #3 执行SQL语句
#         try:
#             self.cs.execute(sql)
#         except Exception as e:
#             print(e)
#             return
#         #4.获取查询结果
#         r=self.cs.fetchall()
#         return r[0][0]    #将结果返回
    # 这次只涉及查询数据库，这个不用
    # def update(self,sql):
    #     """负责更行功能"""
    #     # 3 利用游标对象执行SQL语句
    #     try:
    #         self.cs.execute(sql)
    #     except Exception as e:
    #         print(e)
    #         return
    #     #4.提交 如果不进行提交，所有的改变(insert, delete, update)不会生效
    #     self.db.commit()
    #     print("更新成功！")

#     def __del__(self):
#         self.cs.close()  # 5. 关闭链接
#         self.db.close()

# def token(account):
#     a=connmysql()
#     c=a.cha(account)
#     return c


# # 用例是同时执行的，在每个用例执行之前使用这个函数，等login调用函数更新完env文件之后，执行其他用例(这个好像是一开始就加进内存的回头还得在考虑一下)
# def WaitTime():
#     print("等待一秒")
#     time.sleep(1)

#测试修改返回值
# def ChangeResponse(ret):
#     ret = -1024
#     return ret





# def UpdataEnv():
#     try:
#         device,hwdevice,token = GetTockenFromMysql()
#     except Exception as mysqlErr:
#         print("数据库查询数据报错"+ str(mysqlErr))
#     try:
#         with open('.env','r+') as env_file:
#             lines = env_file.readlines()
#             count = 0
#             length = len(lines)
#             for line in lines:
#                 count += 1
#                 if count == length and line.split("=")[0] != "logintoken":
#                     env_file.write("\n"+"logintoken="+token)
#                 elif  "hwdeviceid" in line:             #hwdeviceid  deviceid判断顺序不能变
#                     if line.split("=")[1] != hwdevice:
#                         line = "hwdeviceid="+hwdevice+"\n"
#                         lines[count-1] = line

#                 elif  "deviceid" in line:
#                     if line.split("=")[1] != device:
#                         line = "deviceid="+device+"\n"
#                         lines[count-1] = line
#             with open('.env','w') as new_env_file:
#                 for new_line in lines:
#                     new_env_file.write(new_line)  
#     except Exception as e:
#         print("更新env文件报错" + str(e))
    
# # 验证login返回的status_code，ret两个数值，当status_code不等于200时，强行停止后边的执行
# # 如果返回的token与env中的不同或者不存在于env中调用UpdataEnv()更新token

# global content_token 
# content_token = ""

# def CheckResponseCode(content):
#     if content.status_code == 200:
#         global content_token
#         if content.body["ret"] == -1024:
#             Mysql_device,Mysql_hwdeviceid,Mysql_token= GetTockenFromMysql()
#             content_token = Mysql_token
#         content_token= content.body["user_info"]["device_info"]["login_token"]  
#     else:
#         sys.exit("HTTPS返回404，之后用例不执行")



# def GetTockenFromMysql():
#     connect = pymysql.Connect(
#         host='rr-bp1c02r68219ep2kio.mysql.rds.aliyuncs.com',
#         port=3306,
#         user='dsyread0510',
#         passwd='PP_dhjh_234_q',
#         db = "cloudgaming",
#         charset='utf8')
#     cursor = connect.cursor()
#     sql = "SELECT device_uuid,hwdeviceid,login_token FROM `july_device` where bind_account = 22993655 ORDER BY last_login_time DESC"
#     cursor.execute(sql)
#     TokenTuple = cursor.fetchall()[0]
#     connect.commit()
#     connect.close()
#     Mysql_device,Mysql_hwdeviceid,Mysql_token = TokenTuple[0],TokenTuple[1],TokenTuple[2]
#     #print(Mysql_device,Mysql_hwdeviceid,Mysql_token)
#     return Mysql_device,Mysql_hwdeviceid,Mysql_token





# if __name__ == "__main__":
#     a=connmysql()
#     account = 22993655
#     c=a.cha(account)
#     print(c)