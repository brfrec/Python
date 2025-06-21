from math import *


def calculAngles (AB,BC,AC):
    angleRadianA = acos(AB/AC)
    angleDegreA = round (degrees(angleRadianA), 2)
    angleRadianB = acos(BC/AC)
    angleDegreB = round(degrees(angleRadianB), 2)
    print("L'angle A vaut : ", angleDegreA )
    print("L'angle B vaut : ", angleDegreB )
    