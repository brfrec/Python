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

def rejouer(recommencer):

    print("Autre calcul ?: ")
    try:
        choixRecommencer = int(input("1 - Oui\n2 - Non\nVotre choix :"))
    except:
        print("Entrée invalide")
    else:
        if choixRecommencer == 1:
                    recommencer = 1
        elif choixRecommencer == 2:
                    recommencer = 0
        else:
            print("Choix impossible")
    return recommencer
