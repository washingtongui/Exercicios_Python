from random import randint
numero_usuario = int(input('Digite um número: '))
numero_aleatorio = randint(0,5)
if numero_usuario == numero_aleatorio:
    print('Uau, parabéns você é bom de palpite!')
    print('O número escolhido por você foi {}'.format(numero_usuario))
    print('O número Escolhido pelo pc é {}'.format(numero_aleatorio))
else:
    print('É uma pena você não acertou!!!')
    print('Você escolheu {}'.format(numero_usuario))
    print('O PC escolheu {}'.format(numero_aleatorio))