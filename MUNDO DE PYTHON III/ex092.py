print('\033[1;33mI N S S   D O   C A P I R O T O\033[m')
from datetime import date
dados = dict()
dados['nome'] = str(input('Digite seu nome: ')).capitalize().strip()
ano_nasc = int(input('Digite seu Ano de nascimento: '))
dados['idade'] = date.today().year - ano_nasc

dados['ctps'] = int(input('Carteira de trabalho (0 Não tem): '))
if dados['ctps'] > 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Digite seu salário: '))
    dados['aposentadoria'] = (dados['contratacao']-ano_nasc) + 35
    print('\033[1;33m-=\033[m'*20)
    print(f'Dados do Cliente')
    print(f'Nome: {dados['nome']}')
    print(f'Idade: {dados['idade']}')
    print(f'(Carteira de Trabalho Previdência Social)\nCTPS: {dados['ctps']}')
    print(f'Ano de contratação: {dados['contratacao']}')
    print(f'Salário: {dados['salario']}')
    print(f'Data previsto para aposento : {dados['aposentadoria']}')

else:
    print('\033[1;33m-=\033[m'*20)
    print(f'Dados do Cliente')
    print(f'Nome: {dados['nome']}')
    print(f'Idade: {dados['idade']}')
    print(f'CTPS (Carteira de Trabalho Previdência Social)\nCTPS: {dados['ctps']}')

