cores = {
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',
    'negrito': '\033[1m',
    'reset': '\033[m'
}

jogador = dict()
lista_gols = []
total_gols = 0

jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
partidas = int(input('Quantas partidas jogadas: '))

for i in range(0, partidas):
    gols_partidas = int(input(f' Quantos gols na {i+1}° partida: '))
    total_gols += gols_partidas
    lista_gols.append(gols_partidas)

jogador['gols'] = lista_gols[:]
jogador['total'] = total_gols

print(f'{cores['amarelo']}-={cores['reset']}'*30)
print(f'{cores['amarelo']}{'DADOS DO JOGADOR':^60}{cores['reset']}')
print(jogador)
print(f'{cores['amarelo']}-={cores['reset']}'*30)

print(f'O nome do jogador é: {jogador['nome']}')
print(f'Os gols feitos por partidas foras: {jogador['gols']}')
print(f'O total de gols foi: {jogador['total']}')
print(f'{cores['amarelo']}-={cores['reset']}'*30)

print(f'O jogador {jogador['nome']} jogou {partidas}')
for i in range(0, partidas):
    print(f' {i+1}° Partida : {jogador['gols'][i]}')
print(f'Foi um total de {total_gols} Gols')