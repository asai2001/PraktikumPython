from threading import Thread
from queue import Queue
import time
import random
class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        for i in range(20):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify : item N°%d appended to queue by %s\n' \
                  % (item, self.name))
            time.sleep(1)
class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify : %d popped from queue by %s' \
                  % (item, self.name))
            self.queue.task_done()
if __name__ == '__main__':
    queue = Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    t5 = Consumer(queue)
    t6 = Consumer(queue)
    t7 = Consumer(queue)
    t8 = Consumer(queue)
    t9 = Consumer(queue)
    t10 = Consumer(queue)
    t11 = Consumer(queue)
    t12 = Consumer(queue)
    t13 = Consumer(queue)
    t14 = Consumer(queue)
    t15 = Consumer(queue)
    t16 = Consumer(queue)
    t17 = Consumer(queue)
    t18 = Consumer(queue)
    t19 = Consumer(queue)
    t20 = Consumer(queue)


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()