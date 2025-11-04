numero = int(input('De qual número você quer começar? '))
fim_numero = int(input('Até onde quer ir? '))
escolha = int(input('Escolha uma opção:\n(1) ÍMPARES \n(2) PARES: '))
Quantidade = 0
numeros = []

if escolha == 1 and numero < fim_numero:
    for n in range(numero, fim_numero):
        if n % 2 == 1:
            Quantidade += 1
            numeros.append(str(n))
elif escolha == 1 and numero > fim_numero:
    for n in range(numero, fim_numero - 1, -1):
        if n % 2 == 1:
            Quantidade += 1
            numeros.append(str(n))
elif escolha == 2 and numero < fim_numero:
    for n in range(numero, fim_numero):
        if n % 2 == 0:
            Quantidade += 1
            numeros.append(str(n))
elif escolha == 2 and numero > fim_numero:
    for n in range(numero, fim_numero - 1, -1):
        if n % 2 == 0:
            Quantidade += 1
            numeros.append(str(n))
else:
    print('\033[1;31mVOCÊ NÃO ESCOLHEU NENHUMA OPÇÃO!!!\033[m')

if numeros:
    print(', '.join(numeros))
    print('São', Quantidade, 'no Total.')