sexo = 'F'
contador = 0
while sexo in ['F', 'M']:
    sexo = str(input('Qual é o seu sexo [F/M]:  ')).upper().strip()
    contador += 1
print('{}° escolha: {}'.format(contador, sexo))
print('\033[1;31mVocê não escolheu entre F e M\033[m')