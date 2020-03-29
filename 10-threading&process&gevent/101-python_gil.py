# GIL:global interpreter lock
# GIL使得同一时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上
# GIL会根据执行的字节码行数以及时间片释放GIL，在遇到IO操作的时候主动释放，使得Python在IO操作的时候很有用

# import dis
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))
from threading import Thread

total = 0

def add():
    # 1.dosomething1
    # 2.io操作
    # 3.dosomething3
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

thread1 = Thread(target=add)
thread2 = Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)