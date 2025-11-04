maioridade = 0
quantidade_M = 0
menores_F = 0
while True:
    print('\033[1;36m=-\033[m'*20)
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o seu sexo [F/M]: ')).upper().strip()[0]
    idade = int(input('Qual é a sua idade: '))
    print('\033[1;36m=-\033[m'*20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar: S/N: ')).upper().strip()[0]
    if idade > 18:
            maioridade += 1
    if sexo == 'M':
            quantidade_M += 1
    if sexo == 'F' and idade < 20:
            menores_F += 1
    if resposta == 'N':
        break
    elif resposta != 'S':
        print(f'\033[1;31m{resposta}\033[m é uma resposta invalida!!!')
print(f'\033[1mFora {maioridade} pessoas maiores de 18 anos de idade.')
print(f'A quantidade de homens nessa lista foi de: {quantidade_M}')
print(f'E {menores_F} Mulheres com menos de 20 anos de idade.')
