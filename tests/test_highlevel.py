import pytest
from collectd_unixsock import CollectDClient
from unittest import mock

#mock_socket = mock.Mock()

@pytest.mark.skip(reason="no way of currently testing this")
def test_first():
    #ncat -lkU aSocket.sock
    c = CollectDClient('./aSocket.sock')
    o = c.listval() 
    print(o.decode())
    #assert o == b'ok\n'


def test_mock():
    with mock.patch('socket.socket') as mock_socket:
        c = Connector()
        p = c.create_plugin(

        c = CollectDClient('./aSocket.sock')
        c._socket.connect.assert_called_with('./aSocket.sock')

        c.list_val() 
        c._socket.sendall.assert_called_with(b'LISTVAL\n')

        c.put_val('test', [1,2,3])
        c._socket.sendall.assert_called_with(b'PUTVAL test  1:2:3\n')
