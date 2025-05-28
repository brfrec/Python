from Fonction import *
from FonctionCalcul import *
import os

os.system("clear")

Explication()

Calcul_souhaite = int(input("Que voulez vous calculer ?\n1 - Valeur de la résistance\n2 - Valeur du condensateur\n3 - Calcul de Tau\nVotre choix:"))
if Calcul_souhaite == 1:
    calculResistance()
elif Calcul_souhaite == 2:
    calculCondensateur()
elif Calcul_souhaite == 3:
    calculTau()
else:
    print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
    exit()
