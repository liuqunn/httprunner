from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseshttprunner(HttpRunner):

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
                    "password": "${ENV(password)}",
                    "pid": "${ENV(pid)}",
                    "type": "${ENV(type)}",
                    "version": "${ENV(version)}",
                    "username": "${ENV(username)}",
                    "deviceid": "${ENV(deviceid)}",
                    "language": "${ENV(language)}",
                    "lz": "${ENV(lz)}",
                    "hwdeviceid": "${ENV(hwdeviceid)}",
                    "m": "User",
                    "a": "login",
                }
            )
            .teardown_hook("${CheckResponseCode($response)}")
            .extract()
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.ret", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseGameInfo().test_start()

