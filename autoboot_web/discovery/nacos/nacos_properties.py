
from autoboot.annotation import static_property


class NacosProperties(object):
    
  @static_property("autoboot.web.discovery.nacos.enable")
  def enable():
    return False

  @static_property("autoboot.web.discovery.nacos.server_address")
  def server_address():
    return "127.0.0.1:8848"
  
  @static_property("autoboot.web.discovery.nacos.namespace")
  def namespace() -> str:
    pass
  
  @static_property("autoboot.web.discovery.nacos.username")
  def username() -> str:
    pass
  
  @static_property("autoboot.web.discovery.nacos.password")
  def password() -> str:
    pass
  
  @static_property("autoboot.web.discovery.nacos.ak")
  def ak() -> str:
    pass
  
  @static_property("autoboot.web.discovery.nacos.sk")
  def sk() -> str:
    pass

  @static_property("autoboot.web.discovery.nacos.service_name")
  def service_name():
    return "test-service"
  
  @static_property("autoboot.web.discovery.nacos.service_ip")
  def service_ip():
    return "127.0.0.1"
  
  @static_property("autoboot.web.discovery.nacos.service_port")
  def service_port():
    return 8080
  
  @static_property("autoboot.web.discovery.nacos.group_name")
  def group_name():
    from nacos import client
    
    return client.DEFAULT_GROUP_NAME
  
  @static_property("autoboot.web.discovery.nacos.heartbeat_interval")
  def heartbeat_interval():
    return 2