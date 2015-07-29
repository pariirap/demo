import threading
import time

def worker(i):
    """thread worker function"""
    print ('Worker', i, 'going to sleep')
    time.sleep(10)
    print ('worker', i, 'woke up')
    return

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()