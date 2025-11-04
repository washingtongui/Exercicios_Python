expressao = str(input('Digite uma expressão: \n'))
#A mesma quantidade de parênteses aberto tem que ser fechado também.
parenteses = 0
for validador in expressao[0:]:
    if validador == '(':
        parenteses += 1
    if validador == ')':
        parenteses -= 1
print('-'*20)
print(parenteses)
print('-'*20)
if parenteses == 0:
    print('Sua expressão é valida!')
else:
    print('expressão invalida!')