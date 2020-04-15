'''
1. Given a set x, find the maximum and minimum values of the set

	E.g.
	x = { 3, 29, 5, 4, 87, 34, 43, 12, 2}

	Your code should output:

	Maximum : 87
	Minimum : 3
'''

x = { 3, 29, 5, 4, 87, 34, 43, 12, 2}
print("Maximum: ", max(x), "Minimum: ", min(x))

'''
2. Given two sets that are duplicates of each other except for one value, write the code to find the missing value

	Input
	set1 = { 12, 55, 6, 7, 9, 2}
	set2 = { 9, 2, 7, 12, 6 }

	Output:
	The difference is the value 12 from set1
'''

#https://www.programiz.com/python-programming/methods/set
#https://www.programiz.com/python-programming/methods/set/difference

set1 = {12, 55, 6, 7, 9, 2}
set2 = {9, 2, 7, 12, 6}

print ("The difference is the value ", set1-set2, "from set1")