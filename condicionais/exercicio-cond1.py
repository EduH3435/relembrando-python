#INFORMAÇÕES AULA
aulas_dadas = 20
media = 6.0

#INFORMAÇÕES ALUNO
nome = input('Digite o nome do aluno: ')

notap1 = float(input('Digite a nota da P1 do aluno: '))
notap2 = float(input('Digite a nota da P2 do aluno: '))
media_aluno = (notap1 + notap2) / 2

faltas = int(input('Digite o número de faltas do aluno: '))
presenca = aulas_dadas - faltas

#IMPRIMINDO...
print("Aluno: ", nome)
print("Média: ", media_aluno)
assiduidade = (presenca * 100) / aulas_dadas
print("Presença: ", assiduidade, "%")

#RESULTADO
if media_aluno >= media and assiduidade >= 70:
    print("Resultado: Aprovado")
elif media_aluno >= media and assiduidade < 70:
    print("Resultado: Reprovado por faltas")
elif media_aluno < media and assiduidade >= 70:
    print("Resultado: Reprovado por média")
elif media_aluno < media and assiduidade < 70:
    print("Resultado: Reprovado por faltas e média")