from random import randint
numero_usuario = 0
numero_computador = 1
contador = 0
while numero_usuario != numero_computador:
    numero_usuario = int(input('\033[1;32mDigite um numero: \033[m'))
    numero_computador = randint(0   ,10)
    contador += 1
    if numero_usuario != numero_computador:
        print('Computador escolheu {} e você {}, você não acertou'.format(numero_computador, numero_usuario))
    else:
        print('Computador escolheu {} e você {}'.format(numero_computador, numero_usuario))
        print('Você acertou na {}° tentativa. Belo palpite!'.format(contador, numero_usuario))