from math import *



def ab():
    BC = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    AB = sqrt((AC ** 2) - (BC ** 2))
    angleRadianA = acos(AB/AC)
    angleDegreA = degrees(angleRadianA)
    angleRadianB = acos(BC/AC)
    angleDegreB = degrees(angleRadianB)
    print("La longueur de AB vaut", AB)
    print("L'angle A vaut : ", angleDegreA )
    print("L'angle B vaut : ", angleDegreB )

def bc():
    AB = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    BC = sqrt((AC ** 2) - (AB ** 2))
    print("La longueur de BC vaut", BC)

    angleRadianA = acos(AB/AC)
    angleDegreA = degrees(angleRadianA)
    angleRadianB = acos(BC/AC)
    angleDegreB = degrees(angleRadianB)
    print("La longueur de AB vaut", AB)
    print("L'angle A vaut : ", angleDegreA )
    print("L'angle B vaut : ", angleDegreB )

def ac():
    AB = int(input("Longueur de AB : "))
    BC = int(input("Longueur de BC : "))
    AC = sqrt((AB ** 2) + (BC ** 2))
    print("La longueur de AC vaut", AC)
    angleRadianA = acos(AB/AC)
    angleDegreA = degrees(angleRadianA)
    angleRadianB = acos(BC/AC)
    angleDegreB = degrees(angleRadianB)
    print("La longueur de AB vaut", AB)
    print("L'angle A vaut : ", angleDegreA )
    print("L'angle B vaut : ", angleDegreB )
