def rectangle_perimeter(length, width):
    return 2 * (length + width)


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = rectangle_perimeter(length, width)
print("The perimeter of the rectangle is:", perimeter)
