print('VAMOS DESCOBRIR SE É TRIANGULO.')
lado1 = float(input('Qual o tamanho deste lado: '))
lado2 = float(input('Qual o tamanho dest outro lado: '))
lado3 = float(input('E por fim, Digite o último lado: '))
if lado1 + lado2 > lado3:
    print('Sim, isto é um triângulo.')
    if lado1 + lado3 > lado2:
        print('Sim, é um triângulo.')
        if lado2 + lado3 > lado1:
            print('Sim, é um triângulo.')
        else:
            print('Não forma um triângulo.')
    else:
        print('Não é um triângulo.')
else:
    print('Não pode formar um triângulo.')