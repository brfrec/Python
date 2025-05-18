import random

liste_numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
liste_numero_etoile = [1,2,3,4,5,6,7,8,9,10]
numero1 = random.randint(1,49)
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
