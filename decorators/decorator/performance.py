import time

# getting performance

def get_performance(func):
 def wrapper():
  start_time = time.time()
  func()
  end_time = time.time()

  return end_time - start_time

 return wrapper

# logging

def logging(func):
 def wrapper():
  print('function started')
  func()
  print('function ended')

 return wrapper
