#  Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#  cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lis2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lis3 = []

for x in range(10):
    lis3.append(lis1[x])
    lis3.append(lis2[x])

print(lis1)
print(lis2)
print(lis3)
