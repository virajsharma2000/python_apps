class TestCases:
 def __init__(self, function):
  self.__function = function
  self.__total_testcases = 0
  self.__testcases_passed = 0

 def set_testcase(self, result, *args):
  self.__total_testcases += 1
  self.__testcases_passed += self.__function(*args) == result
  
 def get_testcases_passed(self):
  return str(self.__testcases_passed) + '/' + str(self.__total_testcases)
