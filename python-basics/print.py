#print() in Python

name = "Mike"
occupation = "Programmer"
age = 34

#f string - New in Python 3
print(f'1. {name} is a {occupation} and he is {age} years old')

#format
print("2. {} is a {} and he is {} years old".format(name, occupation, age))

#Separating multiple arguments
print("3.", name, "is a", occupation, "and he is", age, "years old")
print("4.", name, "is a", occupation, "and he is", age, "years old", sep="|||")

#String concatenation
print("5. " + name + " is a " + occupation + " and he is " + str(age) + " years old")

#Older method
print ("First Name: %s Last Name: %s Integer: %i Float %f" % ("Lee", "Assam", 10, 20.5))