valor1 = int(input('Digite o primeiro valor: '))
valor2: int = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
maior_valor = valor1
menor_valor = valor1
if valor2 > maior_valor and valor2 > valor3:
    maior_valor = valor2
if valor3 > maior_valor and valor3 > valor2:
    maior_valor = valor3
print(maior_valor)
print('Qual é o menor número? ')
if valor2 < menor_valor and valor2 < valor3:
    menor_valor = valor2
if valor3 < valor2 and valor3 < menor_valor:
    menor_valor = valor3
print(menor_valor)