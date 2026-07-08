print("welcome to the python programming language !")

name = input("what is your name ?")

age = input("how old are you ?")
age = int(age)

height = input("what is your height in meters ?")
height = float(height)

current_year = 2026
birth_year = current_year - age

print("\n---profile---")
print("Name :", name)
print("Age :", age)
print("Height :", height, "meters")
print("Birth Year :", birth_year)

is_adult = age>= 18
print("Adult status :", is_adult)



