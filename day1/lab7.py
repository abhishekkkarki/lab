#sum of first 10 odd numbers
numbers= range(1,11)
sumA=0
for i in numbers:
    if i % 2 == 1:
        sumA+=i
print("the sum of first 10 odd numbers is {} " .format(sumA))

 