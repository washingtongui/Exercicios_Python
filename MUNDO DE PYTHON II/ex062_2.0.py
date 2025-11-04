print('-='*19)
print('\033[1;32mPROGRESSÃO ARITMÉTICA\033[m \033[1;31mVERSÃO COM WHILE\033[m')
print('-='*19)
a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual é a razão: '))
SomaTermo = a1
contador = 1
termoinicial = 9
mais = 1
while mais != 0:
    termoinicial += mais
    while contador < termoinicial + 1:
        print('{:2}°'.format(contador), end=' = ')
        print('{}'.format(SomaTermo))
        SomaTermo += r
        contador += 1
    mais = int(input('Quantos termos a mais você deseja ver: '))
