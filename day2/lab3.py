#convert given minutes into time displayed in digital clock
minutes=int(input("enter the time in minutes"))
hours= minutes//60
remaining= minutes % 60
print(f"the time displayed is {hours}:{remaining}")