from math import *

print (" ... PYTHAGORE ... ")
print ("Ce petit programme calcule la longueur d'un coté du'un triangle rectangle en fonction de la longueur de ses deux autres cotés")
print ("Soit un triangle ABC rectangle en B")
choix_calcul = int(input("Quelle longueur voulez vous calculer ?:\n1 - AB\n2 - BC\n3 - AC (hypothènuse)\nVotre choix :"))
if choix_calcul == 1:
    BC = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    AB = sqrt((AC**2)-(BC**2))
    print ("La longueur de AB vaut", AB)

elif choix_calcul == 2:
    AB = int(input("Longueur de BC : "))
    AC = int(input("Longueur de AC (hypothénuse): "))
    BC = sqrt((AC**2)-(AB**2))
    print ("La longueur de BC vaut", BC)

elif choix_calcul == 3:
    AB = int(input("Longueur de AB : "))
    BC = int(input("Longueur de BC : "))
    AC = sqrt((AB**2)+(BC**2))
    print ("La longueur de AC vaut", AC)

else:
    print("Ce choix n'est pas proposé")