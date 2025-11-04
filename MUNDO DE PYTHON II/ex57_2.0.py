sexo = str(input('Qual é o seu sexo [M/F]')).strip().upper()[0]
while sexo not in ['F', 'M']:
    sexo = str(input('\033[1;31mOpção invalida!\033[m Qual é o seu sexo [M/F]')).strip().upper()[0]
print('\033[1;32mSexo {} digitado com sucesso...\033[m'.format(sexo))
