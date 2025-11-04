from datetime import datetime
print('ALISTAMENTO MILITAR')
nome = str(input('Digite seu nome: ')).title().strip()
ano = int(input('Em que ano você nasceu ?'))
ano_atual = datetime.now().year
idade = ano_atual-ano
if idade == 18:
    print('APRESENTAÇÃO PARA ALISTAMENTO MILITAR!')
    print('Neste ano sr {} Já completou ou completará seus 18.'.format(nome))
    print('Deverá realizar o alistamento via site.')
elif idade < 18:
    print('Olá Sr {} Seja bem vindo, vamos ver sua situação! '.format(nome))
    print('Você tem apenas {} de idade não pode se alistar.'.format(idade))
    print('Porém faltam {} anos para você ter seus 18 anos de idade.'.format(18-idade))
    print('Esperamos ansioso por você, Brasil acima de tudo e Deus acima de todos.')
else:
  print('Olá Sr {} após verificação você ainda não se alistou.'.format(nome))
  print('Seu alistamento deveria ter sido feita no ano de {} a {} atrás.'.format(ano+18, idade-18))
  print('Com a maioridade e sem reservista você fica impossibilitado de muitas coisas.')
  print('Procure o quartel mais próximo e regularise sua situação.')