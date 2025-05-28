from math import *
from Fonction import *


def calculResistance():
    print("Calcul de la résistance")
    try:
        C = float(input("Entrez la valeur du condensateur en µF: "))
        Tau5 = float(input("Entrez le temps de charge/décharge 5 tau : "))
        Tau = Tau5 / 5  # Calcul de Tau à partir de 5 Tau
        print("Tau = ", Tau, "s")
        R = ceil((Tau/5) / (C * 1e-6))  # Conversion de µF à F
        if R < 1:
            R = R * 1000
            print("La valeur de la résistance est :",R," mHoms")
        elif R > 1 and R < 1000:
            print("La valeur de la résistance est :", R, " Ohms")
        elif R > 1000 and R < 1000000:
            R = R / 1000
            print("La valeur de la résistance est :", R, " KOhms")  
        elif R > 1000000 and R < 1000000000:
            R = R / 1000000
            print("La valeur de la résistance est :", R, " MOhms")      
        
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")   
    
def calculCondensateur():
    print("Calcul du condensateur")
    
    try:
        R = float(input("Entrez la valeur de la résistance : "))
        Tau5 = float(input("Entrez le temps de charge/décharge 5 tau : "))
        Tau = Tau5 / 5  # Calcul de Tau à partir de 5 Tau
        print("Tau = ", Tau, "s")
    except: print("Erreur : Veuillez entrer une valeur numérique valide pour la résistance.")   
    C = Tau / R
    if C < 1e-6:
        C = C * 1e9
        print("La valeur du condensateur est :",ceil(C) , "nF")
    elif C >= 1e-6 and C < 1:
        C = C * 1e6
        print("La valeur du condensateur est :",ceil(C) , "µF")
        
def calculTau():
    print("Calcul du temps de charge/décharge (Tau)")

    try:
        R = float(input("Entrez la valeur de la résistance : "))
        C = float(input("Entrez la valeur du condensateur en µF : "))
        Tau = R * (C* 1e-6)  # Conversion de µF à F
        if Tau < 1e-3:
            Tau = ceil(Tau * 1e6)
            print("Tau = ",Tau,"µs\n3 Tau = ", Tau * 3, "µs\n5 Tau = ", Tau * 5, "µs")
        elif Tau >= 1e-3 and Tau < 1:
            Tau = Tau * 1e3
            print("Tau = ",Tau,"ms\n3 Tau = ", Tau * 3, "ms\n5 Tau = ", Tau * 5, "ms")
        else:
            print("Tau = ",Tau,"s\n3 Tau = ", ceil(Tau * 3), "s\n5 Tau = ", ceil(Tau * 5), "s")
                
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")


