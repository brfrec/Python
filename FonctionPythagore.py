from math import *



def ab():
    BC = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    AB = sqrt((AC ** 2) - (BC ** 2))
    print("La longueur de AB vaut", AB)

def bc():
    AB = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    BC = sqrt((AC ** 2) - (AB ** 2))
    print("La longueur de BC vaut", BC)

def ac():
    AB = int(input("Longueur de AB : "))
    BC = int(input("Longueur de BC : "))
    AC = sqrt((AB ** 2) + (BC ** 2))
    print("La longueur de AC vaut", AC)

def longeur():
    if choix_calcul == 1:
        ab()

    elif choix_calcul == 2:
        bc()

    elif choix_calcul == 3:
        ac()

    else:
        print("Ce choix n'est pas proposé")