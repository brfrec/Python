import random
import os
os.system("clear")

listeUn = [" La hyène "," Le chevreuil ", " Le lapin ", " La souris ", " Le zèbre ", " Le renard ", " Le chien ", " Le coq "]
listeDeux = ["pisse sur","chie sur","se fait prendre le fifi par","baise", "suce", "encule", "doigte", "fais mousser", "enfile", "gicle sur"]
aleatoire1 = random.randint(0,len(listeUn)-1)
aleatoire2 = random.randint(0,len(listeDeux)-1)
aleatoire3 = random.randint(0,len(listeUn)-1)
if aleatoire1 == aleatoire3:
    aleatoire3 = random.randint(0,len(listeUn)-1)

print(listeUn[aleatoire1] + listeDeux[aleatoire2] + listeUn[aleatoire3])


