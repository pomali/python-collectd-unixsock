from . import CollectDClient

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO



class Plugin():
    def __init__(
            self, 
            socket_path, 
            hostname=None,
            plugin_name=None,
            plugin_instance=None
            ):
        self.collectd_client = CollectDClient(socket_path)

    
    @property
    def source(self):
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
