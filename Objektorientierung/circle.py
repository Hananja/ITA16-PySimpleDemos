# -*- coding: utf-8 -*-
#
# Kreisklasse

import math

# aus der vorgegebenen Dreiecksdatei
def getDistance(p1, p2):
    deltax = abs(p1[0] - p2[0])
    deltay = abs(p1[1] - p2[1])
    return math.sqrt(deltax ** 2 + deltay ** 2)

class Circle:
    def __init__(self, mpoint, radius): # Konstruktor
        self.mpoint = mpoint
        self.radius = radius

    def getPerimeter(self):
        return (self.radius * 2 * math.pi)

    def getArea(self):
        area = self.radius ** 2 * math.pi
        return area

    def scale(self, factor):
        self.radius = self.radius * factor

    def overlap(self, other): # TODO:
        # self ist das eigene
        # other ist das andere Objekt
        pass # TODO

circle1 = Circle((0,0), 10)
circle2 = Circle((2,1), 5)

print("C1: ", circle1.mpoint, " ", circle1.radius)
print("Umfang: ", circle1.getPerimeter())

print( circle1.scale(2) )

print("Umfang: ", circle1.getPerimeter())


print("C2: ", circle2.mpoint, " ", circle2.radius)
print("Umfang: ", circle2.getPerimeter())

print(type(circle2))


