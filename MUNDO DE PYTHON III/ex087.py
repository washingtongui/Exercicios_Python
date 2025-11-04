matriz = [[], [], []]
soma_pares = 0
soma_coluna3 = 0
for posicao, numero in enumerate(matriz):
    if posicao == 0:
        for posicao_0, numero_0 in enumerate(matriz):
            matriz[0].append(int(input(f'Digite um valor para {[posicao, posicao_0]}: ')))
    elif posicao == 1:
        for posicao_1, numero_1 in enumerate(matriz):
            matriz[1].append(int(input(f'Digite um valor para {[posicao, posicao_1]}: ')))
    else:
        for  posicao_2, numero_2 in enumerate(matriz):
            matriz[2].append(int(input(f'Digite um valor para {[posicao, posicao_2]}: ')))
for i in range(3):
    for elemento in matriz[i]:
        if elemento % 2 == 0:
            soma_pares += elemento
        if elemento == matriz[i][2]:
            soma_coluna3 += elemento
        print(f'[  {elemento}  ]', end=' ')
        if elemento == matriz[i][2]:
            print()
print(f'A soma dos núemros pares é {soma_pares}')
print(f'A soma da teceria coluna é {soma_coluna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')