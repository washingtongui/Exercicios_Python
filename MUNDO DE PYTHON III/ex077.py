palavras = (
    'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
    'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
)
for palavras in palavras:
    print(f'\n{palavras}', end=': ')
    for letras in palavras:

        if letras in 'aeiou':
            print(letras, end=' ')
