#Defining a class

class Person :
    #1. Constructor
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    #2. Methods
    def fullName(self):
        return f'{self.firstName} {self.lastName}'


#3. Inheritance

class Customer (Person) :
    def __init__(self, id, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        self._id = id

    def getBalance(self):
        return 10

    def getCustomerId (self):
        return str(self._id)

class Employee (Person):
    def __init__(self, id, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        #private variable
        self.__id = id

    def getDepartment(self):
        #retrieve from database
        return "Sales"

    def getYearsOfService(self):
        return 5

    def getEmployeeID(self):
        return str(self.__id)

#Creating a Person Object
p = Person("Mike", "Smith", 35)

print (p.firstName)
print (p.age)

print(p.fullName())

# Creating a Customer
c = Customer(34, "Mary", "Smith", 40)

print (c.fullName())

#accessing private variables
c = Customer(34, "Mary", "Smith", 40)
print (c._id)
print (c.getCustomerId())

e = Employee(50, "Harold", "Thompson", 55)

#print (e.__id)

print(e.getEmployeeID())

print(e._Employee__id)