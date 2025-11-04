
print('\033[1mCONVERSÃO DE BASES')
numero = int(input('Digite um número: '))
escolha = str(input('Escolha: \n[1] Binário \n[2] Octal \n[3] Hexadecimal \n '))
if escolha == '1':
    print(bin(numero)[2:])
elif escolha == '2':
    print(oct(numero)[2:])
elif escolha == '3':
    print(hex(numero)[2:])
else:
    print('Você não escolheu nenhuma das opções!')