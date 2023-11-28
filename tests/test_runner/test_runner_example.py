from autoboot import AutoBoot, AutoBootConfig
from autoboot_web import WebRunner

# uvicorn tests.test_runner.test_runner_example:app --host 127.0.0.1 --port 8001
autoboot = AutoBoot(config=AutoBootConfig(config_dir="./tests/test_runner"))
autoboot.apply(WebRunner(scan_controllers="tests.test_runner.controller"))
autoboot.run()

app = WebRunner.get_context()