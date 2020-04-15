#Sets

fruits = { "apple", "banana", "cherry"}

print(fruits)

#Access Items
for x in fruits:
    print(x)

#Adding one item
fruits.add("orange")

print(fruits)

#Adding multiple items
fruits.update(["mango", "kiwi", "strawberry"])

print(fruits)

#Get the length of a set
print(len(fruits))

#Remove an item
fruits.remove("kiwi")

print(fruits)

#use discard() to remove items. If the item does not exist, no error will be raised

fruits.discard("guava")

#empty the set

#fruits.clear()

print(fruits)

#join two sets - union
vegetables = {"carrots", "squash"}

produce = fruits.union(vegetables)

print(produce)

#update
#insert the items in set 2 into set 1

set1 = {"a" , "b", "c", "d"}
set2 = {1 , 2 , 3}

set1.update(set2)

print(set1)

#both update and union will exclude duplicate items

#Frozen set - immutable

names = frozenset(["Jim", "John", "Mike"])

print (names)

#names.remove("Jim")

#names.update ({"Mary", "Jane"})

print(names)