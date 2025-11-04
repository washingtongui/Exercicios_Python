from math import trunc
print('Digite um número para ver sua parte inteira')
numero = float(input('Digite um nùmero: '))
print('A parte inteira de {:.2f} é {} '.format(numero, trunc(numero)))