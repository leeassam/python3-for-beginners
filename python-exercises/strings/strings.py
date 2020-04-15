'''
Write a python program that given a string, will return a count of the number of vowels in the string

	E.g. if a variable called input is set to the following:
	input = “The weather is great today”

The output result will be the vowel (if it is present) and a count of the number of times the vowel appears in the string


e - 4 times
a - 3 times
o - 1 time

'''
vowels = {}
input = "The weather is great today"
for x in input :
    if x in ["a","e","i","o","u"] :
        if x in vowels :
            vowels[x] += 1
        else :
            vowels[x] = 1
print (vowels)

#print sorted results
for index in sorted(vowels):
    print(index, ":", vowels[index])

'''

Write a program that reverses the words in a given sentence?

sentence = “There has never been a better time to learn Python”

result = “Python learn to time better a been never has there”

'''
sentence = "There has never been a better time to learn Python"
words = sentence.split()
words.reverse()
print(" ".join(words))