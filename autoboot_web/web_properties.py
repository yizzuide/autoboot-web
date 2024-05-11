
import uuid
from autoboot.annotation import static_property

class WebProperties:
  
  @static_property("autoboot.web.scan_controller_packages")
  def scan_controller_packages() -> list[str]:
    pass
  
  @static_property("autoboot.web.security.cors.cross_origin")
  def cross_origin() -> bool:
    return False

  @static_property("autoboot.web.security.cors.allow_origins")
  def allow_origins() -> list[str]:
    return ["*"]

  @static_property("autoboot.web.security.cors.allow_methods")
  def allow_methods() -> list[str]:
    return ["*"]

  @static_property("autoboot.web.security.cors.allow_headers")
  def allow_headers() -> list[str]:
    return ["*"]

  @static_property("autoboot.web.security.cors.allow_credentials")
  def allow_credentials() -> bool:
    return True
  
  @static_property("autoboot.web.security.cors.max_age")
  def max_age() -> int:
    return 3600

  @static_property("autoboot.web.security.csrf.enable")
  def csrf_enable() -> bool:
    return False
  
  @static_property("autoboot.web.security.csrf.secret")
  def csrf_secret() -> str:
    return str(uuid.uuid1())

  @static_property("autoboot.web.security.csrf.cookie_name")
  def csrf_cookie_name() -> str:
    return "CSRF_Token"
  
  @static_property("autoboot.web.security.csrf.csrf_cookie_domain")
  def csrf_cookie_domain() -> str:
    return None

  @static_property("autoboot.web.security.csrf.header_name")
  def csrf_header_name() -> str:
    return "X-CSRF-Token"