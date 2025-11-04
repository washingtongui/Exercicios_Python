print('F I R M A  D O S  L A S C A D O S ')
funcionario = str(input('Qual é o seu nome:'))
Salario = float(input('Qual é o seu salário: '))
if Salario > 1250:
    print('Nós da FIRMA DOS LASCADOS te parabenizamos \ncom um aumento de 10%.')
    print('Olá, {} seu novo salário será de {:.2f}'.format(funcionario, Salario+(Salario*0.1)))
    print(f'Um aumento de {Salario*0.1:.2f} aumento merecido.')
else:
    print('Nós da FIRMA DOS LASCADOS te parabenizamos \ncom um aumento de 15%.')
    print('Olá, {} seu novo salário será de {:.2f}'.format(funcionario, Salario + (Salario * 0.15)))
    print(f'Um aumento de {Salario * 0.15   :.2f} aumento merecido.')