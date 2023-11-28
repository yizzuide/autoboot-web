
from autoboot.annotation import value_component

class WebProperties:
  
  @value_component("autoboot.web.scan_controller_packages")
  @staticmethod
  def scanControllerPackages() -> list[str]:
    pass