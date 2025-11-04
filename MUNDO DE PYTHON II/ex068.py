from random import randint
contador = 0
while True:
    print('\033[1;34m⚀⚁⚂⚃⚄⚅\033[m'*4)
    print(f'\033[1m{'VAMOS JOGAR PAR OU IMPAR':^30}\033[m')
    print('\033[1;34m⚀⚁⚂⚃⚄⚅\033[m'*4)
    print('\033[1;31mOBS:\033[m \033[1mCASO QUEIRA DIGITE: I ou P\033[m')
    escolha = ' '
    while escolha not in 'IP':
        escolha = str(input('\033[1mESCOLHA IMPAR OU PAR: \033[m')).upper().strip()[0]
    if escolha in ['I', 'P']:
        usuario = int(input('\033[1mDIGITE UM NÚMERO: \033[m'))
        print('\033[1;33m-=\033[m'*12)
        computador = randint(0, 10)
        somador = computador + usuario
        print(f'\033[1mESCOLHA DO USUÁRIO: {usuario} \nESCOLHA DO COMPUTADOR: {computador}'
              f'\nSOMA DAS ESCOLHAS = {somador}\033[m')
        print('\033[1;33m-=\033[m'*12)
        if escolha == 'I' and somador % 2 ==1:
            print(f'\033[1mO NÚMERO {somador} É IMPAR E VOCÊ GANHOU 🏆\033[m')
            contador += 1
        elif escolha == 'P' and somador % 2 == 0:
            print(f'\033[1mO NÚMERO {somador} É PAR E VOCÊ GANHOU 🏆\033[m')
            contador += 1
        else:
            print('\033[1;31mCOMPUTADOR GANHOU! 🏆\033[m')
            break

        print('\033[1;33m-=\033[m'*12)
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
print(f'Você ganhou {contador} vezes 🥇')