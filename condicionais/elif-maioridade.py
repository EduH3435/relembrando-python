idade = int(input('Qual a sua idade? '))
sexo = input('Qual o seu gênero m ou f?: ').lower()

if idade >= 18 and sexo == 'm':
    print('Você é um homem maior de idade!')
elif idade < 18 and sexo == 'm':
    print('Você é é um homem menor de idade!')
elif idade >= 18 and sexo == 'f':
    print('Você é uma mulher maior de idade!')
elif idade < 18 and sexo == 'f':
    print('Você é uma mulher menor de idade!')
else:
    print('Erro na entrada de dados.')