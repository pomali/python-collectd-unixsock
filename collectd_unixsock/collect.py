import socket
import datetime


class CollectDClient():
    def __init__(self, socket_path='/var/run/collectd-unixsock'):
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket.connect(socket_path)

    def list_val(self):
        return self._send('LISTVAL')

    def get_val(self, identifier):
        return self._send('GETVAL {}'.format(identifier))

    def put_val(self, identifier, values, options={}):
        optlist = ''
        vallist = ':'.join([str(x) for x in values])
        return self._send('PUTVAL {} {} {}'.format(identifier, optlist, vallist))

    def put_notif(
            self,
            message, 
            options={
                "severity": "warning", 
                "time": datetime.datetime.now().timestamp()}
            ):
        optlist = "severity=warning time=1201094702"
        return self._send('PUTNOTIF {} message={}'.format(optlist, message))
    
    def flush(self, optlist):
        return self._send('FLUSH {}'.format(optlist))

    def get_threshold(self, identifier):
        return self._send('GETTHRESHOLD {}'.format(identifier))


    def _send(self, command):
        message = '{}\n'.format(command).encode()
        self._socket.sendall(message)
        return self._recv_all()

    def _recv_all(self):
        data = self._socket.recv(1024)
        return data


