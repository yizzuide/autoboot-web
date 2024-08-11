
from autoboot_web.mvc.annotation import Controller, Get


@Controller(path="/user")
class UserController:
  
  @Get("/find/{id}")
  async def findUser(self, id):
    return f"User: {id}"

