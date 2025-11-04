alunos = [
]
informacoes = {
}

while True:
    informacoes['nome'] = str(input('Digite seu nome: '))
    informacoes['media'] = float(input('Digite sua média: '))
    if informacoes['media'] >= 8:
        informacoes['status'] = 'Aprovado'
    else:
        informacoes['status'] = 'reprovado'
    alunos.append(informacoes.copy())
    resp = str(input('Cadastrar mais um aluno? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('\033[1;32m-=\033[m'*20)
print('\033[1;33mESCOLA CAVALO MANCO\033[m')
print('')
for aluno in alunos:
    print(f'{aluno['nome']} →  {aluno['media']} = {aluno['status']}')