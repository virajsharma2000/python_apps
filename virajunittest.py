class TestCases:
 def __init__(self, function):
  self.__function = function
  self.__total_testcases = 0
  self.__testcases_passed = 0
  self.__faild_testcases_list = []

 def set_testcase(self, result, *args):
  self.__total_testcases += 1

  if not self.__function(*args) == result:
   self.__faild_testcases_list.append({'result':result, 'arguments':args})

  else:
   self.__testcases_passed += 1
  
 def get_testcases_passed(self):
  return str(self.__testcases_passed) + '/' + str(self.__total_testcases)

 def get_faild_testcases_list(self):
  return self.__faild_testcases_list

