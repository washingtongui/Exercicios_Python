lista = list()
valores = 1
contador = 0
numero = int(input('Adicione um número: '))
lista.append(numero)
if numero == 5:
    contador += 1
while True:
    resposta = str(input('Você quer continuar ?')).upper().strip()[0]
    if resposta == 'N':
        break
    elif resposta not in 'SN':
        print('Opção invalida')
    else:
        numero = int(input('Adicione um número: '))
        lista.append(numero)
        valores += 1
        if numero == 5:
            contador += 1
print(f'Foram digitados {valores}')
print(f'lista em ordem decrescente {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'Sim o número 5 estava na lista e aparece {contador} vezes.')
else:
    print('Não o número 5 não está na lista.')
