#Importando biblioteca time para usar apenas o sleep.
from time import sleep


#Criando uma def para evitar repetição de código.
def contador(a, b, c):
    for i in range(a ,b , c):
        print(i, end=' ')
        sleep(0.4   )
    print()


#Criando uma def linha para evitar repetição de código.
def linha():
    print('\033[1;34m-=\033[m'*25)


linha()
# a) De 1 até 10 passo 1.
contador(1, 11, 1)
linha()
#De 10 até 0 de 2 passo 2
contador(10, -2, -2)
linha()

#Coletando dados.
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('pulando: '))

#Tratando erros.
if passo == 0:
    passo = 1

#condições para funcionamento do código
if inicio < fim and passo == + abs(passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    fim += passo

    contador(inicio, fim, passo)
elif inicio > fim:
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim  < 0:
        fim -= abs(passo)
    else:
        fim -= abs(passo)
    passo = - abs(passo)
    contador(inicio, fim, passo)
elif inicio < passo > fim:
    print('O passo não pode ser mais do que a contagem!')