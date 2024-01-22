import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = 2 * math.pi * radius * (radius + height)
volume = math.pi * radius**2 * height

print(f"The surface area of the cylinder is {surface_area} and the volume is {volume}.")
