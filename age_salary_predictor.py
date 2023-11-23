import numpy
from sklearn.linear_model import LinearRegression

age = int(input('Enter age: '))

x = numpy.array([20,21,22,23,24,25,26,27,28,29,30]).reshape((-1,1))
y = numpy.array([10,20,30,40,50,60,70,80,90,100,101])

regression = LinearRegression().fit(x,y)

salary = regression.coef_ * age + regression.intercept_

print(salary)
