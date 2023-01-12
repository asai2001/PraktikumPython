import logging
import threading
import time

import random
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s%(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
semaphore = threading.Semaphore(0)
# for item in range(11):
# item = [10, 9, 8, 6, 5, 4, 3, 2, 1]
# item.sort()
def consumer():
    # for item in range(11):
    lst=list(range(100))
    lst.sort(reverse=True)
    for i in range(10):
        logging.info('Consumer is waiting')
        semaphore.acquire()
        logging.info('Consumer notify: item number {}'.format(lst[i]))


def producer():
    lst=list(range(100))
    lst.sort(reverse=True)
    for i in range(10):
        # item = [5, 7, 4, 6, 9, 8]
        # item.sort
        # for item in range(11):
        time.sleep(3)
        logging.info('Producer notify: item number {}'.format(lst[i]))
        semaphore.release()

# def penjual():
#     lst=list(range(100))
#     lst.sort(reverse=True)
#     for i in range(10):
#         # item = [5, 7, 4, 6, 9, 8]
#         # item.sort
#         # for item in range(11):
#         # time.sleep(3)
#         logging.info('Penjual notify: item number {}'.format(lst[i]))
#         semaphore.acquire()

def main():
    # for i in range(3):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        # t3 = threading.Thread(target=penjual)

        t1.start()
        t2.start()
        # t3.start()

        t1.join()
        t2.join()
        # t3.join()
if __name__ == "__main__":
    main()
