

import threading


def thread(func):
    def wrapper(*args, **args):
        threading.Thread(target=func, args=*args, kwargs=**kwargs).start()
    return wrapper
