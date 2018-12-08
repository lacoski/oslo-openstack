from oslo_config import cfg

import oslo.messaging as om

from oslo_messaging.transport import TransportURL

rabbit://openstack:Welcome123@10.10.10.175


cfg.CONF.set_override('rabbit_host', '10.10.10.175')
cfg.CONF.set_override('rabbit_port', 5672)
cfg.CONF.set_override('rabbit_userid', 'openstack')
cfg.CONF.set_override('rabbit_password', 'Welcome123')
cfg.CONF.set_override('rabbit_login_method', 'AMQPLAIN')
cfg.CONF.set_override('rabbit_virtual_host', '/')
cfg.CONF.set_override('rpc_backend', 'rabbit')

res = [{k:v} for k, v in cfg.CONF.iteritems()]
pprint(res)


http://fosshelp.blogspot.com/2015/02/openstack-oslo-messaging-rpc-api.html