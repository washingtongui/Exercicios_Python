print('\033[1;36mESCOLA CAVALO AMANCO\033[m')
nota1 = float(input('\033[34mDigite sua primeira nota: \033[m'))
nota2 = float(input('\033[34mDigite sua segunda nota: \033[m'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\033[1;31mVocê foi reprovado, sua média é {:.1f}\033[m'.format(media))
elif 5.0 < media <6.9:
    print('\033[1;33mVocê está de recuperação sua média é {:.1f}\033[m'.format(media))
else:
    print('\033[1;32mParabéns você foi aprovado é sua média é {:.1f}'.format(media))