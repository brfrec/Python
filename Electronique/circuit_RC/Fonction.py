
def Explication():
    print("Bienvenue dans le programme de calcul de circuits RC.")
    print("Ce programme vous permettra de calculer la valeur d'une résistance, d'un condensateur ou le temps de charge/décharge (Tau) d'un circuit RC.")
    print("Veuillez suivre les instructions pour entrer les valeurs nécessaires.")
    print("\n")  # Ajout d'une ligne vide pour une meilleure lisibilité


#def ConversionUnite():


def calculResistance():
    print("Calcul de la résistance")

    try:
        C = float(input("Entrez la valeur du condensateur : "))
        Tau = float(input("Entrez le temps de charge/décharge (Tau) : "))
        R = Tau / C
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
    





