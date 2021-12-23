#print a specified list after removing the 0th, 4th and 5th elements 
c=0
list1=[2.5,35,767,53,234,556,988]
for i in list1:
    if c!=0 and c!=4 and c!=5:
        print(i,end=" ")
    c+=1