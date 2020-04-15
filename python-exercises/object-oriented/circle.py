'''
Create a Circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
'''

import math

class circle  :

    def __init__(self, raduis=0):
        self.radius = raduis

    def getArea(self):
        return round(math.pi * math.pow(self.radius, 2), 2)

    def getCircumference(self):
        return round(2 * math.pi * self.radius, 2)

    def compare(self, circ):
        if not isinstance(circ, circle):
            raise ValueError("A circle object is required as input")
        else :
            return True if self.getArea() >= circ.getArea() else False


def main():
    circ = circle(5)
    print("Area:", circ.getArea(), "Circumference:", circ.getCircumference())

    circ2 = circle(3)
    print(circ.compare(circ2))

if __name__ == "__main__":
    main()