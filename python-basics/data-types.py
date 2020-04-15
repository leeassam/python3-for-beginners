x = 10

#Getting the data types
print (type(x))

x = "Hello World"
print (type(x))

x = 20.5
print (type(x))

x = ["apple", "banana", "cherry"]
print (type(x))

x = {"name" : "John", "age" : 34}
print (type(x))

x = {"apple", "banana", "cherry"}
print (type(x))

x = True
print (type(x))

x = bytearray(5)
print (type(x))

x = memoryview(bytes(5))
print (type(x))

#setting specific data type
x = str("Hello World")
print (type(x))

x = int(20)
print (type(x))

x = float(20.5)
print (type(x))

x = list(("apple", "banana", "cherry"))
print (type(x))

x = tuple(("apple", "banana", "cherry"))
print (type(x))

x = dict(name="John", age=34)
print (type(x))

x = set(("apple", "banana", "cherry"))
print (type(x))

x = frozenset(("apple", "banana", "cherry"))
print (type(x))

x = bool(5)
print (type(x))

#Conversion
x = 1 #int
y = 2.3 #float

#Convert from int to float
a = float(x)

#Convert from float to int
b = int(y)

print(a)
print(b)

print(type(a))
print(type(b))

#Casting
x = float(1)
y = float (2.8)
z = float ("3")
w = float ("4.2")

print(x, type(x), y, type(y), z, type(z), w, type(w))

#Strings
x = str("s1")
y = str(2)
z = str(3.0)

print(x, type(x), y, type(y), z, type(z))
