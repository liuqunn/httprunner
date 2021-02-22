import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters

class TestCasesLogin(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-password": "${parameterize(testcases/username.csv)}"
            }
        )
    )
    def test_start(self, param):
        super().test_start(param)
    config = (
        Config("login")
        .export(*["token"])
        .base_url("")
        )
        
    teststeps = [
        Step(
            RunRequest("login")
            .get("${ENV(url)}")
            .with_params(
                **{
                    "password": "$password",
                    "pid": "${ENV(pid)}",
                    "type": "${ENV(type)}",
                    "version": "${ENV(version)}",
                    "username": "$username",
                    "deviceid": "${ENV(deviceid)}",
                    "language": "${ENV(language)}",
                    "lz": "${ENV(lz)}",
                    "hwdeviceid": "${ENV(hwdeviceid)}",
                    "m": "User",
                    "a": "login",
                }
            )
            .extract()
            .with_jmespath("body.user_info.device_info.login_token","token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.ret", 0)
            .assert_not_equal("body.user_info.device_info.login_token","")
        ),
    ]


if __name__ == "__main__":
    TestCaseGameInfo().test_start()

