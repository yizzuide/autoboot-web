
import uuid
from autoboot.annotation import value_component

class WebProperties:
  
  @value_component("autoboot.web.scan_controller_packages")
  @staticmethod
  def scan_controller_packages() -> list[str]:
    pass
  
  @value_component("autoboot.web.security.cors.cross_origin")
  @staticmethod
  def cross_origin() -> bool:
    return False

  @value_component("autoboot.web.security.cors.allow_origins")
  @staticmethod
  def allow_origins() -> list[str]:
    return ["*"]

  @value_component("autoboot.web.security.cors.allow_methods")
  @staticmethod
  def allow_methods() -> list[str]:
    return ["*"]

  @value_component("autoboot.web.security.cors.allow_headers")
  @staticmethod
  def allow_headers() -> list[str]:
    return ["*"]

  @value_component("autoboot.web.security.cors.allow_credentials")
  @staticmethod
  def allow_credentials() -> bool:
    return True
  
  @value_component("autoboot.web.security.cors.max_age")
  @staticmethod
  def max_age() -> int:
    return 3600

  @value_component("autoboot.web.security.csrf.enabled")
  @staticmethod
  def csrf_enabled() -> bool:
    return False
  
  @value_component("autoboot.web.security.csrf.secret")
  @staticmethod
  def csrf_secret() -> str:
    return str(uuid.uuid1())

  @value_component("autoboot.web.security.csrf.cookie_name")
  @staticmethod
  def csrf_cookie_name() -> str:
    return "csrf_token"
  
  @value_component("autoboot.web.security.csrf.csrf_cookie_domain")
  @staticmethod
  def csrf_cookie_domain() -> str:
    return None

  @value_component("autoboot.web.security.csrf.header_name")
  @staticmethod
  def csrf_header_name() -> str:
    return "X-CSRF-TOKEN"