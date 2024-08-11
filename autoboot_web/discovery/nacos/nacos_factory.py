
from autoboot import AutoBoot
from autoboot.annotation import component, conditional

from .nacos_properties import NacosProperties

@conditional(value="autoboot.web.discovery.nacos.enable", having_value=True)
@component()
def nacos_client():
  from nacos import NacosClient
  
  client = NacosClient(
    server_addresses=NacosProperties.server_address(),
    namespace=NacosProperties.namespace(),
    username=NacosProperties.username(),
    password=NacosProperties.password(),
    ak=NacosProperties.ak(),
    sk=NacosProperties.sk()
  )
  success = client.add_naming_instance(
    service_name=NacosProperties.service_name(),
    ip=NacosProperties.service_ip(),
    port=NacosProperties.service_port(),
    group_name=NacosProperties.group_name(),
    heartbeat_interval=NacosProperties.heartbeat_interval()
  )
  if success:
    AutoBoot.logger.info(f"nacos register service[{NacosProperties.service_name()}] on {NacosProperties.service_ip()}:{NacosProperties.service_port()}")
  else:
    AutoBoot.logger.error(f"nacos register service[{NacosProperties.service_name()}] fail.")
  return client