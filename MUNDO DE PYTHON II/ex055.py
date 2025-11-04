maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input(f'Digite o peso da pessoa {i}: '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso foi {maior_peso:.1f}kg e o menor peso foi {menor_peso:.1f}kg.')