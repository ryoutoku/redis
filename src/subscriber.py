import redis
import sys
import re
from multiprocessing import Process


class Subscriber(object):

    _re_format = "\'(.*?)\'"

    def __init__(self, host, port):
        self._callbacks = []
        self._connection = redis.StrictRedis(
            host=host,
            port=port
        )
        self._job = None
        self._re = re.compile(self._re_format)

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_subscriber(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def _receive_core(self, channel, end_word):
        pubsub = self._connection.pubsub()
        pubsub.subscribe([channel])
        for data in pubsub.listen():
            [x(data) for x in self._callbacks]
            if isinstance(data['data'], bytes):
                data_str = self._re.findall(data['data'].decode('utf-8'))
                if data_str[-1] == end_word:
                    break
        pubsub.unsubscribe()

    def start_receive(self, channel, end_word='end'):
        if self._job:
            return
        self._job = Process(target=self._receive_core,
                            args=(channel, end_word))
        self._job.start()

    def end_receive(self):
        self._job.join()

    def add_data(self, key, value):
        self._connection.rpush(key, value)


if __name__ == "__main__":

    host = "192.168.56.101"
    port = 6379
    channel = "test"
    subject = Subscriber(host, port)
    subject.add_callback(
        lambda x: print("callback:", x)
    )
    subject.start_receive(channel)

    while(True):
        data = sys.stdin.readline().strip()
        subject.add_data(channel, data)
        if data == "end":
            break

    subject.end_receive()
