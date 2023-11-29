from autoboot import AutoBoot, AutoBootConfig, ApplicationProperties
from autoboot_web import WebRunner

from autoboot_web.http_properties import HttpProperties

# uvicorn tests.test_runner.test_runner_example:app --host 127.0.0.1 --port 8001 --env-file ./tests/test_runner/.env
autoboot = AutoBoot(config=AutoBootConfig(config_dir="./tests/test_runner"))
autoboot.apply(WebRunner())
app = autoboot.run(lambda: WebRunner.get_context())

AutoBoot.logger.warning("app name: {}", ApplicationProperties.app_name())
AutoBoot.logger.warning("session max age: {}", HttpProperties.session_max_age())

