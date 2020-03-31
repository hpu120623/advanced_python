# C10M:如何利用8核心CPU，64G内存，在10gbps的网络上保持1000万并发连接
"""
回调模式：单线程中实现并发
现有问题：
    1.回调模式编码复杂性搞
    2.同步编程的并发性不高
    3.多线程编程需要线程间同步。lock
达到目的：
    1.采用同步的方式去编写异步的代码
    2.使用单线程去切换任务
        a.线程是由操作系统切换，单线程切换意味着我们需要程序员自己去调度任务
        b.不在需要所，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性更高
"""

# def get_url(url):
#     # do_something
#     html = get_html(url) # 此处暂停，切换到另一个函数去执行
#     # parse html
#     urls = parse_url(html)


# 传统函数调用：过程A->B->C，每个函数都有栈，运行一次就退出的
# 我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的执行
# 出现了协程：可以暂停的函数（可以向暂停的地方传入值）

def gen_func():
    # 1.可以产出值 2.可以接收值
    html = yield 'http://projectsedu.com'
    print(html)
    yield 2
# 1.生成器不只可以产出值，还可以接收值

if __name__ == '__main__':
    gen = gen_func()
    # 1.启动生成器方式有两种，next()，send()
    # 在调用send发送非none值之前，我们必须启动一次生成器，方式有两种1.gen.send(none), 2.next(gen)
    # url = next(gen)
    url = gen.send(None)
    # download url
    html = 'python'
    gen.send(html) # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一步代码，才有可能将生成器变成协程
