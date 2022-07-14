"""
We are going to model points in 2D space as objects of a class named Point.
Define a class named Point that has the following specification:

Attributes
    (1) x: int, x-coordinate of the point in 2D space.
    (2) y: int, y-coordinate of the point in 2D space.

Methods
    self is the first argument of all methods. We will only mention the
additional arguments, if any.
    (1) __init__: constructor with two arguments — x and y; assign these two
values to the corresponding attributes within the constructor
    (2) distance: return the distance of the point from the origin as a float
value
    (3) is_origin: return True if the point coincides with the origin, and
False otherwise
    (4) on_xaxis: return True if the point is on the x-axis, and False
otherwise
    (5) on_yaxis: return True if the point is on the y-axis and False otherwise
    (6) quadrant: return the quadrant that this point belongs to; assume that
this method will only be called if the point is not on either of the axes;
possible return values are ['first', 'second', 'third', 'fourth'].
    (7) slope: return the slope of the line joining the origin and this point
as a float value; assume that this method will only be called if the point
is not on the y-axis
"""

import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        distance = math.sqrt(self.x**2 + self.y ** 2)
        return distance

    def is_origin(self):
        if self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def on_xaxis(self):
        if self.y == 0:
            return True
        else:
            return False

    def on_yaxis(self):
        if self.x == 0:
            return True
        else:
            return False

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return 'first'
        elif self.x > 0 and self.y < 0:
            return 'fourth'
        elif self.x < 0 and self.y > 0:
            return 'second'
        elif self.x < 0 and self.y < 0:
            return 'third'

    def slope(self):
        if self.x == 0:
            slope = 0
        else:
            slope = self.y / self.x
        return slope
