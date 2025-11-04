aleatorios = list()
for contador in range(0, 5):
    numeros = int(input('Digite um número: '))
    aleatorios.append(numeros)
print(aleatorios)
print(f'O maior número digitado foi: {max(aleatorios)} e estão nas posições', end=' ')
# Aqui é o pulo do gato para descobrir posição.
for posicao, numeros in enumerate(aleatorios):
    if numeros == max(aleatorios):
        print(f'{posicao}°', end=' ')
print()
print(f'O menor número digitado foi: {min(aleatorios)} e estão nas posições', end=' ')
for posicao, numeros in enumerate(aleatorios):
    if numeros == min(aleatorios):
        print(f'{posicao}°', end=' ')