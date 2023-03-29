#  Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
#  a soma dos quadrados dos elementos do vetor.

lis = []
quadrados = []
for x in range(10):
    numero = int(input(f"Insira o {x + 1}º número: "))
    lis.append(numero)

for x in range(len(lis)):
    quadrado_numero = lis[x] ** 2
    quadrados.append(quadrado_numero)

print("Lista original:", lis)
print("Lista dos quadrados:", quadrados)
print("Soma dos quadrados =", sum(quadrados))
