#WAP which accepts marks of four subjects and display total marks, percentage and grade. 
#Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
subjectA=int(input("enter the marks for maths"))
subjectB=int(input("enter the marks for physics"))
subjectC=int(input("enter the marks for chemistry"))
subjectD= int(input("enter the marks for computing"))
total= subjectA+ subjectB+ subjectC+ subjectD
percentage= total/4
if percentage>= 70:
    division="distinction"
elif percentage>=60:
    division="first"
elif percentage>= 40:
    division="pass"
else:
    division="fail"
print(f"Maths: {subjectA}")
print(f"Physics: {subjectB}")
print(f"Chemistry: {subjectC}")
print(f"Computing: {subjectD}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage}")
print(f"Division: {division}")