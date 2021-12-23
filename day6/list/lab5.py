#count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
list1=["absjsa","a","abak","sass","12341"]
c=0
for i in list1:
    if len(i)>2:
        if i[0]==i[len(i)-1]:
            c+=1
print(c)