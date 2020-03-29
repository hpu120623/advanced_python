# 对于IO操作来说，多线程和多进程性能差别不大，线程比进程更加轻量级
# 1.通过thread类实例化

import time
from threading import Thread


def get_detail_html(url):
    print('get detail html started')
    time.sleep(1)
    print('get detail html end')


def get_detail_url(url):
    print('get detail url started')
    time.sleep(2)
    print('get detail url end')


if __name__ == '__main__':
    thread1 = Thread(target=get_detail_html, args=('',))
    thread2 = Thread(target=get_detail_url, args=('',))
    # thread1.setDaemon(True) # setDaemon为守护线程
    # thread2.setDaemon(True)

    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # 当主线程退出的时候，子线程kill掉
    print(f'last_time:{time.time() - start_time}')

# 2.通过集成Thread来实现多线程
class GetDetailHtml(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print('get detail html started')
        time.sleep(1)
        print('get detail html end')


class GetDetailUrl(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print('get detail url started')
        time.sleep(1)
        print('get detail url end')

if __name__ == '__main__':
    thread1 = GetDetailHtml('get_detail_html')
    thread2 = GetDetailUrl('get_detail_url')
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(f'last_time:{time.time() - start_time}')
