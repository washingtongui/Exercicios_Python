#ANO BISSEXTO
from datetime import date
ano = int(input('Digite o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano de {} é bissexto'.format(ano))
        else:
            print('{} Não é um ano bissexto'.format(ano))
    else:
        print('O ano de {} é bissexto'.format(ano))
else:
    print('{} Não é um ano bissexto'.format(ano))