from threading import Thread, Lock
from queue import Queue
import time

if __name__ == "__main__":

  q = Queue()

  q.put(1)
  q.put(2)
  q.put(3)

  first = q.get()
  print(first)

  q.task_done()
  q.join()

  print('end main')