#  Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#  Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


lis = []
pares = []
impares = []
for x in range(20):
    numero = int(input(f"Insira o {x + 1}º inteiro para a lista: "))
    lis.append(numero)

for x in range(20):
    if lis[x] % 2 == 0:
        pares.append(lis[x])
    else:
        impares.append(lis[x])
print(f"Lista original: {lis}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
