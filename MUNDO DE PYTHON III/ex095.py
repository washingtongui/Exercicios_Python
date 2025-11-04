todos_jogadores = list()
jogador = dict()
lista_gols = list()
contador = 0
while True:
    jogador.clear()
    lista_gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    partidas = int(input('Quantas partidas jogadas: '))
    for i in range(0, partidas):
        gols_partidas = int(input(f' Quantos gols na {i+1}° partida: '))
        lista_gols.append(gols_partidas)
    jogador['gols'] = lista_gols[:]
    jogador['total'] = sum(lista_gols)
    todos_jogadores.append(jogador.copy())
    while True:
        decisao = str(input('Cadastra mais um jogador: [S/N]')).strip().upper()
        if decisao in 'SN':
            break
        print('\033[1;31mEscolha entre S ou N\033[m')
    if decisao == 'N':
        break
print(decisao)

print('\033[1;33m=-\033[m'*40)
print(f'    {"cod      |":^20}{"Nome      |":^20}{"Gols      |":^20}{"Total   ":^20}')
print('\033[1m-\033[m'*80)
for dicionario in todos_jogadores:
    print(f'{str(contador).center(20)}{dicionario["nome"]:^20}'
          f'{str(dicionario["gols"]).ljust(20)}{str(dicionario["total"]).center(20)}')
    contador += 1
print('\033[1;33m=-\033[m' * 40)
while True:
    while True:
        decisao = str(input('Deseja ver Analise de um Jogador?')).upper().strip()
        if decisao in 'SN':
            break
        print('Digite S ou N')
    if decisao == 'N':
        break
    while True:
        escolha = int(input('Deseja analisar a performance de qual jogador? '))
        if escolha < len(todos_jogadores):
            break
        else:
            print(f'Escolha entre 0 e {len(todos_jogadores)-1}')


    print(f'Estatística do jogador {todos_jogadores[escolha]["nome"]}:')
    for i in range(0, len(todos_jogadores[escolha]['gols'])):
        print(f'Na {i+1}° partida fez: {todos_jogadores[escolha]["gols"][i]} Gols')