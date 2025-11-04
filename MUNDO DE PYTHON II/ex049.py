tabuada = int(input('Qual tabuada você deseja ver? '))
for contador in range(0, 11):
    print('{} X {:2} = {:2}'.format(tabuada, contador, contador*tabuada))
