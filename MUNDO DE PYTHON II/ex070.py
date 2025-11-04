total_gasto = mais_de_mil = 0
soma_tudo = 0

produto = str(input('Digite o nome do produto: '))
preco = float(input('Digite o preço do produto: '))
mais_barato = preco
nome_mais_barato = produto
while True:
    resposta = ' '
    soma_tudo += preco
    if preco > 1000:
        mais_de_mil += 1
    elif preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = produto
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resposta == 'S':
        produto = str(input('Digite o nome do produto: '))
        preco = float(input('Digite o preço do produto: '))
    elif resposta == 'N':
        break

print(f'Gastos totais R$: {soma_tudo:.2f}')
print(f'Produtos com valores superiores a um mil: {mais_de_mil:.0f}')
print(f'O {nome_mais_barato} é o produto mais barato valor R$: {mais_barato:.2f} ')