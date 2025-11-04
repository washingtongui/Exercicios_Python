contador = somador = 0
while True:
    print('CASO QUEIRA PARAR O PROGRAMA DIGITE: 999')
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    somador += numero
    contador += 1
print(f'Este é o {contador}° E a soma até agora é: {somador}')