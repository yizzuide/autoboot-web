from autoboot_web.mvc.annotation import Controller
from autoboot_web.mvc.annotation.controller import Get
from fastapi import Request

@Controller(path="/")
class IndexController:
  
  @Get("/index")
  def index(self, name, request: Request):
    print(request.headers)
    print(request.query_params)
    return f"Hello: {name}"