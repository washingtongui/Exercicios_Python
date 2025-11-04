from random import randint
aleatorios = (
    randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
)
contador = menor = maior = 0
for numeros in aleatorios:
    contador += 1
    print(f'{contador}°', end=' = ')
    print(numeros)
    if contador == 1:
        menor = maior = numeros
    else:
        if maior < numeros:
            maior = numeros
        if menor > numeros:
            menor = numeros
print(f'Os números escolhidos pelo computador fora: {aleatorios}')
print(f'O maior numero foi: {maior} e o menor {menor}')