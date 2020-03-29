# Semaphore是用于控制进入数量的锁
# 文件，读、写，写一般只适用于一个线程写，读可以允许有多个

# 做爬虫
import time
from threading import Thread, Semaphore


class HtmlSpider(Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self) -> None:
        time.sleep(1)
        print('got html text success')
        self.sem.release()


class UrlProducer(Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider('https://www.baidu.com/{}'.format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
