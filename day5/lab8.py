#Fibonacci series between 0 to 50
a=0
b=1
print(a,b,end=" ")
while True:
    c=a+b
    a=b
    b=c
    if c>=50:
        break
    print(c,end=" ")