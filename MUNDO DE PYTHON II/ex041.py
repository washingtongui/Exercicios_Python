from datetime import datetime
print('C A T E G O R I A S')
ano = int(input('Qual é o seu ano de nascimento: '))
idade = datetime.now().year - ano
print('CATEGORIA: ')
if idade <= 9:
    print('MIRIM')
    print('SUA IDADE É {}'.format(idade))
elif 9 < idade <= 14:
    print('INFANTIL')
    print('SUA IDADE É {}'.format(idade))
elif 14 < idade <= 19:
    print('JUNIOR')
    print('SUA IDADE É {}'.format(idade))
elif idade == 20:
    print('SÊNIOR')
    print('SUA IDADE É {}'.format(idade))
else:
    print('MASTER')
    print('SUA IDADE É {}'.format(idade))