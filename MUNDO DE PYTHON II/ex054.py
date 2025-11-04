from datetime import date
repetir = 7
maioridade = 0
menoridade = 0
for i in range(1, repetir+1):
    ano_nascimento = int(input('Qual é o seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print(idade)
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f'São {maioridade} que estão na maioridade. \nE {menoridade} que estão na menoridade.')