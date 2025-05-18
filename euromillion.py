import random


liste_numero = []
liste_numero_etoile = []
for i in range(1, 50):
    liste_numero.append(i)
for i in range(1, 11):
    liste_numero_etoile.append(i) 
numero1 = random.randint(1,49)
print(liste_numero)
print("\033[0;32m Voici le premier numéro : \033[0m" + str(numero1))
numero2 = random.randint(1,49)
while numero2 == numero1:
    numero2 = random.randint(1,49) 
print("\033[0;32mVoici le deuxième numéro : \033[0m" + str(numero2))
numero3 = random.randint(1,49)
while numero3 == numero1 or numero3 == numero2:
    numero3 = random.randint(1,49)
print("\033[0;32mVoici le troisième numéro : \033[0m" + str(numero3))
numero4 = random.randint(1,49)
while numero4 == numero1 or numero4 == numero2 or numero4 == numero3:
    numero4 = random.randint(1,49)
numero5 = random.randint(1,49)
print("\033[0;32mVoici le quatrième numéro : \033[0m" + str(numero4))
while numero5 == numero1 or numero5 == numero2 or numero5 == numero3 or numero5 == numero4:
    numero5 = random.randint(1,49)
print("\033[0;32mVoici le cinquième numéro : \033[0m" + str(numero5))

etoile1 = random.randint(1,10)
print("\033[0;35mVoici la première étoile : \033[0m" + str(etoile1))
etoile2 = random.randint(1,10)
while etoile2 == etoile1:
    etoile2 = random.randint(1,10)
print("\033[0;35mVoici la deuxième étoile : \033[0m" + str(etoile2))
