contador = int(input('Digite um número: '))
fatorial = 1
print('\033[1;32mC A L C U L A D O R A   F A T O R I A L\033[m')
print('\033[1;31m{}!\033[m'.format(contador))
while 0 < contador:
    print('\033[1m{}\033[m'.format(contador), end='')
    print(' \033[1;33mX\033[m 'if contador > 1 else ' \033[1;33m=\033[m ', end='')
    fatorial *= contador
    contador -= 1
print('\033[1;31m{}\033[m'.format(fatorial))