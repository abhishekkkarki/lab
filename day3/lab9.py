#Take username and password from user and check it again for the three times 
# whether the user has entered the right username and password. If yes then print a message "Logged in Successfully",
# if not then print invalid credentials for consecutive 3 times and if the limit exceeds than print "Attempt finished".
username=input("enter your username")
password=input("enter your password")
for i in range(3):
    un=input("enter your username")
    pd=input("enter your password")
    if un == username and pd == password:
        print("Logged in sucessfully")
        break
else:
    print("Attempts exceeded")