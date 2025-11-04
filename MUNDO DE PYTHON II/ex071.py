saque = int(input('Digite o valor de saque: '))
resto_50 = saque % 50
resto_20 = resto_50 % 20
resto_10 = resto_20 % 10
resto_01 = resto_10 % 1

notas_50 = saque // 50
notas_20 = resto_50 // 20
notas_10 = resto_20 // 10
notas_01 = resto_10 // 1


print('-='*10)

if notas_50 >= 1:
    print(f'{notas_50} notas de 50,00')
if notas_20 >= 1:
    print(f'{notas_20} notas de 20,00')
if notas_10 >= 1:
    print(f'{notas_10} notas de 10,00')
if notas_01 >= 1:
    print(f'{notas_01} notas de 1,00')