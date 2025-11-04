print('\033[1;34mUSE\033[m \033[1;31mPONTO(.)\033[m \033[1;34mE NÃO\033[m \033[1;31mVÍRGULA(,) \033[m')
peso = float(input('Qual é o seu peso em (KG): '))
altura = float(input('Qual é sua altura em (METROS): '))
imc = peso / (altura**2)
print('SEU IMC É {:.1f}'.format( imc))
if imc < 18.5:
    print('\033[1;31mVocê está abaixo do peso!!!\033[m')
elif 18.5 <= imc < 25:
    print('\033[1;32mVocê está com o peso ideal!!!')
elif 25 <= imc < 30:
    print('\033[1;31mVocê está com sobrepeso!!!!!!!!!!\033[m')
elif 30 <= imc < 40:
    print('\033[1;31mObesidade!!!\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA!\033[m')