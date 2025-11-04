print('\033[1;36m=-\033[m'*12)
print("\033[1mCAIXA ELETRÔNICO TOM'S\033[m")
print('\033[1;36m=-\033[m'*12)
saque = int(input('Digite o valor de saque: '))
notas_50 = notas_20 = notas_10 = notas_1 = 0
while True:
    if saque == 0:
        break
    if saque >= 50:
        saque -= 50
        notas_50 += 1
    elif saque >= 20:
        saque -= 20
        notas_20 += 1
    elif saque >= 10:
        saque -= 10
        notas_10 += 1
    elif saque >= 1:
        saque -= 1
        notas_1 += 1
if notas_50 >= 1:
    print(f'{notas_50} notas de 50,00')
if notas_20 >= 1:
    print(f'{notas_20} notas de 20,00')
if notas_10 >= 1:
    print(f'{notas_10} notas de 10,00')
if notas_1 >= 1:
    print(f'{notas_1} notas de 1,00')