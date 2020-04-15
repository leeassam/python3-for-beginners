#Import Argument Parser Library
import argparse

#Create a parser
parser = argparse.ArgumentParser(description="Enter your first name and your last name")

#Add arguments
parser.add_argument("-f", required=True, help="First Name")
parser.add_argument("-l", required=True, help="Last Name")

#Extract arguments
args = parser.parse_args()

#Send output
print ("Hello {} {}".format(args.f,args.l))

