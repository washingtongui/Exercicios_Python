print('\033[1;32mG E S T Ã O   D E   P R O D U T O S\033[m')
produto = str(input('\033[1mQUAL É O NOME DO PRODUTO: ')).upper().strip()
valor = float(input('QUAL É O VALOR DO PRODUTO: '))
pagamento = ['DINHEIRO OU CHEQUE', 'CARTÃO DE DÉBITO', 'CARTÃO DE CRÉDITO',
                   'DIVIDIDO EM 2X', 'DIVIDIDO EM 3X\033[m']
juros = valor * 0.2 + valor

opcao = int(input('\033[1;34mEscolha uma opção:\033[m \033[1;36m\n(0) → {} \n(1) → {} \n(2) → {} '
                  '\n(3) → {} \n(4) → {}\033[m \033[1;34m\nSua escolha: \033[m'
                  .format(pagamento[0], pagamento[1], pagamento[2], pagamento[3], pagamento[4])))
print('\033[31m─────────\033[m'*4)
if opcao == 0:
    print('\033[1;4;32m{}\033[m'.format(pagamento[0]))
    print('\033[1mNOME DO PRODUTO: {} \nVALOR DO PRODUTO: R$ {:.2f}'.format(produto,valor))
    print('DESCONTO DE\033[m \033[1;4;31m10%\033[m \033[1m{}'.format(pagamento[0]))
    print('VALOR À PAGAR COM DESCONTO: R$ {:.2f}\033[m'.format(valor - valor * 0.1))
elif opcao == 1 or opcao == 2:
    print('\033[1;4;32m{} ou {}\033[m'.format(pagamento[1], pagamento[2]))
    print('\033[1mNOME DO PRODUTO: {} \nVALOR DO PRODUTO: R$ {:.2f}'.format(produto, valor))
    print('DESCONTO DE\033[m \033[1;4;31m5%\033[m \033[1mNO {} \n{:^53} \n{:^54}'.format(pagamento[1],'ou', pagamento[2]))
    print('VALOR À PAGAR  COM DESCONTO: R$ {:.2f}\033[m'.format(valor - (valor * 0.05)))
elif opcao == 3:
    print('\033[1;4;32m{} NO CARTÃO\033[m'.format(pagamento[3]))
    print('\033[1mNOME DO PRODUTO: {} \n\033[1;4;31m20%\033[m DE JUROS: R$ {:.2f}'.format(produto, juros))
    print('{} NO CARTÃO\033[m \n\033[1;31m1° PARCELA R$ {:.2f} \n2° PARCELA R$ {:.2f}\033[m'
          .format(pagamento[3], juros/2 , juros/2))
elif opcao == 4:
    print('\033[1;4;32m{} NO CARTÃO\033[m'.format(pagamento[4]))
    print('\033[1mNOME DO PRODUTO: {} \n\033[1;4;31m20%\033[m DE JUROS: R${:.2f}'.format(produto, juros))
    print('{} NO CARTÃO\033[m \n\033[1;31m1° PARCELA R$ {:.2f} \n2° PARCELA R$ {:.2f} ' 
          '\n3° PARCELA R$ {:.2f}\033[m'.format(pagamento[4],(valor*0.2+valor)/3,
                                                juros/3, juros/3))
else:
    print('\033[1;31mERRO! \nVOLTE AO MENU! \nVOCÊ NÃO ESCOLHEU NENHUMA DAS OPÇÕES!\033[m')
print('\033[31m─────────\033[m'*4)