n1 = int(input('Digite 1° número: '))
n2 = int(input('Digite 2° número: '))
n3 = int(input('Digite 3° número: '))
n4 = int(input('Digite 4° número: '))
numeros = (n1, n2, n3, n4)
print(numeros)
print(f'O valor 9 apareceu {numeros.count(9)}X na tela')
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')
