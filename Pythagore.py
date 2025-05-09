from math import *
from Fonction import *

print (" ... PYTHAGORE ... ")
print ("Ce petit programme calcule la longueur d'un coté du'un triangle rectangle en fonction de la longueur de ses deux autres cotés")
print ("Soit un triangle ABC rectangle en B")
choix_calcul = int(input("Quelle longueur voulez vous calculer ?:\n1 - AB\n2 - BC\n3 - AC (hypothènuse)\nVotre choix :"))
if choix_calcul == 1:
    ab()

elif choix_calcul == 2:
    bc()

elif choix_calcul == 3:
    ac()

else:
    print("Ce choix n'est pas proposé")