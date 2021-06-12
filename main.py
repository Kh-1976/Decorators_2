import logging
from datetime import datetime as dt
import os


def parametrized_decor(parameter):
    def decorator_function(fn):
        def foo(*args):
            logging.basicConfig(filename=os.path.join(parameter, 'logger.log'), level=logging.INFO)
            result = fn(*args) + '!'
            logging.info([str(dt.now())[:-7], fn.__name__, *args, result])
            return result
        return foo
    return decorator_function


@parametrized_decor(parameter='C:\\Logs')
def func(a):
    return 'Hello ' + a


print(func('Decorator'))
