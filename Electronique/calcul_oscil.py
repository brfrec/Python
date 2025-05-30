from math import *
# Calculs divers sur oscillateurs LC
encore = 1
def Dire_aurevoir():
    print("Merci d'avoir utilisé le calculateur d'oscillateurs LC.")
    print("Au revoir !")
while encore == 1:
    
    print("Calculateur d'oscillateurs LC")
    print("1. Fréquence de résonance")
    print("2. Inductance")
    print("3. Capacité")
    
    choix = int(input("Entrez votre choix (1, 2 ou 3) : "))
      
    if choix == 1:
        C = float(input("Entrez la capacité (en Farads) : "))
        L = float(input("Entrez l'inductance (en Henrys) : "))
        f = 1 / (2 * pi * sqrt(L * C))
        ZL = 2*pi * L * f  # Impédance de l'inductance
        ZC = 1 / (2 * pi * f * C) # Impédance de la capacité
        print("La fréquence de résonnance est a:", f, "Hz")
        print("L'impédance de l'inductance est ", ZL," Ohms")
        print("L'impédance de la capacité est", ZC," Ohms")
        recommencer = int(input("Voulez vous faire un autre calcul ? (1 pour oui, 0 pour non)"))
        if recommencer == 0:
            encore = 0
            Dire_aurevoir()
        elif recommencer == 1:
            encore = 1    

    elif choix == 2:
        f = float(input("Entrez la fréquence de résonance (en Hz) : "))
        C = float(input("Entrez la capacité (en Farads) : "))
        L = 1 / (4 * pi**2 * f**2 * C)
        ZL = 2*pi * L * f  # Impédance de l'inductance
        ZC = 1 / (2 * pi * f * C) # Impédance de la capacité
        print(f"L'inductance est ", L," H")
        print(f"L'impédance de l'inductance est", ZL," Ohms")
        print(f"L'impédance de la capacité est ", ZC," Ohms")
        recommencer = int(input("Voulez vous faire un autre calcul ? (1 pour oui, 0 pour non)"))
        if recommencer == 0:
            encore = 0
            Dire_aurevoir() 
        elif recommencer == 1:
            continue
    
    elif choix == 3:
        f = float(input("Entrez la fréquence de résonance (en Hz) : "))
        L = float(input("Entrez l'inductance (en Henrys) : "))
        C = 1 / (4 * pi**2 * f**2 * L)
        ZL = 2*pi * L * f  # Impédance de l'inductance
        ZC = 1 / (2 * pi * f * C)
        print("La capacité est de ", C,"F")
        print("L'impédance de l'inductance est ", ZL," Ohms")
        print("L'impédance de la capacité est, ", ZC," Ohms")
        recommencer = int(input("Voulez vous faire un autre calcul ? (1 pour oui, 0 pour non)"))
        if recommencer == 0:
            encore = 0
            Dire_aurevoir()
        elif recommencer == 1:
            continue
    
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
        
