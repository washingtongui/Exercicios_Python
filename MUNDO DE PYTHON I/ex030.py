numero = int(input('Digite um número: '))
imparOUpar = numero % 2
if imparOUpar == 1:
    print('{} É um número impar'.format(numero))
else:
    print(f'{numero} É um número Par')