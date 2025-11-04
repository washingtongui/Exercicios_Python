#Código da cabeça do Washington
from random import choice
jogo = ['Pedra', 'Papel', 'Tesoura']
print('\033[1;33m{:^39}\033[m'.format('J O K E N P Ô'))
jogador = str(input('\033[1mEscolha entre:\033[m \033[1;32mPedra, Papel'
                    '\033[m \033[1mou\033[m \033[1;32mTesoura.\033[m '
                    '\n\033[1mSua escolha: \033[m')).title().strip()
if jogador  in jogo:
    computador = choice(jogo)
    print('\033[1mVocê escolheu: \033[1;32m{}\033[m \033[1me o Computador escolheu: \033[1;32m{}\033[m'
          .format(jogador, computador))
    if jogador == computador:
         print('EMPATE')
    elif jogador == 'Pedra' and computador == 'Tesoura':
         print('\033[1;33mJogador Ganhou\033[m')
    elif jogador == 'Papel' and computador == 'Pedra':
         print('\033[1;33mJogador Ganhou\033[m')
    elif jogador == 'Tesoura' and computador == 'Papel':
         print('\033[1;33mJogador Ganhou\033[m')
    else:
         print('\033[1;33mComputador Ganhou!\033[m')
else:
    print('\033[1;31mSUA ESCOLHA NÃO É VALIDA! \nVOLTE AO MENU INICIAL\033[m')