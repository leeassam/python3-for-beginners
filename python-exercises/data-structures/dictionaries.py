'''
Given an arbitrary dictionary where the values are numbers, write a python script that sums and finds the average of all the values in the dictionary

	E.g.

	Input
	numbers = { ‘data1’ : 100, ‘data2’ : 54, ‘data3’ : 247 }

	Output:

	Sum : 401
	Average : 133.67
'''
numbers = { 'data1' : 100, 'data2' : 54, 'data3' : 247 }

sum = sum(numbers.values())
avg = sum / len(numbers.values())
avg = round(avg, 2)

print ("Sum: ",sum)
print ("Average: ", avg)
