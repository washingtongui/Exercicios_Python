alt = float(input('Digite a altura da parede: '))
larg = float(input('Largura da parede: '))
Area = (alt * larg)
#Metro quadrado total
Qtinta = (Area/2)
#Quantidade de tinta total
print('Altura: {:.1f} m \nLargura: {:.1f} m \nArea: {:.1f} m\u00b2'.format(alt, larg, Area))
print(f'A quantidade de tinta necessária é: {Qtinta:.2f}L de tinta.')