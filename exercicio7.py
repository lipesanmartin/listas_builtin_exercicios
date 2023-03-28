#  Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lis = []
for x in range(5):
    numero = int(input(f"Insira o {x + 1}º número: "))
    lis.append(numero)

produto = 1
for x in range(5):
    produto *= lis[x]

print(lis)
print("Soma entre os números:", sum(lis))
print("Produto dos números:", produto)
