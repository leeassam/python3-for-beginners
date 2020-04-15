'''
Given a list of tuples, find all the tuples that contain a given element, n

	Example

	Input
	n = 10,  list = [ (12,3,10), (5,3), (11, 10, 90), (12, 13, 51)]

	Output
	[(12,3,10), (11, 10, 90)]

'''

n = 10
list = [ (12,3,10), (5,3), (11, 10, 90), (12, 13, 51)]

result = []
for x in list:
    if n in x:
        result.append(x)
print (result)