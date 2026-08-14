## Day 2: 30 Days of python programming
import math as math

#LEVEL 1
firstname = "eliud"
lastname = "quiroz"
fullname = "eliud quiroz"
country = "Colombia"
city= "Barranquilla"
age = 18
year = 2007
is_married = False
is_true = True
is_light_on = False
a = 2; b=3

#LEVEL 2
#1. 
print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
#2. 
print(len(firstname))
#3.
print(len(lastname) == (len(lastname)))

#4.
num_one=5; num_two=4
#5. 
total= num_one + num_two
#6.
diff= num_one-num_two
#7.
product= num_one*num_two
#8.
division= num_one/num_two
#9.
remainder= num_two%num_one
#10.
exp=num_one**num_two
#11.
floor_division = num_one//(num_two)
#12.
radius = float(input("Ingrese el radio"))
area_of_circle = math.pi*radius**2
circum_of_circle = 2*math.pi*radius
#13.
firstname = input("Ingrese el primer nombre")
lastname = input("Ingrese los apellidos")
country = input("Ingrese su pais")
age = int(input("Ingrese su edad"))
#14.
help('keywords')
