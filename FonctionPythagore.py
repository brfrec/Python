from math import *
from Angles import *



def ab():
    BC = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    AB = sqrt((AC ** 2) - (BC ** 2))
    print("La longueur de AB vaut", AB)
    calculAngles (AB,BC,AC)

def bc():
    AB = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    BC = sqrt((AC ** 2) - (AB ** 2))
    print("La longueur de BC vaut", BC)
    calculAngles (AB,BC,AC)
    
    
   

def ac():
    AB = int(input("Longueur de AB : "))
    BC = int(input("Longueur de BC : "))
    AC = sqrt((AB ** 2) + (BC ** 2))
    print("La longueur de AC vaut", AC)
    calculAngles (AB,BC,AC)