import redis
import asyncio


class Publisher(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._connection = redis.StrictRedis(
            host=self._host,
            port=self._port
        )
        self._data = {}

    def send_message(self):

        while True:
            keys = self._connection.keys()

            is_break = False
            for key in keys:
                old_data = self._data.setdefault(key, [])
                data = self._connection.lrange(key, 0, -1)

                if len(old_data) == len(data):
                    continue

                key_str = key.decode('utf-8')
                data_str = [x.decode('utf-8') for x in data]

                print("publish:", data_str)

                self._connection.publish(key_str, data_str)
                self._data[key] = data
                if data_str[-1] == "end":
                    self._connection.rpop(key)
                    is_break = True
            if is_break:
                break


if __name__ == "__main__":

    host = "192.168.56.101"
    port = 6379

    publisher = Publisher(host, port)

    publisher.send_message()
