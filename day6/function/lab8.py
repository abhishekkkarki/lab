#function that accepts a string and calculate the number of upper case letters and lower case letters
def primeCheck(n):
    for i in range(2,n):
        if n % i==0:
            print("Composite")
            break
    else:
        print("Prime")
primeCheck(17)