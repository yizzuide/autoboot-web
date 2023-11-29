
import uuid
from autoboot.annotation import value_component

class HttpProperties:
  
  @value_component("autoboot.web.http.gzip.enable")
  @staticmethod
  def gzip_enable() -> bool:
    return False

  @value_component("autoboot.web.http.gzip.minimum_size")
  @staticmethod
  def minimum_size() -> int:
    return 1000

  @value_component("autoboot.web.http.session.enable")
  @staticmethod
  def session_enable() -> bool:
    return False
  
  @value_component("autoboot.web.http.session.secret")
  @staticmethod
  def session_secret_key() -> str:
    return str(uuid.uuid1())

  @value_component("autoboot.web.http.session.cookie_name")
  @staticmethod
  def session_cookie_name() -> str:
    return "session_id"
  
  @value_component("autoboot.web.http.session.max_age")
  @staticmethod
  def session_max_age() -> int:
    return 3600

  @value_component("autoboot.web.http.session.same_site")
  @staticmethod
  def session_same_site() -> str:
    return "lax"
  
  @value_component("autoboot.web.http.session.https_only")
  @staticmethod
  def session_https_only() -> bool:
    return False
  
  
  