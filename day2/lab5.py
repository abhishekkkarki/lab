#Given the number of students in each class, print the smallest possible number of desks
#when a desk is used for two students.
a=int(input("enter number of students in class A"))
b=int(input("enter number of students in class B"))
c=int(input("enter number of students in class c"))
desksInA=a//2
desksInB= b//2
desksInC= c//2
if a % 2!= 0 :
    desksInA +=1
if b % 2 != 0:
    desksInB +=1
if c % 2 != 0:
    desksInC +=1
total= desksInA+desksInB+desksInC
print(f"The total number of desks required is {total}")