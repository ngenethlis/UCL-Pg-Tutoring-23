# Python Script to showcase testing


# Program to be tested:

class Rectangle:

    def __init__(self, h, w):
        if h < 0 or w < 0:
            raise ValueError("Height and width must be positive")
        self.height = h
        self.width = w

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return 2 * (self.height + self.width)

    def getDiagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5


class Square(Rectangle):

    def __init__(self, s):
        super().__init__(s, s)

    def getSide(self):
        return self.height

    def setSide(self, s):
        self.height = s
        self.width = s

    def setHeight(self, h):
        self.height = h
        self.width = h

    def setWidth(self, w):
        self.height = w
        self.width = w
