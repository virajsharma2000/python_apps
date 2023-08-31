# making sure that the file runs by importing only

if __name__ == 'pyalgebra':

 # in this library we are solving the equation of x + y = z,x - y = z,x * y = z and z / y = z when both x and y are filled then raise a type error and if x is filled or y is filled then calculate the answer of the equation and if neither x is filled nor y is filled then raise a type error
 
 def solve_addition_equation(x,y,z):
    if x == 0:
        x_value = z - y

        return x_value
         
    if y == 0:
        y_value = z - x

        return y_value

    if x != 0 and y != 0:
        raise TypeError('You can only fill x number or y number,you cannot fill both x and y')

    if x == 0 and y == 0:
        raise TypeError('You need to fill x or y')

 def solve_substraction_equation(x,y,z):
    if x == 0:
        x_value = z + y

        return x_value

    if y == 0:
        y_value = x - z

        return y_value

    if x != 0 and y != 0:
        raise TypeError('You can only fill x number or y number,you cannot fill both x and y')

    if not x != 0 and y != 0:
        raise TypeError('You need to fill x or y')

 def solve_multiplication_equation(x,y,z):
    if x == 0:
        x_value = z / y

        return x_value

    if y == 0:
        y_value = z / x

        return y_value

    if x != 0 and y != 0:
        raise TypeError('You can only fill x number or y number,you cannot fill both x and y')

    if not x != 0 and y != 0:
        raise TypeError('You need to fill x or y')

 def solve_division_equation(x,y,z):
    if x == 0:
        x_value = z * y

        return x_value

    if y == 0:
        y_value = z / x
        
        return y_value

    if x != 0 and y != 0:
        raise TypeError('You can only fill x number or y number,you cannot fill both x and y')

    if not x != 0 and y != 0:
        raise TypeError('You need to fill x or y')

    

    



         
