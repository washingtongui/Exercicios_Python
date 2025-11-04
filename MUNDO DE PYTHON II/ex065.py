resposta = 'S'
somador = 0
contador = 0
maior = 0
menor = 0
while resposta == 'S':
    if resposta == 'S':
        numero = int(input('Digite um número inteiro: '))
        somador += numero
        contador += 1
        if contador == 1:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    resposta = str(input('Quer continuar [S/N]? ')).upper().strip()
print('A média de {} é {:.1f}'.format(somador, somador/contador))
print('O maior número digitado foi: {} e o menor foi: {}'.format(maior, menor))