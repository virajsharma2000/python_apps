def negative_number_or_positive_number(number):
    if number < 0:
        return 'negative'

    if number == 0:
        return 'neither negative nor positive'

    if number > 0:
        return 'positive'


def get_odd_or_even(number):
    if number % 2 == 0:
        return 'even'

    else:
        return 'odd'

def get_half(number):
    return int(number / 2)

def get_power(number):
    return int(number ** number)

class Calculations:
    def __init__(self,number1,number2):
        self.num1 = number1
        self.num2 = number2

    def add(self):
        return int(self.num1 + self.num2)

    def subtract(self):
        return int(self.num1 + self.num2)

    def multiply(self):
        return int(self.num1 * self.num2)

    def divition_quotiont(self):
        return int(self.num1 / self.num2)

    def divition_remainder(self):
        return int(self.num1 % self.num2)

class Comparison:
    def __init__(self,number1,number2):
        self.num1 = number1
        self.num2 = number2

    def is_equal(self):
        return self.num1 == self.num2

    def is_greater(self):
        return self.num1 > self.num2

    def is_smaller(self):
        return self.num1 < self.num2
    
`
