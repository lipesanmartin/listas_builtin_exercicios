#  Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#  Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []

for pessoa in range(5):
    altura = float(input(f"Insira a altura da {pessoa + 1}ª pessoa: "))
    alturas.append(altura)
    idade = int(input(f"Insira a idade da {pessoa + 1}ª pessoa: "))
    idades.append(idade)

print("Idades:", idades)
print("Alturas:", alturas)
idades.reverse()
alturas.reverse()
print("Idades invertido:", idades)
print("Alturas invertido:", alturas)
