#Lists

#define a list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#access element from the list
print (fruits[1])

#negative index
#get last element from the list
print (fruits[-1])

#get the second to last element from the list
print(fruits[-2])

#count of number of items in a list
print(fruits.count('apple'))

print(fruits.count('tangerine'))

#index of where an item appears
print(fruits.index('banana'))

print(fruits.index('banana', 4)) # Find index of next banana starting at position 4

#reverse the order of the elements
fruits.reverse()

print(fruits)

#add an item to the end of a list
fruits.append("grape")

print(fruits)

#insert an item at a specific index
fruits.insert(3, 'mango')

print(fruits)

#sort alphabetically
fruits.sort()

print(fruits)

#remove last list item
fruits.pop()

print(fruits)

#loop over list
for x in fruits:
    print (x)

#check if an item is in a list
if "apple" in fruits:
    print ("Yes, 'apple' is in the fruits list")

#slicing a list
print(fruits)

print (fruits[3:6]) #start at index 3 and include up to index 5, excluding 6

#print from index 4 till the end
print(fruits[4:])

#negative indexing
#start from 4th element from the right and go to the 3rd element from the right
print(fruits[-4: -2])

#remove items
print(fruits)

fruits.remove("kiwi")
fruits.remove("banana")

print(fruits)

