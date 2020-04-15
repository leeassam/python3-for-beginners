import greeting
import greeting as greet #alias
from greeting import name_greeting
from greeting import fullname_greeting as full_greet

#executing a function from the module
greeting.name_greeting("Lee")

#accessing a variable from the module
greeting.person = "John"
greeting.morning_greeting()

#using an alias
greet.morning_greeting()

#import specific function from the module
name_greeting("Mark")

#import specific function with an alias
full_greet("Lisa", "Smith")

#show a list of special variables
print(dir())

if __name__ == "__main__":
    print("modules.py is being run")
    name_greeting("from main of modules.py")