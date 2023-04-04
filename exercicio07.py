#  Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import math

lis = []
for x in range(5):
    numero = int(input(f"Insira o {x + 1}º número: "))
    lis.append(numero)

print(lis)
print("Soma entre os números:", sum(lis))
print("Produto dos números:", math.prod(lis))
