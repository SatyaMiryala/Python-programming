#For below programs collect input from user, pi is constant value 3.14 (print output in formatted way)

#write a program to calculate perimeter of the circle with radius 10.2

pi = 3.14

radius = float(input("Please enter the radius of the circle"))

perimeter = 2 * pi * radius

print("the primeter of the circle with radius {} is {}".format(radius,perimeter))



#write a program to calculate area of circle with radius (float) (collect using input function)

pi = 3.14

radius = float(input("Please enter the radius of the circle"))

area = pi *(radius**2)

print("the area of the circle with radius {} is {}".format(radius,area))

#Collect radius and height from user, calculate Area of cone (area of cone = 0.33 * pi * r * r * h) (int)

pi = 3.14

radius = float(input("Please enter the radius of the cone"))

height = float(input("Please enter the height of the cone"))

area_cone = 0.33 *  pi * radius * radius * height

print(f"The area of cone with radius {radius} and height {height} is {area_cone}")
