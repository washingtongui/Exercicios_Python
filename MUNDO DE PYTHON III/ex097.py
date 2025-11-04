def msg(txt):
     print(f'{"\033[1;33m-=\033[m"*len(txt)}')
     print(txt.center(len(txt)*2))
     print(f'{"\033[1;33m-=\033[m"*len(txt)}')


while True:
    msg(str(input('Digite qualquer coisa: ')))
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('\033[1;31mDigite apenas S ou N\033[m')
    if resp == 'N':
        break