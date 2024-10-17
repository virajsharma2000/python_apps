import virajunittest

def sum_of_numbers(number1, number2):
 return number1 + number2

def sum_of_numbers2(number1, number2):
 return number1 + 1

print('unittesting of function 1')

print('\n')

testcases = virajunittest.TestCases(sum_of_numbers)

testcases.set_testcase(10, 8, 2)
testcases.set_testcase(13, 7, 6)

testcases_passed = testcases.get_testcases_passed()
testcases_faild_list = testcases.get_faild_testcases_list()

print('testcases passed', testcases_passed)
print('testcases faild list', testcases_faild_list)

print('\n')

print('unittesting of function2')

print('\n')

testcases = virajunittest.TestCases(sum_of_numbers2)

testcases.set_testcase(9, 8, 1)
testcases.set_testcase(6, 5, 1)
testcases.set_testcase(10, 8, 2)
testcases.set_testcase(11, 7, 4)

testcases_passed_list = testcases.get_testcases_passed()
testcases_faild_list = testcases.get_faild_testcases_list()

print('testcases passed', testcases_passed_list)
print('testcases faild list', testcases_faild_list)
