resposta = 0
while resposta not in ['5']:
    print('\033[33m-=\033[m'*13)
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    resposta = str(input('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR \n'))
    if resposta in ['1']:
        print('SOMA')
        print('{} + {} = {}'.format(valor1, valor2, valor1+valor2))
    elif resposta in ['2']:
        print('MULTIPLICADOR')
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
    elif resposta in ['3']:
        if valor1 > valor2:
            print('{} é maior que {}'.format(valor1, valor2))
        else:
            print('{} é maior que {}'.format(valor2, valor1))
    elif resposta in ['6', '7', '8', '9', '0']:
        print('\033[1;31mVocê não escolheu nenhuma das opções!\033[m')