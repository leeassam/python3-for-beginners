'''
Given a list of employees, write the code to extract the second to last employee from the list? Assume that you do not know how long the list initially is.

E.g.

employees = [“John Smith”, “Frank Jacobs”, “Scott Anderson”, “Mary Smith”, “Jim Bates”]

You code should print out :
Mary Smith
On the output console
'''

employees = ["John Smith", "Frank Jacobs", "Scott Anderson", "Mary Smith", "Jim Bates"]

print (employees[len(employees)-2])


'''
Given a list of movies, write the code that will sort the list alphabetically and remove duplicates that might exist

E.g.
movies = [‘Inception’, ‘Aladin’, ‘Avatar’, ‘Inception’ ]

Result:
movies = [‘Aladin’, ‘Avatar’, ‘Inception’ ]

'''

#Convert to a set to remove duplicates, then convert to a list again and sort
movies = ['Inception', 'Aladin', 'Avatar', 'Inception' ]
movies = list(set(movies))
movies.sort()
print(movies)