import logging
import random
import threading
import time
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s%(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
items = []
condition = threading.Condition()
# items = random.randint(0,20)
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def consume(self):
        with condition:
            if len(items) == 0:
                logging.info('no items to consume')
                condition.wait()
            items.pop()
            logging.info('consumed 1 item')
            condition.notify()

    def run(self):
        global item
        time.sleep(2)
        item = random.randint(0, 20)
        for item in range(20):
            self.consume()

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def produce(self):
        with condition:
            if len(items) == 10:
                logging.info('items produced {}.Stopped'.format(len(items)))
                condition.wait()
            items.append(1)
            logging.info('total items {}'.format(len(items)))
            condition.notify()
    def run(self):
        global item
        time.sleep(0.5)
        item = random.randint(0, 20)
        for item in range(20):
            self.produce()
def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
if __name__ == "__main__":
    main()
