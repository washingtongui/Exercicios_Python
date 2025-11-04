from  random import randint
from time import sleep
palpites = []
copiador = []
contador = 0
quantidade = int(input('Quantos palpites você quer gerar: '))
for l in range(0, quantidade):
    while len(copiador) < 6:
        numero = randint(1, 60)
        if numero not in copiador:
            copiador.append(numero)
    palpites.append(copiador[:])
    copiador.clear()
for valores in palpites:
    contador += 1
    print(f'jogo {contador}° = {valores}')
    sleep(0.9)

