
termo1 = 0
termo2 = 1
termo3 = 0
contador = 1
Total_termo = int(input('até qual termo você deseja ver '))
print('{} \n{}'.format(termo1, termo2))
while contador < Total_termo + 1:
    contador += 1
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    print(termo3)