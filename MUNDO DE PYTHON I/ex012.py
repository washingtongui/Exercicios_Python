print('S U P E R M E R C A D O   T O M')
print('')
Fruta = str(input('Qual é o nome da Fruta: '))
print('')
Valor = float(input('Digite o valor da fruta para ser aplicado os 5% de desconto: '))
Descon =  Valor - (0.05*Valor)
print('')
print('{} é uma fruta deliciosa, o valor dela é: {:.2f} R$, \nMas como hoje é o dia das promoções'
      ' \ne estamos com um desconto de 5% ela está: {:.2f} R$ '.format(Fruta, Valor, Descon))