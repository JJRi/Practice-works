#
#   Practice work were I got little hold on about multithreading
#   Work nmbr 2


import threading
import queue
import time

jono = queue.Queue()

for i in range(1, 31):
    jono.put(i)

def rinttaa_yksi(nmbs, lanka):
    while not nmbs.empty():
        jobi = nmbs.get()
        time.sleep(1)
        print(f'{jobi} by # {lanka} ')



t1 = threading.Thread(target=rinttaa_yksi, name='t1', args=(jono, 'T1'),)
t2 = threading.Thread(target=rinttaa_yksi, name='t2', args=(jono, 'T2'),)
t3 = threading.Thread(target=rinttaa_yksi, name='t3', args=(jono, 'T3'),)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


