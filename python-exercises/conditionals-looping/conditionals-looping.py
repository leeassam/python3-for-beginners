
odd = []
even = []
for n in range(1, 101):
    if n % 2 != 0 :
        odd.append(n)
    else :
        even.append(n)

print("Odd Numbers: ", odd)
print("Even Numbers: ", even)


myList = [1, 2, "one", "two", "three", 1.5, 3.5]
result = { "Ints" : [], "Strings" : [], "Floats" : []}

for n in myList :
    if isinstance(n, int) :
        result["Ints"].append(n)
    elif isinstance(n, float) :
        result["Floats"].append(n)
    elif isinstance(n, str) :
        result["Strings"].append(n)

print(result)