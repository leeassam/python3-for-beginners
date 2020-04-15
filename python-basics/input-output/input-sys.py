import sys

#send output
print ("Hello {} {}".format(sys.argv[1], sys.argv[2]))

print(sys.argv[0])

print (len(sys.argv))

for arg in sys.argv :
    print(arg)