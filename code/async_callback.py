from tornado import ioloop
from tornado.concurrent import Future


def callback(future):
    print 'callback!'
    future.set_result(1)

def async_func():
    future = Future()
    future.add_done_callback(callback)
    return future

result = ioloop.IOLoop.current().run_sync(async_func)
