Total_idade = 0
Mais_velho = 0
Nome_velho = ''
Mais_novas = 0
for contador in range(1,5): #Eu quero 4 então coloco 1 número a mais.
    nome = str(input('Digite o Nome: ')).title().strip() #strip() para tirar os espaços
    idade = int(input('Digite a Idade: '))
    sexo = str(input('F -> Feminino ou M -> Masculino: ')).strip().upper()
    Total_idade += idade #Para fazer a soma de todas as idades que passar no “Loop”.
    if sexo == 'M' and idade > Mais_velho:
        Mais_velho = idade
        Nome_velho = nome
    elif sexo == 'F' and idade < 20:
        Mais_novas += 1
print('\033[1mA média de todas as idades é {:.1f}'.format(Total_idade/4))
print('O nome do homem mais velho é {} e a idade é {} anos.'.format(Nome_velho, Mais_velho))
print('São {} mulheres com menos de 20 anos de idade.\033[m'.format(Mais_novas))