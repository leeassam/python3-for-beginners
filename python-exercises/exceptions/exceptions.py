'''
Write a function that accepts two numbers and performs division. The function should throw an exception if the second number is 0 or if any of the numbers are less than 0.
'''

def division(num1, num2) :
    if num2 == 0:
        raise ZeroDivisionError ("Cannot divide by 0")
    elif num1 < 0 or num2 < 0 :
        raise ValueError ("Numbers cannot be less than 0")
    else :
        return round((num1/num2), 2)

#division(10,0)
#division(-10,2)
print(division(10,3))