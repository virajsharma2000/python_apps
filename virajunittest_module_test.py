import virajunittest

def sum_of_numbers(number1, number2):
 return number1 + number2

testcases = virajunittest.TestCases(sum_of_numbers)

testcases.set_testcase(10, 8, 2)
testcases.set_testcase(13, 7, 6)

testcases_passed = testcases.get_testcases_passed()

print(testcases_passed)
