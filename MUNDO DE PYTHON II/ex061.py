print('-='*19)
print('\033[1;32mPROGRESSÃO ARITMÉTICA\033[m \033[1;31mVERSÃO COM WHILE\033[m')
print('-='*19)
a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual é a razão: '))
termo_10 = a1
contador = 1
while contador < 11:
    print('{:2}°'.format(contador), end=' = ')
    print('{}'.format(termo_10))
    termo_10 += r
    contador += 1
''