import pytest
import os
import sys
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters

sys.path.insert(0, os.getcwd())  #将当前路径加入到框架的目录中且优先查找
from testcases.public_api.login_test import TestCasesLogin   #引入login类，才能使用login接口



class TestCaseClientRegionList(HttpRunner):  #更改为与接口相关的名字，方便以后引用（例如引用login接口需要先导入类名）
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
        Config("region_list")
        .variables(
        **{
            "username": "$username",     #在此文件中引用其他测试用例，需要定义本次用例中引用的参数
            "password": "$password"
        }
    )
        )
    
    teststeps = [
        Step(
            RunTestCase("login function")
            .call(TestCasesLogin)          #调用login接口
            .export(*["token"])
        ),
        Step(
            RunRequest("region_list")
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
                    "brand": "${ENV(brand)}",
                    "Sint": "29",
                    "m": "Client",
                    "a": "region_list"
                }
            ) 
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("${judgment_ret($response)}",0)
        )
    ]

if __name__ == "__main__":
    TestCaseClientRegionList().test_start()