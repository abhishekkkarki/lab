#sum of all items in a dictionary
dict={1:4,2:5,3:9,4:90,5:98}
sum=0
for i in dict:
    sum+=dict[i]
print(f"The sum of items is {sum}")