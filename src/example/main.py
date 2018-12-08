from oslo_config import cfg

import oslo.messaging as om

from oslo_messaging.transport import TransportURL


rabbit://openstack:Welcome123@10.10.10.175//nova


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


transport = messaging.get_rpc_transport(cfg.CONF)
target = messaging.Target(topic='test', version='2.0')
client = messaging.RPCClient(transport, target)
client.call(ctxt, 'test', arg=arg)

conf=cfg.CONF


transport = oslo_messaging.get_rpc_transport(self.conf, url='fake:')
client = oslo_messaging.RPCClient(transport, target)

url, results, hide_password


from oslo_config import cfg
from oslo_messaging import TransportURL
import oslo_messaging

import oslo_messaging.transport
oslo_messaging.transport.TransportURL(cfg.CONF, '10.10.10.175')
trl = oslo_messaging.transport.TransportURL(cfg.CONF, '10.10.10.175')
trl = oslo_messaging.transport.TransportURL(cfg.CONF, transport='rabbit://openstack:Welcome123@10.10.10.175//nova')

class TestClient(object):

    def __init__(self, transport):
        target = messaging.Target(topic='test', version='2.0')
        self._client = messaging.RPCClient(transport, target)

    def test(self, ctxt, arg):
        return self._client.call(ctxt, 'test', arg=arg)


https://docs.openstack.org/oslo.messaging/latest/reference/target.html#target-versions