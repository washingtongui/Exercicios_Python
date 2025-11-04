print('-='*19)
print('\033[1;32mPROGRESSÃO ARITMÉTICA\033[m \033[1;31mVERSÃO COM WHILE\033[m')
print('-='*19)
resposta = 'S'
while resposta in ['S']:
    a1 = int(input('Qual o primeiro termo: '))
    r = int(input('Qual é a razão: '))
    termo = int(input('Qual termo você deseja ver: '))
    termo_10 = a1
    contador = 1
    while contador < termo + 1:
        print('{:2}°'.format(contador), end=' = ')
        print('{}'.format(termo_10))
        termo_10 += r
        contador += 1
    resposta = str(input('DESEJA CONTINUAR [S/N]: ')).upper().strip()