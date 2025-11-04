#Termo a ser encontrado.7
# a1 o primeiro termo, n = numero de termos -1, R = razão entre um número e outro.
print('P R O G R E S S Ã O    A R I T M É T I C A')
a1 = int(input('QUAL É O PRIMEIRO TERMO: '))
r = int(input('QUAL É A RAZÃO DESSA P.A: '))
termo10 = a1 + (11 - 1) * r
quantidade = 0
for contador in range(a1, termo10, r):
    quantidade += 1
    print('{}° = {} '.format(quantidade, contador))