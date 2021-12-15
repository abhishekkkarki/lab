#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user:
# Number of classes held
# Number of classes attended.
# And print percentage of class attended
# Is student is allowed to sit in exam or not.
classesHeld=int(input("Enter the total number of classes held "))
classesAttended=int(input("Enter the number of classes attended "))
percentage=(classesAttended/classesHeld)*100
if percentage>=75:
    eligibility="is allowed"
else:
    eligibility="is not allowed"
print(f"Attendance percentage: {percentage} %")
print(f"The student {eligibility} to sit in exam")

