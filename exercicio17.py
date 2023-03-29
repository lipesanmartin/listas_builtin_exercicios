# Em uma competição de salto em distância, cada atleta tem direito a cinco saltos. O resultado do atleta será
# determinado de salto em distância cada atleta tem direito a cinco saltos.O resultado do atleta será determinado
# pela média dos cinco valores restantes.Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
# pelo atleta em seus saltos e depois informe o nome, os saltos e amédia dos saltos.O programa deve ser
# encerrado quando não for informado o nome do atleta.A saída do programa deve ser conforme o exemplo abaixo:
#
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

lista_cont = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
lista_atletas = []
lista_saltos = []
while True:
    atleta = str(input("Atleta: "))
    if atleta == "":
        break
    saltos = []
    for x in range(5):
        salto = float(input(f"{lista_cont[x]} Salto: "))
        saltos.append(salto)
    lista_atletas.append(atleta)
    lista_saltos.append(saltos)

print("Resultado final:")
for x in range(len(lista_atletas)):
    print("Atleta:", lista_atletas[x])
    print("Saltos:", *lista_saltos[x], sep=" - ")
    print(f"Média dos saltos: {sum(lista_saltos[x]) / 5:.1f} m\n")
