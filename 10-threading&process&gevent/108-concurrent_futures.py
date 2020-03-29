# 线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程接口一致

import time
from concurrent.futures import ThreadPoolExecutor, as_completed, Future

# Future:未来对象，task的返回容器，非常重要！！！

def get_html(times):
    time.sleep(times)
    print('get page {} success'.format(times))
    return times

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    # # 通过submit函数提交执行的函数到线程池中，submit是立即返回，是非阻塞的
    # task1 = executor.submit(get_html, (3))
    # task2 = executor.submit(get_html, (2))

    # # done方法，用于判定任务是否完成
    # print(task1.done())
    # # cancel在线程没有执行时，可以取消
    # print(task2.cancel())
    # time.sleep(4)
    # print(task1.done())
    # # result方法可以获取task的执行结果
    # print(task1.result())

    # as_completed获取已经成功的task的返回
    urls = [2, 3, 4, 5]
    all_task = [executor.submit(get_html, url) for url in urls]
    # for future in as_completed(all_task):
    #     data  = future.result()
    #     print('get {} page success'.format(data))

    # 通过executor获取已经完成的task
    for data in executor.map(get_html, urls):
        print('get {} page success'.format(data))
