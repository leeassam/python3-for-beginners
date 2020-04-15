#File handling in Python

#Best way to open a file
#File will automatically be closed when the nest code block completes

#Use a+ to create a new file if it does not exist and prevent destructive overwrite
with open("data.txt", "a+") as data :
    #file is now open
    #work on file
    data.read()

#Writing to a file
with open("data.txt", "w+") as data:
    #file is now open
    #work on file
    data.write("This is the first line of text in the file\n")
    data.write("This is the second line of text in the file\n")
    data.write("This is the third line of text in the file\n")
    data.write("This is the fourth line of text in the file\n")

#Reading contents of a file
with open("data.txt", "r") as data:
    #read data from the entire file
    print(data.read())

print("\n")

#Read first n characters from a file
with open("data.txt", "r") as data:
    # read first 15 characters
    print(data.read(15))

print("\n")

#Read from the file one line at a time
with open("data.txt", "r") as data:
    # read data one line at a time
    print(data.readline() + " - Line 1")
    print(data.readline() + " - Line 2")
    print(data.readline() + " - Line 3")

print("\n")

with open("data.txt", "r") as data:
    for line in data:
        print (line)

#Read all lines at once
allLines = []
with open("data.txt", "r") as data:
    allLines = data.readlines()

print(allLines)

#File Seeks - Moving the Read/Write Pointer

'''
.seek(offset, from_what)
offset - Number of characters from the from_what parameter

from_what:
0 - beginning of the file
1 - current pointer position
2 - end of the file

'''

with open("data.txt", "r") as data:
    #set pointer to the 6th character from the beginning of the file
    data.seek(5, 0)
    print (data.readline())
    #get the pointer position
    print(data.tell())

#Editing files

#open file and get contents
with open("data.txt", "r") as data:
    contents = data.readlines()

'''
list.insert (i, x)
Data x is placed before the cell in the list indicated by i
'''

contents.insert(1, "This is a line inserted between line 1 and 2\n")

print(contents)

#Re-open to rewrite file
with open("data.txt", "w") as data:
    contents = "".join(contents)
    data.write(contents)

#Read new contents
with open("data.txt", "r") as data:
    for line in data:
        print(line)
