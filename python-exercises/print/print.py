'''
Given the following two variables
name = “John Banks”
age = 34

Write a print() statement using the f string notation, substituting the variables where necessary that will display on the console:

Hi, my name is John Banks and I am 34 years old

'''

name = "John Banks"
age = 34

print(f" Hi, my  name is {name} and I am {age} years old")

'''
Given that
x, y = 10, 12

Write the code using the format() command in a print() statement substituting the values of the variables x and y that will display the following on the console

The result of 10 + 12 is 22
'''

x, y = 10, 12

print("The result of {} + {} is {}".format(x, y, x+y))
