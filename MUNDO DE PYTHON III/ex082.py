todos = list()
pares = []
impares = []
while True:
    numero = int(input('Adicione um número: '))
    todos.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    while True:
        decisao = str(input('Você quer continuar ')).upper().strip()[0]
        if decisao == 'N':
            break
        elif decisao == 'S':
            break
        else:
            print('Erro, tente digitar S/N')
    if decisao == 'N':
        break

print(f'Os números digitados foram {todos}')
print(f'Os números pares foram {pares}')
print(f'Os números ímpares foram {impares}')    