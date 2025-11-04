numero = 0
somador = 0
contador = 0
while numero != 999:
    numero = int(input('Digite um número inteiro: '))
    if numero != 999:
        contador += 1
        somador += numero
        print(somador)
print('Foram digitados {} números'.format(contador))
print('Resultado de todos os números: {}'.format(somador))