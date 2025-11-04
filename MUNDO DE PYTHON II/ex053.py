frase = str(input('Digite um palíndromo para confirmarmos: ')).upper().strip()
frase_sem_espaco = ''.join(frase.split())
inverso = frase_sem_espaco[::-1]
if frase_sem_espaco == inverso:
    print(f'A frase {frase}, é um palíndromo.')
else:
    print(f'A frase: {frase}, Não é um palíndromo.')