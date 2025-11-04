print('\033[1mE M P R E S T I M O   B A N C Á R I O')
nome = str(input('Digite o seu nome: ')).title().strip()
print('Use como guia o valor a seguir. \033[31mEx: R$1234.56\033[m')
salario = float(input('\033[1mDigite o seu salário: '))
disponivel = salario * 0.3
imovel = float(input('\033[1mQual o valor do imóvel: '))
QuantidadeParcela = int(input('Em quantas vezes você quer dividir: '))
ano = (QuantidadeParcela/12)
ValorParcelas = (imovel/QuantidadeParcela)
print('__'*30)
if disponivel >= ValorParcelas:
    print('Olá Sr {}, Seu Crédito para a compra de sua sonhada casa foi aprovado! 🎊🎊🎊'.format(nome))
    print('VALOR DA CASA: R$ {:.2f} \nVALOR DAS PARCELAS: {} X R${:.2f} \nMARGEM DISPONÍVEL PARA FINANCIAMENTO:'
          ' R${:.2f}'.format(imovel, QuantidadeParcela, ValorParcelas, disponivel))
    print('SEU SALÁRIO: R$ {:.2f}'.format(salario))
    print('SALÁRIO RESTANTE: R$ {:.2f}'.format(salario-ValorParcelas))
    print('O EMPRÉSTIMO SERÁ QUITADO EM {} ANOS'.format(ano))
else:
    print('Olá Sr {} é uma pena, mas seu empréstimo não foi aprovado 🥲'.format(nome))
    print('VALOR DA CASA: R${:.2f} \nSEU SALÁRIO: {:.2f} \nMARGEM DISPONÍVEL PARA FINANCIAMENTO: {:.2f}'
          .format(imovel, salario, disponivel))
    print('O VALOR DAS PARCELAS SERIA {} X {:.2f}'.format(QuantidadeParcela,ValorParcelas))