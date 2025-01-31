#/usr/bin/env python 3
import math

name = "Merrick Crabb"
age = 18
height = 5.10
favorite_color = "Red"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"Hello: {name}, my is age is {age}, my favorite color is  {favorite_color}!")
print(f"Hello: {name}, my is age is {age:05d},my height {height:.2f}  my favorite color is  {favorite_color}!")

name = "Merrick Crabb"
name = """Merrick's 
multi-line  
string"""

print(f"""Name: {name} 
Age:{age} 
Height: {height:.2f} 
Favorite Color: {favorite_color}
""")
r = int(input("Enter the radius of circle:"))
circle_area = math.pi * math.pow(r, 2)
print(f"Circle Area with Radius {r} is {circle_area:.1f}")

print(f"square root of my age is: {math.sqrt(age)}")

print(f"sin of height: {math.sin(height)}, cos of height: {math.cos(height)}")

#The sum of age and 5.
print(f"sum of age and 5: {age + 5}")
#The difference between height and 4.
print(f"difference between height and 4 is {height - 4}")
# The product of age and height.
print(f"the product of age and height is {age * height}")
#The quotient of height and 2.
print(f"the quotient of height and 2 is {height / 2}")
# The remainder of age divided by 3
print(f"the remainder of age divided by 3 is {age % 3}")
# age raised to the power of 2.
print(f"age raised to the power of 2 {age ** 2}")

temp_fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (temp_fahrenheit - 32) * 5 / 9
print(f"Temperature {temp_fahrenheit}°F in Celsius is {celsius:.2f}°C")