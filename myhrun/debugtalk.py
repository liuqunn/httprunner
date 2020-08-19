import requests
import json

kw = {
        "a": "login",
        "password": "96e79218965eb72c92a549dd5a330112",
        "pid": "gloudphone",
        "type": "Android",                   
        "m": "User",
        "version": "420200722",
        "username": "22993655",
        "deviceid": "R_iH8HGpNRzpxXbv34lcpJcyT8jxuc1S",
        "hwdeviceid": "785cfff3-c74d-4a5f-b696-320c57fd3527"
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
        print("login接口错误")
if __name__ == "__main__":
    get_token()