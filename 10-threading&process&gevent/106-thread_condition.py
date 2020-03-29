# 线程通信：条件变量：用于复杂的线程间通信
from threading import Condition, Thread


# 通过condition完成协同读诗
# condition有两把锁，一把底层所会在线程调用了wait方法的时候释放，上面的会在每次调用wait的时候分配一把并放入到condition的队列中
# 等待notify的唤醒
class XiaoAi(Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
            self.cond.wait()
            print(f'{self.name}: 在')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 好吧')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 共饮长江水')
            self.cond.notify()


class TianMao(Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self) -> None:
        # 在调用with方法后才能调用wait、notify
        with self.cond:
            print(f'{self.name}: 小爱同学')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 我们来对古诗吧')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 我住长江头')
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # tianmao.start() # 启动顺序很重要
    xiaoai.start()
    tianmao.start()
