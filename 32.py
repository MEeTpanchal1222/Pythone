import math

def circle_area(radius):
    return math.pi * radius **2 #FOR POWER **

# Test the function
radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print("The area of the circle with radius", radius, "is:", area)
