# -*- coding: utf-8 -*- 

import random
import os
os.system("clear")
titre = "Voici les prochains numéros gagnants de l'€uromillion !"
print(titre.center(100))

liste_numero = []
liste_numero_etoile = []
for i in range(1, 50):
    liste_numero.append(i)
for i in range(1, 11):
    liste_numero_etoile.append(i) 
numero1 = random.randint(1,49)



numero2 = random.randint(1,49)
if numero2 == numero1:
    numero2 = random.randint(1,49) 

numero3 = random.randint(1,49)
if numero3 == numero1 or numero3 == numero2:
    numero3 = random.randint(1,49)
numero4 = random.randint(1,49)
if numero4 == numero1 or numero4 == numero2 or numero4 == numero3:
    numero4 = random.randint(1,49)
numero5 = random.randint(1,49)
if numero5 == numero1 or numero5 == numero2 or numero5 == numero3 or numero5 == numero4:
    numero5 = random.randint(1,49)
liste_numero_sortie = [numero1, numero2, numero3, numero4, numero5]
sortie_Triée = sorted(liste_numero_sortie)

print("\033[0;32mVoici les numéros gagnants : \033[0m" + str (sortie_Triée[0]))
print("\033[0;32mVoici le deuxième numéro : \033[0m" + str (sortie_Triée[1]))
print("\033[0;32mVoici le troisième numéro : \033[0m" + str (sortie_Triée[2]))
print("\033[0;32mVoici le quatrième numéro : \033[0m" + str (sortie_Triée[3]))
print("\033[0;32mVoici le cinquième numéro : \033[0m" + str (sortie_Triée[4]))
etoile1 = random.randint(1,10)

etoile2 = random.randint(1,10)
liste_etoile_sortie = [etoile1, etoile2]
sortie_etoile_Triée = sorted(liste_etoile_sortie)
print("\033[0;35mVoici la première étoile : \033[0m" + str(sortie_etoile_Triée[0]))
if etoile2 == etoile1:
    etoile2 = random.randint(1,10)
print("\033[0;35mVoici la deuxième étoile : \033[0m" + str(sortie_etoile_Triée[1]))
