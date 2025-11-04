#Importanto uma biblioteca apenas para uma experiência melhor para o usuário.
from time import sleep
#Uma lista para uma variação de dados a vontade do usuário.
dados_pessoas = list()
#utilizarei essa variável de dicionário para copiar os dados para a lista principal.
dados_individuais = dict()
#Separação de dados somente para as mulheres.
dados_mulheres = list()
#Pessoas com idades acima da média.
acima_media_idade = list()
#Contador de pessoas.
quant_cadastros = 0
#A média de todas as idades
soma_idades = 0
#Aqui será o Loop.
while True:
    #Usarei alguns tratamentos de strings para evitar erros feitos pelo usuário.
    dados_individuais["nome"] = (str(input('Digite seu nome: ').capitalize().strip()))
    while True:
        dados_individuais["sexo"] = (str(input('Qual seu sexo [F/M]: ').upper().strip()[0]))
        if dados_individuais['sexo'] in 'FM':
            break
        else:
            print('\033[1;31mDigite F ou M\033[m')
    dados_individuais["idade"] = (int(input('Qual é sua idade: ')))
    dados_pessoas.append(dados_individuais.copy())
    #Aqui será a decisão para que o loop continue ou pare, após já ter cadastrado uma pessoa.
    while True:
        resposta = str(input('Cadastra mais uma pessoas [S/N]')).upper().strip()[0]
        #Eu poderia fazer outro loop aqui para aceitar apenas N ou S, mas vou respeitar as boas práticas e tratamento de
        #erros, como não chegamos nisso deixarei assim nesse momento.
        #Ele usou na correção vim e implementei.
        if resposta == 'N':
            break
        elif resposta == 'S':
            print('Continuaremos...')
            # Apenas uma experiência visual mesmo, nada de tão importante no código.
            for c in range(1, 4):
                print('.')
                sleep(0.5)
            break
        else:
            print('\033[1;31mDigite S ou N\033[m')
    if resposta == 'N':
        break
#Contador de cadastro, eu poderia ter feito lá no append de dados, mas não é essa a proposta do exercício.
for contador in dados_pessoas:
    quant_cadastros += 1
#Nesse pequeno laço faremos a soma das idades.
for dicionario in dados_pessoas:
    soma_idades += dicionario['idade']
#Aqui cadastraremos todas as mulheres em outra lista, pois o enunciado pede isso.
for dicionario in dados_pessoas:
    if dicionario['sexo'] == 'F':
        dados_mulheres.append(dicionario.copy())
#Adicionando pessoas acima da idade da média entre todos.
for dicionario in dados_pessoas:
    if dicionario['idade'] > soma_idades/quant_cadastros:
        acima_media_idade.append(dicionario.copy())
#Uma pequena separação de elementos.
print('=-'*20)
print(f'No total serão {quant_cadastros} pessoas cadastradas.')
print(f'A média da idade desse grupo de pessoas é: {soma_idades/quant_cadastros:.1f}')
print('As mulheres cadastradas foram:', end=' ')
for dicionario in dados_mulheres:
    print(dicionario['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for dicionario in acima_media_idade:
    print(dicionario)