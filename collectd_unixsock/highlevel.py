import socket
import time
from . import CollectDClient

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


class Connector():
    def __init__(
            self,
            socket_path,
            hostname=socket.gethostname(),
            ):
        self.collectd_client = CollectDClient(socket_path)

    def create_plugin(self, *args, **kwargs):
        return Plugin(self, *args, **kwargs)


class Plugin():
    def __init__(
            self,
            connector,
            plugin_name=None,
            plugin_instance=None
            ):
        self._connector = connector
        self._plugin_name = plugin_name
        self._plugin_instance = plugin_instance

    @property
    def identifier(self):
        buf = StringIO()
        if self.host:
            buf.write(self.host)
        if self.plugin_name:
            buf.write("/")
            buf.write(self.plugin_name)
        if self.plugin_instance_name:
            buf.write("/")
            buf.write(self.plugin_instance_name)
        if self.type:
            buf.write("/")
            buf.write(self.type)
        if self.typeinstance:
            buf.write("/")
            buf.write(self.type_instance)
        return buf.getvalue()

    def create_gauge(self, value_name):
        return Widget(self, )


class Widget():
    def __init__(
            self,
            plugin,
            value_name,
            type_name='gauge',
            ):
        self._plugin = plugin
        self._type = type_name
        self._value_name = value_name

    @property
    def identifier(self):
        return '/'.join([
            self._plugin.identifier,
            self._value_name,
            self._type])

    def put_val(self, value):
        timestamp = time.time()
        self._plugin._connector.put_val(self.identifier, [value], timestamp)
