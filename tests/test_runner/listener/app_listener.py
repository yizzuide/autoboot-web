
from autoboot import AutoBoot
from autoboot.event import ApplicationListener
from autoboot.meta import Listener
from autoboot_web.discovery.nacos import nacos_client

@Listener
class AppListener(ApplicationListener):
  
  def on_started(self):
    nacos = nacos_client()
    if nacos:
      service_list = nacos.list_naming_instance(service_name="test-service", group_name="test-group")
      AutoBoot.logger.warning(f"nacos service list: {service_list}")