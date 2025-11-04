numero = int(input('Digite um número: '))
imparOUpar = numero % 2
print('{} É Impar'.format(numero) if imparOUpar == 1 else '{} É Par'.format(numero))
#Ou se eu quisesse facilidade ao invés de seguir o curso.
print(f'{numero} É Impar' if imparOUpar == 1 else f'{numero} É Par.')
