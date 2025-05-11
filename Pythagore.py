from math import *
from FonctionPythagore import *

print (" ... PYTHAGORE ... ")
print ("Ce petit programme calcule la longueur d'un coté d'un triangle rectangle en fonction de la longueur de ses deux autres cotés")
print ("ou la valeur de ses angles en degrés")
print ("Soit un triangle ABC rectangle en B")
longueurOuAngle = int(input("1 - Calcul d'une longeur\n2 - Calcul d'un angle\nVotre choix : "))
if longueurOuAngle == 1:
    choix_calcul = int(input("Quelle longueur voulez vous calculer ?:\n1 - AB\n2 - BC\n3 - AC (hypothènuse)\nVotre choix :"))
    if choix_calcul == 1:
        ab()
    elif choix_calcul == 2:
        bc()
    elif choix_calcul == 3:
        ac()
    else:
        print("Ce choix n'est pas proposé")
 
elif longueurOuAngle == 2:
    print ("en construction")
