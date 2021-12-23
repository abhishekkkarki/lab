#generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
val=int(input("Enter the range "))
dict={}
for i in range(val+1):
    dict[i]=i**2
print(dict)
