impares_pares = [[],[]]
for contador in range(1, 8):
    numero = int(input(f'{contador}° Digite um número: '))
    if numero % 2 == 0:
        #Números pares
        impares_pares[0].append(numero)
    else:
        #Números ímpares.
        impares_pares[1].append(numero)
impares_pares[0].sort()
impares_pares[1].sort()
print(f'Os números pares digitados: {impares_pares[0]}')
print(f'Os números impares digitados: {impares_pares[1]}')
