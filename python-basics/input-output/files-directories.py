#Working with files and directories
import os
#Create a directory
if (not os.path.isdir(os.getcwd() + "/files")) :
    os.mkdir("files")

#Place a file in the directory
with open ("files/test.txt", "w") as data:
    data.write("This is a test file")

#Rename file
os.rename("files/test.txt", "files/test2.txt")

#Delete a file
os.remove("files/test2.txt")

#Delete a directory
os.rmdir("files")