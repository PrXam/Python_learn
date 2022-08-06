import socket
import time


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        try:
            self.sock = socket.create_connection((host, port), timeout)
        except socket.error:
            raise ClientError

    def put(self, metric, num_value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        self.sock.sendall((' '.join(['put', metric, str(num_value), str(timestamp)]) + '\n').encode("utf8"))
        data = None
        while not data:
            data = self.sock.recv(1024)
        data = data.decode("utf8")
        if data.partition('\n')[0] != 'ok':
            raise ClientError

    def get(self, metric):
        self.sock.sendall((' '.join(['get', metric]) + '\n').encode("utf8"))
        data = None
        while not data:
            data = self.sock.recv(4096)
        data = data.decode("utf8")
        data = data[:-2:]
        data = data.split('\n')
        if data.pop(0) != 'ok':
            raise ClientError
        else:
            diction_response = {}
            try:
                for line in data:
                    line_split = line.split(' ')
                    if diction_response.get(line_split[0]) is None:
                        diction_response[line_split[0]] = []
                    diction_response[line_split[0]].append((int(line_split[2]), float(line_split[1])))
                    diction_response[line_split[0]].sort()
                return diction_response
            except (IndexError, ValueError):
                raise ClientError

    def close(self):
        self.sock.close()


