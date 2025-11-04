Nome = str(input('Digite o seu nome completo: ')).title().strip()
print('O nome digitado foi: {}'.format(Nome))
print('O primeiro nome é {}'.format(Nome.split()[0]))
print('O último nome é {}'.format(Nome.split()[-1]))
