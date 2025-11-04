print('------------------------------------------')
print('F I R M A  D O S   B A T E   M A S S A KKK')
print('------------------------------------------')
print('')
Funcio = str(input('Qual é o seu nome: '))
print('')
sal = float(input('Qual o seu salário: '))
#Lembre sempre de usar o ponto e não a vírgula.
#Pois e o sistema de medida dos Eua e não Br
aumento = sal + (sal * 0.15)
print('Bom o Sr {} Ganhou um aumento de 15% merecidos \nno seu salário,'
      'que antes sendo {:.2f} R$ \npassa a ser {:.2f} R$. Meus parabéns!'
      ' '.format(Funcio, sal, aumento))