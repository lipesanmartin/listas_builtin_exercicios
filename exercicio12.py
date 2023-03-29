#  Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
#  quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []
alunos = 0

for aluno in range(30):
    altura = float(input(f"Insira a altura do {aluno + 1}º aluno: "))
    alturas.append(altura)
    idade = int(input(f"Insira a idade do {aluno + 1}º aluno: "))
    idades.append(idade)

media_altura_turma = sum(alturas) / len(alturas)
for x in range(len(idades)):
    if idades[x] > 13 and alturas[x] > media_altura_turma:
        alunos += 1

print("Média de altura:", media_altura_turma)
print(f"{alunos} alunos possuem mais de 13 anos e são mais altos que a média da turma.")
