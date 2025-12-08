from threading import Semaphore

class Foo:
    def __init__(self):
        self.second_ready = Semaphore(0)
        self.third_ready = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.second_ready.release()   # allow second()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_ready.acquire()   # wait for first()
        printSecond()
        self.third_ready.release()    # allow third()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_ready.acquire()    # wait for second()
        printThird()
