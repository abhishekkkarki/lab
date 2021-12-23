#find the Max of three numbers
def max(a,b,c):
    if a>b:
        if a>c:
            ans=a
        else:
            ans=c
    elif b>c:
        ans=b
    else:
        ans=c
    print(f"The greatest number is {ans}")
max(1,3,2)