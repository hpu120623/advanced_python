# 通过queue的方式进行线程同步,Queue是线程安全的
import time
from queue import Queue
from threading import Thread

from tools import variables

def get_detail_html(queue):
    # 爬取文章详情页
    # global detail_url_list # 方法一、通過共享变量的方式通信，不推荐，因为不安全
    # 方法二、直接传递detail_url_list
    while True:
        url = queue.get()

        print('get detail html started')
        time.sleep(1)
        print('get detail html end')


def get_detail_url(queue):
    # 爬取文章列表页
    # global detail_url_list
    while True:
        print('get detail url started')
        time.sleep(2)
        for i in range(20):
            queue.put('http://projectsedu.com/{id}'.format(id=i))
        print('get detail url end')


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000) # Queue过大，会对内存造成影响
    thread1 = Thread(target=get_detail_url, args=(detail_url_queue, ))
    for i in range(5):
        thread2 = Thread(target=get_detail_html, args=(detail_url_queue, ))
        thread2.start()
