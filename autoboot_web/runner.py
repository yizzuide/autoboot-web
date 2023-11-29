from typing import Optional
from importlib import import_module
from autoboot import AutoBoot
from autoboot.plugin import AppPlugin, Runner
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.sessions import SessionMiddleware
from .http_properties import HttpProperties
from .web_properties import WebProperties

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
    packages: list[str] = []
    if self._scan_controllers:
      packages.extend([self._scan_controllers] if isinstance(self._scan_controllers, str) else self._scan_controllers)
    
    if WebProperties.scan_controller_packages():
      packages.extend(WebProperties.scan_controller_packages()) 
    
    for package in packages:
      #__import__(packages)
      import_module(package)
    
    app = self.get_context()
    
    if HttpProperties.gzip_enable():
      AutoBoot.logger.info("GZIP is enabled.")
      app.add_middleware(GZipMiddleware, minimum_size=HttpProperties.gzip_minimum_size())
      
    if HttpProperties.session_enable():
      AutoBoot.logger.info("Session is enabled.")
      app.add_middleware(
        SessionMiddleware, 
        secret_key=HttpProperties.session_secret_key(),
        session_cookie=HttpProperties.session_cookie_name(),
        max_age=HttpProperties.session_max_age(),
        same_site=HttpProperties.session_same_site(),
        https_only=HttpProperties.session_https_only()
      )
    
    if WebProperties.cross_origin():
      AutoBoot.logger.info("Cross-Origin Resource Sharing (CORS) is enabled.")
      from fastapi.middleware.cors import CORSMiddleware
      app.add_middleware(
        CORSMiddleware,
        allow_origins=WebProperties.allow_origins(),
        allow_credentials=WebProperties.allow_credentials(),
        allow_methods=WebProperties.allow_methods(),
        allow_headers=WebProperties.allow_headers(),
        max_age=WebProperties.max_age()
      )
      
    if WebProperties.csrf_enabled():
      AutoBoot.logger.info("CSRF is enabled.")
      try:
        from autoboot_web.middleware import UniformCSRFMiddleware
      except ImportError:
        raise ImportError("CSRF middleware is not installed.")
    
      app.add_middleware(
        UniformCSRFMiddleware, 
        secret=WebProperties.csrf_secret(), 
        cookie_name=WebProperties.csrf_cookie_name(),
        cookie_domain=WebProperties.csrf_cookie_domain(),
        header_name=WebProperties.csrf_header_name()
      )
    
    return super().env_prepared()
  
  def app_started(self) -> None:
    return super().app_started()
  