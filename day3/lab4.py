#Given three integers, print the smallest one. (Three integers should be user input) 
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a<b and a<c:
    print(f"The smallest number is {a}")
if b<c and b<a:
    print(f"The smallest number is {b}")
if c<a and c<b:
    print(f"The smallest number is {c}")