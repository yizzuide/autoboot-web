from typing import Optional
from importlib import import_module
from autoboot import AutoBoot
from autoboot.plugin import AppPlugin, Runner
from .web_properties import WebProperties
from fastapi import FastAPI

class WebRunner(AppPlugin):
  
  __ctx__ = "FastAPI"
  
  def __init__(self, scan_controllers: Optional[str | list[str]] = None) -> None:
    self._scan_controllers = scan_controllers
  
  @staticmethod
  def get_context() -> FastAPI:
    return AutoBoot.get_context(WebRunner.__ctx__)
  
  def install(self) -> Runner:
    app = FastAPI()
    return (WebRunner.__ctx__, app)
  
  def env_prepared(self) -> None:
    if self._scan_controllers:
      if isinstance(self._scan_controllers, str):
        #__import__(self._scan_controllers)
        import_module(name=self._scan_controllers)
      else:
        for controller in self._scan_controllers:
          import_module(name=controller)
    
    if WebProperties.scanControllerPackages():     
      for package in WebProperties.scanControllerPackages():
        import_module(name=package)
  
  def app_started(self) -> None:
    return super().app_started()
  