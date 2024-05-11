import asyncio
from typing import Optional
from importlib import import_module
from autoboot import AutoBoot
from autoboot.plugin import AppPlugin
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.sessions import SessionMiddleware
from .http_properties import HttpProperties
from .web_properties import WebProperties

class WebRunner(AppPlugin[FastAPI]):
  
  _loop: asyncio.AbstractEventLoop
  
  # custom context name, default is class name
  #context_name = "WebRunner"
  
  def __init__(self, scan_controllers: Optional[str | list[str]] = None) -> None:
    self._scan_controllers = scan_controllers
    
  def __repr__(self) -> str:
    return f"WebRunner(scan_controllers={self.scan_controllers}"
    
  def get_event_loop(cls) -> asyncio.AbstractEventLoop:
    return cls._loop
  
  def install(self) -> FastAPI:
    app = FastAPI()
    
    @app.on_event("startup")
    def startup_event() -> None:
      WebRunner._loop = asyncio.get_running_loop()
      AutoBoot.logger.info("hold event loop: {}.", WebRunner._loop)
      
    return app
  
  def env_prepared(self) -> None:
    self.packages: list[str] = []
    if self._scan_controllers:
      self.packages.extend([self._scan_controllers] if isinstance(self._scan_controllers, str) else self._scan_controllers)
    
    if WebProperties.scan_controller_packages():
      self.packages.extend(WebProperties.scan_controller_packages()) 
      
  
  def app_started(self) -> None:
    for package in self.packages:
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
      
    if WebProperties.csrf_enable():
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