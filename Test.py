import random


listeUn = [" Chevreuil ", " Lapin ", " Souris ", " Zèbre ", " Renard ", " Chien ", " Coq "]
listeDeux = [" caline ", "baise", "suce", "encule", "doigte", "caresse", "enfile", "gicle sur"]
aleatoire1 = random.randint(0,len(listeUn)-1)
aleatoire2 = random.randint(0,len(listeDeux)-1)
aleatoire3 = random.randint(0,len(listeUn)-1)
print(listeUn[aleatoire1] + listeDeux[aleatoire2] + listeUn[aleatoire3])


