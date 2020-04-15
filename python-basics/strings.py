#Strings

a = "Hello"
print(a)

#Multi-Line Strings

a = """This is a multi line string in
Python. You can use this method 
if there is a lot of information you want to 
assign to a string"""

print(a)

a = '''This is a multi line string in
Python. You can use this method 
if there is a lot of information you want to 
assign to a string'''

print(a)

#Strings are arrays
a = "Hello, World!"
print(a[1])

#Slicing
b = "Hello, World!"
print(b[2:5])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#String length
b = "Hello, World!"
print (len(a))

#String methods

#strip() - remove whitespaces
a = " Hello, World! "
print(a.strip())

#lower and upper case
print(a.lower())
print(a.upper())

#replace()
a = "Hello, World!"
print(a.replace("H", "J"))

#split
#split string into array where it finds the delimiter specified
a = "Hello, World!"
print(a.split(","))

#check if character(s) are present
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

#find
txt = "It is a great day to learn Python!"
print(txt.find("great")) #returns lowest index of first occurrence of search string

#isnumeric
txt = "1250"
print (txt.isnumeric())

#convert to upper case
txt = "Hello World"
print(txt.upper())

#String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#format
age = 25
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

#formatting operator
print("Hello %s, you scored %i out of %i" % ("John", 95, 100))

