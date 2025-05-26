from math import *
#pull
print (" Calculs divers sur oscillateurs LC")
print ("Quelle valeur voulez vous calculer ?")
print ("1. Fréquence de résonance")
print ("2. Inductance")
print ("3. Capacité")
choix = int(input("Entrez votre choix (1, 2 ou 3) : "))
if choix == 1:
    C = float(input("Entrez la capacité (en Farads) : "))
    L = float(input("Entrez l'inductance (en Henrys) : "))
    f = 1 / (2 * pi * sqrt(L * C))
    print(f"La fréquence de résonance est {f:.2f} Hz")
elif choix == 2:
    f = float(input("Entrez la fréquence de résonance (en Hz) : "))
    C = float(input("Entrez la capacité (en Farads) : "))
    L = 1 / (4 * pi**2 * f**2 * C)
    print(f"L'inductance est {L:.2e} H")
elif choix == 3:
    f = float(input("Entrez la fréquence de résonance (en Hz) : "))
    L = float(input("Entrez l'inductance (en Henrys) : "))
    C = 1 / (4 * pi**2 * f**2 * L)
    print(f"La capacité est {C:.2e} F")
else:
    print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

