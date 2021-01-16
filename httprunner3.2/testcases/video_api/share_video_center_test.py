# 视频中心type=new下的所有视频

import pytest
import os
import sys
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters

sys.path.insert(0, os.getcwd())  #将当前路径加入到框架的目录中且优先查找
from testcases.public_api.login_test import TestCasesLogin   #引入login类，才能使用login接口



class TestCaseShareVideoCenter(HttpRunner):  #更改为与接口相关的名字，方便以后引用（例如引用login接口需要先导入类名）
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-password": "${parameterize(testcases/username.csv)}"   #取excel表格中的数据做数据驱动
            }
        )
    )
    def test_start(self, param):
        super().test_start(param)
    config = (
        Config("share_video_center")
        .variables(
        **{
            "username": "$username",     #在此文件中引用其他测试用例，需要定义其他用例中引用的参数
            "password": "$password"
        }
    )
        )
    
    teststeps = [
        Step(
            RunTestCase("login function")
            .call(TestCasesLogin)          #调用login接口
            .export(*["token","username"])
        ),
        Step(
            RunRequest("share_video_center")
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
                    "m": "video",
                    "a": "share_video_center",
                    "Sint": "27",
                    "page": "1",
                    "rows": "10",
                    "type": "new"
                }
            ) 
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.ret", "${judgment_ret($response)}")
        )
    ]

if __name__ == "__main__":
    TestCaseShareVideoCenter().test_start("")