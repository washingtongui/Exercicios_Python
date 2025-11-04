print('COMPARAÇÃO DE NÚMEROS')
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print(' \033[1;31m{}\033[m é maior que \033[1;32m{}\033[m'.format(numero1, numero2))
elif numero2 > numero1:
    print(' \033[1;31m{}\033[m é maior que \033[1;32m{}\033[m'.format(numero2, numero1))
else:
    print('\033[1;33mOs números são idênticos\033[m')