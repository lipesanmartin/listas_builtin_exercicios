# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

lista_notas = []
# lista_notas_reversa = []
cont = 1
while True:
    nota = float(input(f"Insira a {cont}ª nota: "))
    if nota == -1:
        break
    elif 0 <= nota <= 10:
        lista_notas.append(nota)
        cont += 1
    else:
        print("Valor inválido.")
soma = sum(lista_notas)
media = soma / len(lista_notas)
acima_da_media = 0
menor_que_7 = 0
print(*lista_notas, sep=', ')
lista_notas.reverse()
for x in lista_notas:
    print(x)
    if x > media:
        acima_da_media += 1
    if x < 7:
        menor_que_7 += 1
print("A soma das notas é:", soma)
print(f"A média das notas é: {media:.1f}")
print(f"{acima_da_media} notas estão acima da média.")
if menor_que_7 == 0:
    print("Nenhuma nota abaixo de 7.")
else:
    print(f"{menor_que_7} nota(s) abaixo de 7.")
print("Programa Finalizado.")
