from autoboot import AutoBoot, AutoBootConfig, ApplicationProperties
from autoboot_web import WebRunner

# uvicorn tests.test_runner.test_runner_example:app --host 127.0.0.1 --port 8001 --env-file ./tests/test_runner/.env
autoboot = AutoBoot(config=AutoBootConfig(config_dir="./tests/test_runner"))
autoboot.apply(WebRunner())
app = autoboot.run(lambda: WebRunner.get_context())
autoboot.logger.info(ApplicationProperties.app_name())