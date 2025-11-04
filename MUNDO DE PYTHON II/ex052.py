quantidade = int(input('Quantos números você deseja testar: '))
for i in range(1, quantidade + 1):
    numero = int(input('{}° digite: '.format(i)))
    primo = 0
    for contador in range(1, numero+1):
        if numero%contador == 0:
            primo += 1
    if primo == 2:
        print('É primo')
    else:
        print('não é primo')