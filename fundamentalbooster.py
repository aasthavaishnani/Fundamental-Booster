print("\nWelcome User :)")
print("It collects basic informations\n")

name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
height = float(input("Enter your Height in inches : "))
fnum = int(input("Enter your Favourite Number : "))

print("\nThank youuu :)")
print("Processing...")

currentyear = 2026
birthyear = currentyear - age

print("\ndetails : ")
print(f"Name : ")
print(f"type : {type(name)}",end=", ")
print(f"memory add : {id(name)}",end=", ")
print(f"value : {name} \n")

print(f"Age : ")
print(f"type : {type(age)}",end=", ")
print(f"memory add : {id(age)}",end=", ")
print(f"value : {age} \n")

print(f"Height : ")
print(f"type : {type(height)}",end=", ")
print(f"memory add : {id(height)}",end=", ")
print(f"value : {height} \n")

print(f"Favourite Number : ")
print(f"type : {type(fnum)}",end=", ")
print(f"memory add : {id(fnum)}",end=", ")
print(f"value : {fnum} \n")

print("Entered Details of User ->\n")
print(f"Hello {name}!")
print(f"You are {age} years old and born in {birthyear}.")
print(f"Your height is {height} Inches.")
print(f"Your favourite number is {fnum}. \n")

print("Thank you !! ")
print("Good Bye :) :) :) ")