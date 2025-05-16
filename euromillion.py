import random

liste_numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
liste_numero_etoile = [1,2,3,4,5,6,7,8,9,10]
numero1 = random.randint(1,49)
print("Voici le premier numéro : " + str(numero1))
numero2 = random.randint(1,49)
while numero2 == numero1:
    numero2 = random.randint(1,49) 
print("Voici le deuxième numéro : " + str(numero2))
numero3 = random.randint(1,49)
while numero3 == numero1 or numero3 == numero2:
    numero3 = random.randint(1,49)
print("Voici le troisième numéro : " + str(numero3))
numero4 = random.randint(1,49)
while numero4 == numero1 or numero4 == numero2 or numero4 == numero3:
    numero4 = random.randint(1,49)
numero5 = random.randint(1,49)
print("Voici le quatrième numéro : " + str(numero4))
while numero5 == numero1 or numero5 == numero2 or numero5 == numero3 or numero5 == numero4:
    numero5 = random.randint(1,49)
print("Voici le cinquième numéro : " + str(numero5))

etoile1 = random.randint(1,10)
print("Voici la première étoile : " + str(etoile1))
etoile2 = random.randint(1,10)
while etoile2 == etoile1:
    etoile2 = random.randint(1,10)
print("Voici la deuxième étoile : " + str(etoile2))
