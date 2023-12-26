from multiprocessing import Pool

def cube(number):
  return number*number*number

if __name__ == "__main__":
  numbers = range(10)

  pool = Pool()

  # run multiple scripts
  result = pool.map(cube,numbers)

  '''
  # need to run single script
  result = pool.apply(cube,(numbers[3],))
  '''

  pool.close()
  pool.join()

  print(result)

  print('End main')

