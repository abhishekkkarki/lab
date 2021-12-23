#find the largest number from a list
list1=[2,3,6,23,4]
a=0
g=0
for i in list1:
    if a<i:
        g=i
    a=i
print(f"The greatest number in the list is {g}")