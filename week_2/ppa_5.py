"""
Write a program to realize the equation of a line given 2 points in 2D space.
The input is in 5 lines where, the first, second, third, and fourth lines
represent x1, y1, x2, y2 respectively. The fifth line corresponds to x3
​Determine y3 using the equation of a straight line.

The output should be "Vertical Line" if the line is vertical.
In other cases, the output should be 2 lined,
        where the first line is the value of y3
        and the second line indicates whether the slope of the line is
        positive, negative or zero. Print "Positive Slope", "Negative Slope" or
        "Horizontal Line" accordingly.
  """
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())

if (x2 - x1) == 0:
    print("Vertical Line")
else:
    m = (y2 - y1) / (x2 - x1)
    y3 = ((x3 - x1) * m) + y1
    if m > 0:
        print(y3)
        print("Positive Slope")
    elif m < 0:
        print(y3)
        print("Negative Slope")
    elif m == 0:
        print(y3)
        print("Horizontal Line")
