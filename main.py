import logging
from datetime import datetime as dt
import os


def decorator_function(fn):

    def foo(*args, **kwargs):
        path = kwargs['path']
        logging.basicConfig(filename=os.path.join(path, 'logger.log'), level=logging.INFO)
        logging.info([str(dt.now())[:-7], fn.__name__, *args, fn(*args) + '!'])
        return fn(*args) + '!'
    return foo


@decorator_function
def func(a):
    return 'Hello ' + a


print(func('Decorator',  path='C:\\Logs'))
