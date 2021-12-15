#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".
age=int(input("Enter the age "))
gender=input("Enter the gender: M or F ")
gender= gender.upper()
if age>20 or age<60:
    print("ERROR")
elif gender=="F":
    result="she will work inurban areas only"
elif age<40 and age>20:
    result="He will work anywhere"
elif age<60 and age>40:
    result="He will work in urban areas only"
