lado1 = float(input('Digite o Primeiro lado: '))
lado2 = float(input('Digite o Segundo lado: '))
lado3 = float(input('Digite o Terceiro lado:'))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('TRIÂNGULO EQUILÁTERO.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('TRIÂNGULO ISÓSCELES.')
    else:
        print('TRIÂNGULO ESCALENO.')
else:
    print('\033[1;31mNão é um triângulo!!!\033[m')