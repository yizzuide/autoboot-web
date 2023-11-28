from autoboot_web.mvc.annotation import Controller
from autoboot_web.mvc.annotation.controller import Get

@Controller(path="/user")
class UserController:
  
  @Get("/find/{id}")
  def findUser(self, id):
    return f"User: {id}"

