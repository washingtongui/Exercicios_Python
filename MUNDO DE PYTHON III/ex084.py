cadastro = list()
dados_temporarios = list()
cont_cadastro = 0
cont_pesados = 0
nomes_pesados = []
cont_leves = 0
nomes_leves = []
saida = ''
while True:
    if saida == 'ok':
        break
    dados_temporarios.append(str(input('Digite seu nome: ')))
    dados_temporarios.append(float(input('Digite seu peso (KG): ')))
    cadastro.append(dados_temporarios[:])
    cont_cadastro += 1
    if cont_cadastro == 1:
        cont_pesados = dados_temporarios[1]
        cont_leves = dados_temporarios[1]
        nomes_pesados.append(dados_temporarios[0])
        nomes_leves.append(dados_temporarios[0])
    else:
     if cont_pesados <= dados_temporarios[1]:
        if cont_pesados < dados_temporarios[1]:
            nomes_pesados.clear()
        nomes_pesados.append(dados_temporarios[0])
        cont_pesados = dados_temporarios[1]
     elif cont_leves >= dados_temporarios[1]:
        if  cont_leves > dados_temporarios[1]:
            nomes_leves.clear()
        nomes_leves.append(dados_temporarios[0])
        cont_leves = dados_temporarios[1]
    while True:
        decisao = str(input('Você quer continuar? ')).upper().strip()[0]
        if decisao == 'S':
            break
        elif decisao == 'N':
            saida = 'ok'
            break
        else:
            print('Escolha S ou N')
    dados_temporarios.clear()
print(cadastro)
print(f'Foram cadastradas {cont_cadastro} pessoas.')
print(f'O maior peso registrado foi: {cont_pesados} de {nomes_pesados}')
print(f'O menor peso registrado foi: {cont_leves} de {nomes_leves}')