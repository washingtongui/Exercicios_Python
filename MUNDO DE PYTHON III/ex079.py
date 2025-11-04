aleatorios = []
parada_forcada = ''
while True:
    if parada_forcada == 'OK':
        break
    valores = int(input('Digite um valor: '))
    if valores in aleatorios:
        print('Valor duplicado não será adicionado, tente novamente!')
    else:
        print('Valor adicionado com sucesso... ')
        aleatorios.append(valores)
    while True:
        resposta = str(input('Quer continuar? Digite [S/N]')).upper().strip()[0]
        if resposta == 'N':
            parada_forcada = 'OK'
            break
        elif resposta == 'S':
            break
        else:
            print('Tente novamente')
print(sorted(aleatorios))