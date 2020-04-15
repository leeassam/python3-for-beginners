
odd = []
even = []
for n in range(1, 101):
    if n % 2 != 0 :
        odd.append(n)
    else :
        even.append(n)

print("Odd Numbers: ", odd)
print("Even Numbers: ", even)