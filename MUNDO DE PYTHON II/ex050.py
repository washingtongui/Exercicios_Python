par = 0
soma = 0
for contador in range(1, 7):
    numero = int(input('Digite {}° número:  '.format(contador)))
    if numero % 2 == 0:
        soma += numero
        par += 1
print('São {} números pares e a soma deles resulta em: {}    '.format(par, soma))