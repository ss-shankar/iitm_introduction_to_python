class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.valid_triangle()

    def valid_triangle(self):
        if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c) > self.a:
            self.valid = True
        else:
            self.valid = False

    def is_equilateral(self):
        if self.a == self.b == self.c:
            return True
        else:
            return False

    def is_isosceles(self):
        if (self.a == self.b and self.c != self.a and self.c != self.b) or (self.c == self.b and self.c != self.a and self.b != self.a):
            return True
        else:
            return False

    def is_scalene(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return True
        else:
            return False
