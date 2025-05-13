
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
            
            rejouer(recommencer)
        elif choix_calcul == 2:
            bc()
            rejouer(recommencer)
        elif choix_calcul == 3:
            ac()
            rejouer(recommencer)
        