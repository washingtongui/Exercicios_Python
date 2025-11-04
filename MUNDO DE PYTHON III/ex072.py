numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
    'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze',
    'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:
    numero_extenso = int(input('Digite um número entre 0 e 20 para vê-lo: '))
    if 0 <= numero_extenso <= 20:
        print(numeros[numero_extenso])
        break