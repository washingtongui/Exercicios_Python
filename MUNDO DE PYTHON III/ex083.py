#Analisando a resolução do Guanabara ex083 aula 17 mundo de Python III.

#primeio receberemos a expressão.
expressao = str(input('Digite sua expressão: '))
#Toda string é uma lista.
#Criando uma lista vazia.
pilha = []
#Vamos usar for para analisar cada parênteses, digitado.
for simbolo in expressao:
    #validação de parênteses aberto
    if simbolo == '(':
        pilha.append('(')
    #Para essa verificação a lista pode estar cheia ou vazia.
    elif simbolo == ')':
        #Verificando se tem '(' na lista.
        if len(pilha) > 0:
            pilha.pop()
        else:
            #Sinal de que tem mais parênteses fechando do que abrindo.
            pilha.append(')')
            #Pelo que analise se o primeiro caractere for um ')' ele adiciona na lista e para o loop.
            break
if len(pilha) == 0:
    print('Sua expressão está valida.')
else:
    print('Sua expressão está invalida.')