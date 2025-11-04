while True:
    contador = 0
    tabuada = int(input('Qual tabuada você deseja ver: '))
    if tabuada == -(abs(tabuada)):
        break
    while contador < 10:
        contador += 1
        print(f'{tabuada} X {contador} = {tabuada * contador}')