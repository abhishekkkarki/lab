#take number of apples and people and divide accordingly
apples= int(input("enter the number of apples"))
people= int(input("enter the number of people"))
divided= apples// people
basket= apples% people
print(f"each person gets {divided} apples and {basket} apples remaining in the basket")