person = ""

def name_greeting(name) :
    print ("Hello " + name)

def fullname_greeting(firstName, lastName) :
    print("Hello {} {}".format(firstName, lastName))

def morning_greeting():
    print("Good morning to you {}".format(person))

def afternoon_greeting():
    print("Good afternoon {}".format(person))

if __name__ == "__main__":
    print("greeting.py is being run")
    name_greeting("from main of greeting.py")
else :
    print ("greeting.py is being imported")