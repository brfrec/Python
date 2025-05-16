import random


listeUn = [" Chevreuil ", " Lapin ", " Souris ", " Zèbre "]
listeDeux = [" caline ", "baise", "suce", "encule", "doigte"]
aleatoire1 = random.randint(0,len(listeUn)-1)
aleatoire2 = random.randint(0,len(listeDeux)-1)
aleatoire3 = random.randint(0,len(listeUn)-1)
print(listeUn[aleatoire1] + listeDeux[aleatoire2] + listeUn[aleatoire3])


