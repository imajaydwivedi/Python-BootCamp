from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time

def square(numbers,queue):
  for i in numbers:
    queue.put(i*i)

def make_negative(numbers,queue):
  for i in numbers:
    queue.put(-i)

if __name__ == "__main__":
  q = Queue()

  numbers = [0,1,2,3,5,10,20,100]

  #print(f'start value is {numbers[:]}')

  p1 = Process(target=square, args=(numbers,q))
  p2 = Process(target=make_negative, args=(numbers,q))

  p1.start()
  p2.start()

  p1.join
  p2.join

  #print(f'end value is {numbers[:]}')
  print(q.qsize())
  while not q.empty():
    print(q.get())

  print(f"End main")
