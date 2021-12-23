#find the factorial of a number using functions
def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    print(f"The factorial of {num} is {result}")
factorial(4)