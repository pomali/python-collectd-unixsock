# Python Collectd client using unix sockets


## Usage 

Enable plugin UnixSock in `collectd.conf`

```
# See collectd.conf(5)
  LoadPlugin unixsock
  # ...
  <Plugin unixsock>
    SocketFile "/var/run/collectd-unixsock"
    SocketGroup "collectd"
    SocketPerms "0770"
    DeleteSocket false
  </Plugin>
```

### Using low level `CollectDClient`
```python
from collectd_unixsock import CollectDClient

MY_HOSTNAME = "my_hostname"
PLUGIN_NAME = "my_plugin_name"

c = CollectDClient()
print(c.list_val())
print(
  c.put_val(
    '/'.join([MY_HOSTNAME, PLUGIN_NAME, "temperature"]),
    36.6))

```


### Using high level `Plugin`
```python
from collectd_unixsock import Plugin
conn = Plugin(
  "/var/run/collectd-unixsock",
  hostname = MY_HOSTNAME, 
  plugin_inst=PLUGIN_NAME)
  )
gauge = conn.Gauge("gague_name")
gauge.

```






## References

- https://collectd.org/wiki/index.php/Plugin:UnixSock
- https://collectd.org/documentation/manpages/collectd-unixsock.5.shtml
- <https://collectd.org/wiki/index.php/Plain_text_protocol>
- https://github.com/astro/collectd/blob/master/contrib/collectd-unixsock.py
- https://github.com/astro/collectd/blob/master/contrib/collectd-network.py
- https://github.com/appliedsec/collectd
- https://github.com/appliedsec/collectd/blob/3861996acde1edc2fb3335fbb61e2569a1aa2dc4/collectd.py
- https://docs.python.org/3/howto/sockets.html#socket-howto
- https://collectd.org/wiki/index.php/Plain_text_protocol
- https://collectd.org/wiki/index.php/Networking_introduction
- https://pythonhosted.org/collectd/
- https://collectd.org/documentation/manpages/collectd.conf.5.shtml
- 
