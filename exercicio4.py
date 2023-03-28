#  Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lis = []
cons = 0
for x in range(10):
    elemento = str(input("Insira um caracter para adicionar à lista: "))
    lis.append(elemento)

for x in range(10):
    if lis[x] not in "aeiou":
        print(lis[x])
        cons += 1
print(f"Existem {cons} consoantes no vetor {lis}.")
