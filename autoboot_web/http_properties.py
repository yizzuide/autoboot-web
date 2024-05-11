
import uuid
from autoboot.annotation import static_property

class HttpProperties:
  
  @static_property("autoboot.web.http.gzip.enable")
  def gzip_enable() -> bool:
    return False

  @static_property("autoboot.web.http.gzip.minimum_size")
  def gzip_minimum_size() -> int:
    return 1000

  @static_property("autoboot.web.http.session.enable")
  def session_enable() -> bool:
    return False
  
  @static_property("autoboot.web.http.session.secret")
  def session_secret_key() -> str:
    return str(uuid.uuid1())

  @static_property("autoboot.web.http.session.cookie_name")
  def session_cookie_name() -> str:
    return "session_id"
  
  @static_property("autoboot.web.http.session.max_age")
  def session_max_age() -> int:
    return 3600

  @static_property("autoboot.web.http.session.same_site")
  def session_same_site() -> str:
    return "lax"
  
  @static_property("autoboot.web.http.session.https_only")
  def session_https_only() -> bool:
    return False
  
  
  