def area(a, b):
    area_terreno = a * b
    print(area_terreno)
def linha():
    print('\033[1;33m-=\033[m'*15)


linha()
informacoes = str(input('Qual o terreno: '))
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
linha()
print(f'Informações: {informacoes} \nLargura: {largura} X Altura {altura} ')
print('Área: ', end=": ")
area(altura, largura)