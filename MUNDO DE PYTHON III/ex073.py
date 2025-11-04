Tabela_brasileira =(
    'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Bahia',
    'Botafogo', 'São Paulo', 'Bragantino', 'Corinthians', 'Fluminense',
    'Ceará SC', 'Internacional', 'Atlético-MG','Grêmio','Vasco da Gama',
    'Santos', 'EC Vitória', 'Juventude', 'Fortaleza', 'Sport Recife'
)
print('\033[1;34m-=\033[m'*21)
print('\033[1;33mT A B E L A   D O   B R A S I L E I R Ã O\033[m')
print('')
print(f'\033[1;33m{2025:^40}\033[m')
print('\033[1;32m-=\033[m'*21)

contador = 0
print('\033[1mOs cinco primeiros colocados\033[m')
for primeiros_colocados in Tabela_brasileira[0:5]:
    contador += 1
    print(f'\033[1;32m{contador}° {primeiros_colocados}\033[m')

contador = 16
print('\033[1mOs quatro ultimos colocados\033[m')
for ultimos_colocados in Tabela_brasileira[16:20]:
    contador += 1
    print(f'\033[1;31m{contador}° {ultimos_colocados}\033[m')

print('\033[1mTimes em ordem alfabética.\033[m')
for ordem_alfabetica in sorted(Tabela_brasileira):
    print(f'\033[1;31m{ordem_alfabetica[:1]}\033[m{ordem_alfabetica[1:]}')

print('\033[1mEm qual posição na tabela está EC Vitória na tabela: \033[m')
print(f'O EC Vitória está na {Tabela_brasileira.index('EC Vitória') + 1}° da tabela')