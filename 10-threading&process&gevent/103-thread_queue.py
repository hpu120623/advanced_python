# 线程间通信

import time
from threading import Thread

from tools import variables


def get_detail_html():
    # 爬取文章详情页
    # global detail_url_list # 方法一、通過共享变量的方式通信，不推荐，因为不安全
    # 方法二、直接传递detail_url_list
    while True:
        if len(variables.detail_url_list):
            # url = detail_url_list.pop() # 不是线程安全
            # for url in detail_url_list:

            print('get detail html started')
            time.sleep(1)
            print('get detail html end')


def get_detail_url():
    # 爬取文章列表页
    # global detail_url_list
    while True:
        print('get detail url started')
        time.sleep(2)
        for i in range(20):
            variables.detail_url_list.append('http://projectsedu.com/{id}'.format(id=i))
        print('get detail url end')


if __name__ == '__main__':
    thread1 = Thread(target=get_detail_url)
    for i in range(5):
        thread2 = Thread(target=get_detail_html)
        thread2.start()
