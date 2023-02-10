#Bethany Berlage and Rosemary Hoffman
#Problem 5
def net_value(salary):
    value=0.14*(salary-100)+0.24*(salary+1000)
    print(value)

net_value(100)

#Problem 6
def next_stop(location):
    print("next stop is", location)
    print("next stop is", location)

next_stop("Chicago")

import math
#Problem 7
def circle(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    print("The difference between the area of a circle and its circumference is", area-circumference)

circle(2)

#Problem 8
def greeting(name):
    print("Hello", name)

greeting("Rosemary")

#Problem 9
def answer(x):
    value=(math.sin(x))**3+math.cos(x)-3*(math.tan(x)/(math.tan(x)+1)**2)
    print(value)

answer(1)


