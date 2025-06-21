from math import *


def calculAngles (AB,BC,AC):
    angleRadianA = acos(AB/AC)
    angleDegreA = degrees(angleRadianA)
    angleRadianB = acos(BC/AC)
    angleDegreB = degrees(angleRadianB)
    print("L'angle A vaut : ", angleDegreA )
    print("L'angle B vaut : ", angleDegreB )
    
