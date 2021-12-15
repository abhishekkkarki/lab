# Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ elseprint ‘COMMON YEAR’.
# Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
# • a year is always a leap year if its number is exactly divisible by 400
year= int(input("Enter the year "))
mod400= year%400
mod100=year%100
mod4=year%4
if mod4==0 and mod100 !=0 or mod400==0:
    value="LEAP YEAR"
else:
    value="COMMON YEAR"
print(f"The given year is a {value}")