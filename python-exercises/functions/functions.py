'''
Write a function that takes as input any number of integer parameters. The function should return a list of the input numbers sorted in descending order
'''

def sort_result(*nums) :
    result = list(nums)
    result.sort(reverse=True)
    return result

print(sort_result(10,2,3,4,5))

print(sort_result(10,9,8,5))

'''
Write a function that accepts a sting and calculates the number of uppercase letters and lowercase letters in the string.

E.g.
Input “The weather on Monday in Atlanta is rainy”

Output:
No of uppercase characters: 3
No of lowercase characters: 31
'''

sentence = "The weather on Monday in Atlanta is rainy"
uppercase, lowercase = 0 , 0
for char in sentence:
    if char.isalpha() and char.isupper():
        uppercase += 1
    elif char.isalpha() and char.islower():
        lowercase += 1

print("No of uppercase characters:", uppercase)

print("No of lowercase characters:", lowercase)
