def space(planet):
 def my_decorator(func):
  def wrapper():
   print('before entering planet', planet)
   func()
   print('after exiting planet', planet)

  return wrapper

 return my_decorator


@space('earth')

def get_hello_planet():
 print('hello world')


get_hello_planet()


