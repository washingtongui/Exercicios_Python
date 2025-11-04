print('-'*22)
print('  RADAR DE VELOCIDADE  ')
print('-'*22)
velocimetro = float(input('Em qual velocidade o veiculo passou no radar: '))
print('-'*22)
print('{:.1f} KM/H'.format(velocimetro))
print('-'*22)
if velocimetro >= 88.0:
    print('O radar era de 80 com tolerância de 10%')
    print('Você ultrapassou os 88 KM/H e a Multa é: 7,00 o KM')
    print('Multa: R$ {:.2f}'.format((velocimetro - 88)*7))
else:
    print('Sua velocidade é {} KM/H Parabéns.'.format(velocimetro))
    print('A segurança no trânsito é essencial para salvar vidas, \nreduzir lesões e preservar a qualidade de vida das pessoas')