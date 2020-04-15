#Functions

#Defining a function
def helloWorld() :
    print ("Hello from a function")

#Calling a function
helloWorld()

#Parameters

def greeting (firstName) :
    print ("Hello " + firstName)

greeting("Lee")

def fullGreeting (firstName, lastName) :
    print ("Hello %s %s" % (firstName, lastName)) #older
    print ("Hello {} {}".format(firstName, lastName))
    print ("Hello {first} {last}".format(first=firstName, last=lastName))
    print("Hello {first} {last}".format(last=lastName, first=firstName))

fullGreeting("Lee", "Assam")

#Default parameter values
def default_greeting(firstName = "John") :
    print ("Hi {}".format(firstName))


default_greeting()

default_greeting("Richard")

#Passing a list as a parameter

def myFoodList (food) :
    for item in food :
        print (item)

food = ["bread" , "apple", "ham", "banana"]

myFoodList(food)

#Returning values

def addition(num1, num2) :
    return num1 + num2

print (addition(10, 34))

#Unknown number of parameters
def sum (*numbers) :
    result = 0
    for x in numbers:
        result += x
    return result

print (sum(10, 25, 35, 100))

print (sum(30, 25, 55))


#Pass statement
def func() :
    pass

#Passing by Reference vs Passing Value

'''
All parameters (arguments) in Python are passed by reference
Changing what a parameter refers to within a function , will also change
the original value passed in
'''

def changedVar (inputList) :
    inputList.append([1,2,3,4])
    print ("Values changed inside the function : ", inputList)
    return

list = [10, 20, 30]
changedVar(list)

print ("Values outside the function: ", list)

#Reference is overwritten

def overwrite (inputList) :
    inputList = [1,2,3,4] # this would assign a new reference to inputList
    print ("Values inside the function: ", inputList)
    return

list = [10, 20, 30]
overwrite(list)

print ("Values outside the function: ", list)

#Recursion

#Factorial example

'''
5! = 5 x 4 x 3 x 2 x 1 = 120
3! = 3 x 2 x 1 = 6
'''

def fact(num) :
    result = 1
    while (num > 0):
        result *= num
        num -= 1
    return result

print (fact(5))

#defining a recursive function
def recur_factorial(n):
    if n == 1:
        return n
    else :
        return n * recur_factorial(n-1)

print (recur_factorial(5))

