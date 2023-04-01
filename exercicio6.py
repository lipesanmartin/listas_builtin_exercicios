#  Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
#  imprima o número de alunos com média maior ou igual a 7.0.

medias = []
passou = 0
for alunos in range(10):
    nota1 = float(input(f"Insira a primeira nota do aluno {alunos + 1}: "))
    nota2 = float(input(f"Insira a segunda nota do aluno {alunos + 1}: "))
    nota3 = float(input(f"Insira a terceira nota do aluno {alunos + 1}: "))
    nota4 = float(input(f"Insira a quarta nota do aluno {alunos + 1}: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Média do aluno {alunos + 1} é {media:.1f}")
    medias.append(media)

for x in medias:
    if x >= 7:
        passou += 1
print("Medias:", medias)
print(f"A media de {passou} aluno(s) é maior ou igual a 7.0.")

