from flask import request
import threading
import time


def health_check() -> str:
    return 'Im Alive'


def trigger_async() -> str:
    data = request.data
    t = threading.Thread(target=async_method, args=(data,)).start()
    return 'Success'


def async_method(data) -> None:
    time.sleep(3)
    print('finish async Now')
