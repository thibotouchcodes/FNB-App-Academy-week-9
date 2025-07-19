import calculate

unit = input("Enter the unit of measurement (e.g., cm, m, inches): ")
print("\n")
length = float(input(f"Enter the length of the rectangle ({unit}): "))
print("\n")
width = float(input(f"Enter the width of the rectangle ({unit}): "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)
print("\n")
print(f"The area of the rectangle is {area:.2f}{unit}²")
print("\n")
print(f"The perimeter of the rectangle is {perimeter:.2f}{unit}")
print("\n")