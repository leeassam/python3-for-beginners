#Conditionals and Looping

# if statement
a = 33
b = 200

if b >a :
    print("b is greater than a")

#elif - if previous conditions are not true, try this condition

a = 33
b = 33
if b > a :
    print ("b is greater than a")
elif a == b :
    print ("a and b are equal")

#else keyword catches anything which is not caught by the preceeding conditions

a = 200
b = 33
if b > a:
    print ("b is greater than a")
else :
    print("b is not greater than a")

#short hand on one line

if a > b : print ("a is greater than b")

#ternary operator

a = 2
b = 330
print ("A") if a > b else print ("B")

a, b = 10, 20
min = a if a < b else b

print(min)

#and or

a = 200
b = 33
c = 500

if a > b and c > a:
    print ("Both conditions are True")

if a > c or a > b:
    print ("At least one of the conditions is True")

#nested conditions

x = 19

if x > 10:
    print ("Above ten, ")
    if x > 20 :
        print ("and also above 20!")
    else :
        print ("but not above 20")

#pass

'''
    if statements cannot be empty, but if for some reason you want to have an if 
    statement with no content, put in the pass statement to avoid getting an error
'''

a = 33
b = 200

if b > a :
    pass

#while loops
i = 1
while i < 6:
    print (i)
    i +=1

#break statement
i = 1
while i < 6 :
    print (i)
    if i == 3:
        break
    i +=1

#continue - stop current iteration and continue with next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)

#else - enter condition when while condition is no longer true

i = 1
while i < 6:
    print (i)
    i += 1
else :
    print ("i is no longer less than 6")


#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print (x)

#range

for x in range(6):
    print(x)

for x in range(2, 6):
    print (x)

#nested loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print (x, y)

#pass statement - for loops cannot be empty. Put in a pass statement
# to avoid getting an error

for x in [0, 1, 2]:
    pass