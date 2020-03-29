# 多进程编程:ProcessPoolExecutor
# 耗CPU的操作，用多进程编程，对于IO操作来说，使用多线程，进程切换代价高于线程
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor

# 1.对于CPU操作来说，多进程优于多线程
def fib(index):
    if index <= 2:
        return 1
    return fib(index - 1) + fib(index - 2)

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
    # with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, num) for num in range(30, 40)]
        start_time = time.time()
        for future in as_completed(all_task):
            print(f'exec result: {future.result()}')

        print('last time is: {}'.format(time.time() - start_time))


# 2.对于IO操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
    # with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 20]
        start_time = time.time()
        for future in as_completed(all_task):
            print(f'exec result: {future.result()}')

        print('last time is: {}'.format(time.time() - start_time))