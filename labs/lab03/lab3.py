import math

class Shape():
    def __init__(self):
        pass
    def getArea():
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
    
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def getArea(self):
        return (self.b * self.h) / 2

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return (math.pi * pow(self.r, 2))
    
file = open("shapes.txt", "r")
shape_list = file.readlines()
for line in shape_list:
    tokens = line.strip().split(",")
    if tokens[0] == "Triangle":
        b = float(tokens[1])
        h = float(tokens[2])
        shape = Triangle(b, h)
    elif tokens[0] == "Rectangle":
        l = float(tokens[1])
        w = float(tokens[2])
        shape = Rectangle(l, w)
    else:
        r = float(tokens[1])
        shape = Circle(r)
    print(shape.getArea())

file.close()