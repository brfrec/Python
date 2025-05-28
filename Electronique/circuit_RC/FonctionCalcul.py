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
    
def calculCondensateur():
    print("Calcul du condensateur")

    try:
        R = float(input("Entrez la valeur de la résistance : "))
        Tau = float(input("Entrez le temps de charge/décharge (Tau) : "))
        C = Tau / R
        if C < 1e-6:
            C = C * 1e9
            print("La valeur du condensateur est :", C, "nF")
        elif C >= 1e-6 and C < 1e-3:
            C = C * 1e6
            print("La valeur du condensateur est :", C, "µF")
        elif C >= 1e-3 and C < 1:
            print("La valeur du condensateur est :", C, "mF")
                
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")

def calculTau():
    print("Calcul du temps de charge/décharge (Tau)")

    try:
        R = float(input("Entrez la valeur de la résistance : "))
        C = float(input("Entrez la valeur du condensateur : "))
        Tau = R * C
        if Tau < 1e-3:
            Tau = Tau * 1e6
            print("Le temps de charge/décharge (Tau) est :", Tau, "µs")
        elif Tau >= 1e-3 and Tau < 1:
            Tau = Tau * 1e3
            print("Le temps de charge/décharge (Tau) est :", Tau, "ms")
        else:
            print("Le temps de charge/décharge (Tau) est :", Tau, "s")
                
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")

        
