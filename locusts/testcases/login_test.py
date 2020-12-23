import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters

class TestCaseshttprunner(HttpRunner):
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
        .base_url("https://b2.51ias.com")
        )
        
    teststeps = [
        Step(
            RunRequest("login")
            .get("/api.php")
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
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.ret", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseGameInfo().test_start()

