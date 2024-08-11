
import asyncio

from autoboot_web.mvc.annotation import Controller, Get
from fastapi import Request


@Controller(path="/")
class IndexController:
  
  @Get("/index")
  async def index(self, name, request: Request):
    print(request.headers)
    print(request.query_params)
    #await asyncio.sleep(1)
    return f"Hello: {name}"