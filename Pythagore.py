
from math import *
from FonctionPythagore import *

recommencer = 1
while recommencer:

    print (" ... PYTHAGORE ... ")
    print ("Ce petit programme calcule la longueur d'un coté d'un triangle rectangle en fonction de la longueur de ses deux autres cotés")
    print ("Soit un triangle ABC rectangle en B")
    try:
        choix_calcul = int(input("Quelle longueur voulez vous calculer ?:\n1 - AB\n2 - BC\n3 - AC (hypothènuse)\nVotre choix :"))
    except:
        print ("Valeur invalide !")
    else:
        if choix_calcul == 1:
            ab()
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

        elif choix_calcul == 2:
            bc()

        elif choix_calcul == 3:
            ac()

        else:
            print("Ce choix n'est pas proposé")