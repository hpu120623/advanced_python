# 线程间同步
# Lock：在加锁和释放锁的过程中，耗费时间，速度变慢，影响并发性能
# 锁会引起死锁
# 死锁的情况A(a, b)
"""
A(a,b)
acquire(a)
acquire(b)

B(a,b)
acquire(b)
acquire(a)
解释：A线程拿到a，B线程拿到b,此时A线程等待B释放b，而B线程等待A释放a，就形成死锁
"""

from threading import Thread, Lock, RLock

# 在同一个线程里面，可以连续调用多次acquire，一定要注意，acquire的次数要和release的次数相等

total = 0
# lock = Lock()
lock = RLock()


def add():
    # 1.dosomething1
    # 2.io操作
    # 3.dosomething3
    global total
    global lock
    for i in range(1000000):
        lock.acquire() # 加锁
        lock.acquire() # 再加一次acquire()造成死锁
        total += 1
        lock.release() # 释放锁，一定要release
        lock.release() # 释放锁，一定要release


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


thread1 = Thread(target=add)
thread2 = Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
