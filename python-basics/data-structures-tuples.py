#Tuples

#Definition
fruit = ( "apple", "banana", "cherry", "orange", "grapes", "nectarine")

print(fruit)

#Accessing elements
print (fruit[1])

#Range
print (fruit[2:5]) #start at 2 and go until index 4

#Changing tuple values
#First convert to a list

y = list (fruit)
y [1] = "guava"

#Convert back to a tuple

x = tuple(y)

print(x)

#loop through a tuple

for x in fruit:
    print(x)

#check for item
if "apple" in fruit:
    print("Yes, 'apple' is in the fruits tuple")

#join tuples
vegetables = ('carrots', 'squash')

produce = fruit + vegetables

print(produce)

#Named Tuples
#Allow you to reference each item by name rather than index
from collections import namedtuple

person = namedtuple("Person", "name age gender")
user = person (name="Fred", age = 34, gender="male")

print(user)

print(user.name)
print(user.age)
print(user.gender)