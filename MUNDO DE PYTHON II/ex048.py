impares_multiplo = 0
soma = 0
for contador in range(1, 501):
    if contador % 2 != 0 and contador % 3 == 0:
       soma += contador
       impares_multiplo += 1
print('São: {} números ímpares divisíveis por 3 no total.'.format(impares_multiplo))
print('A soma entre todos os números é {}'.format(soma))