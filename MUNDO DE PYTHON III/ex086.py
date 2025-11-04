matriz = [[], [], []]

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
print('-='*20)
print(f'[  {matriz[0][0]}  ] [  {matriz[0][1]}  ] [  {matriz[0][2]}  ]')
print(f'[  {matriz[1][0]}  ] [  {matriz[1][1]}  ] [  {matriz[1][2]}  ]')
print(f'[  {matriz[2][0]}  ] [  {matriz[2][1]}  ] [  {matriz[2][2]}  ]')