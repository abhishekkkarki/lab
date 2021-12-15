#Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
c=int(input("Enter the third number "))
if a==b or a==c or b==c:
    answer=0
else:
    answer=a+b+c
print(answer)