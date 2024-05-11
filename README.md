# autoboot web starter
基于 [autoboot](https://github.com/yizzuide/autoboot) 框架的插件机制扩展，集成了`FastAPI`框架，专注于web开发方向。
<p>
  <a href="https://pypi.org/project/autoboot-web">
      <img src="https://img.shields.io/pypi/v/autoboot-web?color=%2334D058&label=pypi%20package" alt="Version">
  </a>
  <a href="https://pypi.org/project/autoboot-web">
        <img src="https://img.shields.io/pypi/pyversions/autoboot-web.svg?color=%2334D058" alt="Python">
  </a>
  <a href="https://pepy.tech/project/autoboot-web">
      <img src="https://static.pepy.tech/personalized-badge/autoboot-web?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Downloads">
  </a>
  <a href="https://github.com/yizzuide/autoboot-web/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/yizzuide/autoboot-web" alt="License">
  </a>
</p>

## Quick Start

### Install
```sh
pip install autoboot-web
```

### Usage
#### 配置

* 启动配置文件`.env`
```ini
# 环境名称（默认值：dev，框架根据这个配置项来加载当前的环境配置）
ENV_NAME=dev

APPLICATION_NAME=web-runner
```

* 环境配置文件`.env.dev`
```ini
APPLICATION_NAME=web-runner-dev
```

* 主配置文件`autoboot.yaml`
```yaml
autoboot:
  application:
    name: !env $APPLICATION_NAME
    module: api

  web:
    http:
      gzip:
        enable: true
        # 小于1KB不压缩
        minimum_size: 1KB
      session:
        enable: true
        cookie_name: "session_id"
        max_age: 120m
    security:
      cors:
        cross_origin: true

    # 扫描控制器包
    scan_controller_packages:
      - controller
```

#### 创建目录`controller`

* 在该目录下创建`__init__.py`
```py
from .controller import IndexController

__all__=["IndexController"]
```

* 在该目录创建`index.py`
```py
from autoboot_web.mvc.annotation import Controller, Get


@Controller(path="/", tag="index")
class IndexController:
  
  @Get("/")
  def index(self, name):
    return f"Hello: {name}"
```

#### 创建并启动容器
* 创建`main.py`
```py
from autoboot import AutoBoot, AutoBootConfig
from autoboot_web import WebRunner

context = Autoboot(AutoBootConfig(config_dir="."))
# 注册插件
context.apply(WebRunner())
# 暴露插件的Runner到全局变量（FastAPI使用的unicorn启动时会用到）
app = context.run(lambda: WebRunner.get_context())

# 其它使用 FastAPI 实例 app 的代码
# ...
```

#### 启动服务器
```bash
uvicorn example.main:app --host 127.0.0.1 --port 8000 --env-file .env
```

## Contributors
有问题可以在issues开话题讨论，如果你有新的想法，创建新的`feat`或`pref`分支并提交PR。

## License
[MIT License](https://github.com/yizzuide/autoboot/blob/main/LICENSE.txt)

