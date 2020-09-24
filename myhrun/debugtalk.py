import requests
import json
import pymysql
import os


kw = {
        "a": "login",
        "password": "96e79218965eb72c92a549dd5a330112",
        "pid": "gloudphone",
        "type": "Android",                   
        "m": "User",
        "version": "420200722",
        "username": "22993655",
        "deviceid": "R_VWfhDcsKKGvRKLwNCG2DF0Jk7jKXuR",
        "hwdeviceid": "b9d1def2-88e8-4cc3-a632-fa2f460d5625"
                }
def get_token():
    response = requests.get("https://b2.51ias.com/api.php",params=kw)
    if json.loads(response.text)["ret"]==0:
        token= json.loads(response.text)["user_info"]["device_info"]["login_token"]
        print(token)
        with open('.env','r+') as env_file:
            lines = env_file.readlines()
            count = 0
            length = len(lines)
            for line in lines:
                count += 1
                if count == length and line.split("=")[0] != "logintoken":
                    env_file.write("\n"+"logintoken="+token)
                elif  "logintoken" in line:
                    if line.split("=")[1] != token:
                        line = "logintoken="+token+"\n"
                        lines[count-1] = line
                    break
            with open('.env','w') as new_env_file:
                for new_line in lines:
                    new_env_file.write(new_line)
    else:
        print("使用默认账号登录接口报错")

def WriteToEnv(content):
    if json.loads(content.text)["ret"]==0:
        token= json.loads(content.text)["user_info"]["device_info"]["login_token"]
        with open('.env','r+') as env_file:
            lines = env_file.readlines()
            count = 0
            length = len(lines)
            for line in lines:
                count += 1
                if count == length and line.split("=")[0] != "logintoken":
                    env_file.write("\n"+"logintoken="+token)
                elif  "logintoken" in line:
                    if line.split("=")[1] != token:
                        line = "logintoken="+token+"\n"
                        lines[count-1] = line
                    break
            with open('.env','w') as new_env_file:
                for new_line in lines:
                    new_env_file.write(new_line)
    else:
        print("login登录信息错误，使用默认账号登录更新tocken")
        get_token()

def connect_mysql():
    connect = pymysql.Connect(
        host='rr-bp1c02r68219ep2kio.mysql.rds.aliyuncs.com',
        port=3306,
        user='dsyread0510',
        passwd='PP_dhjh_234_q',
        db = "cloudgaming",
        charset='utf8'
)
    cursor = connect.cursor()
    sql = "SELECT login_token FROM july_device where bind_account =  17307458"
    cursor.execute(sql)
    tocken1 = cursor.fetchall()[0][0]
    connect.commit()
    connect.close()
# if __name__ == "__main__":
#     get_token()