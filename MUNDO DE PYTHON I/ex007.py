print('--------------------------------------------')
print('')
print('E S C O L A  C A V A L O  M A N C O')
print('')
print('--------------------------------------------')
nome = str(input('Digite seu nome: '))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = ((n1 + n2) / 2)
print('A sua primeira nota foi: {:.1f}. \nE a sua segunda nota foi {:.1f}.'
      ' \nE a média entre elas é: {:1f}!'.format(n1, n2, m))

# {:.2f} → formata um número float com 2 casas decimais
# {}     → espaço onde o valor será inserido
# :      → inicia a formatação
# .2     → define duas casas decimais
# f      → indica que o valor é do tipo float (número decimal)

# \n → caractere especial que representa uma quebra de linha (newline)
# Quando usado em uma string, faz o texto continuar na linha de baixo
# Exemplo: print("Olá\nMundo") → imprime:
# Olá
# Mundo