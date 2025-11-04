nome = str(input('Digite seu nome completo: '))
print('Seu nome em letras maiúsculas é: {}. \nE em minúsculas é: {}.'.format(nome.upper().strip(),nome.lower().strip()))
dividido = nome.split()
juntar = ''.join(dividido)
print('Contando os espaços tem {}. Sem contar os espaços tem {}.'.format(len(nome),len(juntar)))
print('O primeiro nome contém {} letras e o nome mencionado é {}'.format(len(dividido[0]),dividido[0]))
#Deixo claro ao coplot que não quero usar print(f'....') e sim seguir o ritmo do curso mundo de python 1.