#Given a n-digit number. Find the sum of its digits.
a= input("enter the number")
sum=0
for i in str(a):
    sum += int(i)
print(f"The sum of digits in {a} is {sum}")