#Exceptions

try :
    print (x)
    print ("After our print statement")
except :
    print ("An exception occurred")


try :
    print(x)
except NameError :
    print ("Variable x is not defined")
except :
    print ("Something else went wrong")

#Else
#Execute a block of code if no errors were raised

try :
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else :
    print ("Value of x is {}".format(x))

#Finally
#Excecute block regardless of if try block raises an error or not

try :
    #x = 10 * 50
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else :
    print("Value of x is {}".format(x))
finally :
    print ("This code will always run")


#Raising your own exception

y = -1
if y < 0 :
    #raise Exception ("Your number is less than zero")
    #raise ValueError ("Your number is less than zero")
    pass


#Getting the details of an exception
try :
    with open ("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error :
    print(fnf_error)

#Assertions
y = 2
assert (y > 0) , "y cannot be less than 0"