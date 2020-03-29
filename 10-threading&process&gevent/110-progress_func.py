# concurrent和multiprocessing（更加底层）
# 共享全局变量不能适用于多进程编程，可以适用于多线程
# multiprocessing中的queue不能用于pool进程
# pool中的进程间通信需要使用manager中的queue,或者pipe
from queue import Queue
from multiprocessing import Queue
from multiprocessing import Manager

import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process

def get_html(n):
    time.sleep(n)
    print('main process started')
    return n


if __name__ == '__main__':
    process = Process(target=get_html, args=(2, ))
    process.start()
    process.join()
    print('main process end')