def maior(*valores):
    r = 0
    print(f'Foram inseridos {len(valores)}')
    print('Os valores são: ', end=' ')
    for i in valores:
        if i == max(valores):
            r += 1
        print(i, end=' ')
    print()
    print(f'O maior valor foi {max(valores)}')
    print(f'Ele aparece {r} vezes.')

lista  = []
while True:
    numeros= int(input('Digite: '))
    lista.append(numeros)
    while True:
        resp = str(input('Deseja continuar [S/N]:  ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Digite S ou N')
    if resp == 'N':
        break
maior(*lista)