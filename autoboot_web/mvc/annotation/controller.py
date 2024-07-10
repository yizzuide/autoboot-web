from typing import Type, Optional
from fastapi.routing import APIRouter
from autoboot_web import WebRunner
from autoboot_web.mvc import ClassBasedView


def Controller(path: Optional[str] = None, tag: Optional[str] = None):
  """
  Controller decorator

  :param path: path to the controller
  :param tag: tag for the api doc
  """
  
  if path:
    if not path.startswith("/"):
      path = "/" + path
  
  def wrapper(cls) -> Type[ClassBasedView]:
    router = APIRouter(tags=[tag] if tag else None)
    
    items = cls.__dict__.items()
    for name, method in items:
      if not callable(method) or not hasattr(method, "req_method"):
        continue
      
      if not method.__path__:
        raise Exception("Must set path on request mapping")
      else:
        if path:
          if path.endswith("/") and method.__path__.startswith("/"):
            method.__path__ = path + method.__path__[1:]
          elif not path.endswith("/") and not method.__path__.startswith("/"):
            method.__path__ = path + "/" + method.__path__
          else:
            method.__path__ = path + method.__path__

        if not method.__path__.startswith("/"):
          method.__path__ = "/" + method.__path__
          
        if method.req_method == "GET":
          router.add_api_route(
              path=method.__path__,
              endpoint=method,
              methods=["GET"],
              **method.__kwargs__
          )
        elif method.req_method == "POST":
          router.add_api_route(
              path=method.__path__,
              endpoint=method,
              methods=["POST"],
              **method.__kwargs__
          )
        elif method.req_method == "PUT":
          router.add_api_route(
              path=method.__path__,
              endpoint=method,
              methods=["PUT"],
              **method.__kwargs__
          )
        elif method.req_method == "DELETE":
          router.add_api_route(
              path=method.__path__,
              endpoint=method,
              methods=["DELETE"],
              **method.__kwargs__
          )
        elif method.req_method == "PATCH":
          router.add_api_route(
              path=method.__path__,
              endpoint=method,
              methods=["PATCH"],
              **method.__kwargs__
          )
        else:
          raise Exception("Unknown request method")
        
    # Add get_router method to the class
    cls.get_router = classmethod(lambda: router)
    
    # rectify routes which bind on method
    classBasedView = ClassBasedView(router=router, cls=cls)
    
    # register router
    WebRunner.get_context().include_router(router)
    
    return classBasedView
  return wrapper


def Get(path: str, **kwargs):
  def decorator(fn):
    fn.req_method = "GET"
    fn.__path__ = path
    fn.__kwargs__ = kwargs
    return fn
  return decorator

def Post(path: str, **kwargs):
  def decorator(func):
      func.req_method = "POST"
      func.__path__ = path
      func.__kwargs__ = kwargs
      return func
  return decorator

def Delete(path: str, **kwargs):
  def decorator(func):
      func.req_method = "DELETE"
      func.__path__ = path
      func.__kwargs__ = kwargs
      return func
  return decorator

def Put(path: str, **kwargs):
  def decorator(func):
      func.req_method = "PUT"
      func.__path__ = path
      func.__kwargs__ = kwargs
      return func
  return decorator

def Patch(path: str, **kwargs):
  def decorator(func):
      func.req_method = "PATCH"
      func.__path__ = path
      func.__kwargs__ = kwargs
      return func
  return decorator