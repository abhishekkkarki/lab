#sum of first 10 even numbers
numbers= range(1,11)
sumA=0
for i in numbers:
    if i % 2 == 0:
        sumA+=i
print("sum of first 10 even numbers is {} " .format(sumA))
