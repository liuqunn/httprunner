# 获取我的视频接口，未加入精选的视频，如果存在就加入精选，没有就跳过加入精选接口
#step中需要使用username（account_id）使用$username

import pytest
import os
import sys
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters
from testcases.public_api.login_test import TestCasesLogin   #引入login类，才能使用login接口

sys.path.insert(0, os.getcwd())  #将当前路径加入到框架的目录中且优先查找


class TestCaseGetMyVideo(HttpRunner):  #更改为与接口相关的名字，方便以后引用（例如引用login接口需要先导入类名）                           ******需要修改TestCase+接口名
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-password": "${parameterize(testcases/username.csv)}"   #取excel表格中的数据做数据驱动                       如果修改了excel文档，这里需要修改
            }
        )
    )
    def test_start(self, param):
        super().test_start(param)
    config = (
        Config("get_my_video")                                                                                                        #需要修改 接口名
        .variables(
        **{
            "tip_text":"get_my_video接口成功,没有未加入精选视频，account_convert_video接口跳过" ,   #定义跳过之后的说明                   #跳过的step的说明
            "username": "$username",     #在此文件中引用其他测试用例，需要定义其他用例中引用的参数                                          
            "password": "$password"
        }
    )
        )
    
    teststeps = [
        Step(
            RunTestCase("login function")                                                                                               #需要修改 接口名
            .call(TestCasesLogin)          #调用login接口
            .export(*["token","username"])
        ),
        Step(
            RunRequest("get_my_video")                                                                                                  #需要修改 接口名   
            .with_variables(
                **{   
                }
                )
            .get("${ENV(url)}")
            .with_params(
                **{
                    "deviceid": "${ENV(deviceid)}",
                    "ver": "${ENV(ver)}",
                    "pid": "${ENV(pid)}",
                    "logintoken": "$token",        
                    "account_id": "$username",
                    "mode": "${ENV(mode)}",
                    "language": "${ENV(language)}",
                    "lz": "${ENV(lz)}",
                    "hwdeviceid": "${ENV(hwdeviceid)}",
                    "TimeZoneName": "${ENV(TimeZoneName)}",
                    "TimeZoneId": "${ENV(TimeZoneId)}",
                    "version": "${ENV(version)}",
                    "m": "CUser",                                                                                                       #修改m参数
                    "a": "get_my_video",                                                                                                #a参数
                    "Sint": "27",                                                                                                       #以下都是需要修改的接口的特定参数
                    "account_id": "$username"
                }
            ) 
            .extract()
            .with_jmespath("body.video_list.my_video","MyVideo")   #提取响应的返回值
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.ret", "${judgment_ret($response)}")  #统一用judgment_ret判断ret
        ),

       Step(
            RunRequest("account_convert_video")
            .setup_hook("${var_skipif($MyVideo,$tip_text)}")   #统一用var_skipif这个函数做skipif跳转
            .with_variables(
                **{
                    "video_id":"${get_videoid($MyVideo)}"    
                }
                )
            .get("${ENV(url)}")
            .with_params(
                **{
                   "deviceid": "${ENV(deviceid)}",
                    "ver": "${ENV(ver)}",
                    "pid": "${ENV(pid)}",
                    "logintoken": "$token",        
                    "account_id": "$username",
                    "mode": "${ENV(mode)}",
                    "language": "${ENV(language)}",
                    "lz": "${ENV(lz)}",
                    "hwdeviceid": "${ENV(hwdeviceid)}",
                    "TimeZoneName": "${ENV(TimeZoneName)}",
                    "TimeZoneId": "${ENV(TimeZoneId)}",
                    "version": "${ENV(version)}",
                    "m": "video",
                    "a": "account_convert_video",
                    "Sint": "29",
                    "brand": "${ENV(brand)}",
                    "video_id": "$video_id",
                    "video_name": "aaa",
                    "account_id": "$username"
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.ret", "${judgment_ret($response)}")
        )
    ]


if __name__ == "__main__":
    TestCaseGetMyVideo().test_start("")
