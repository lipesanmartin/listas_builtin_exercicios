# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
# litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros
# e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo.
# O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a
# cada execução do programa.
# Comparativo de Consumo de Combustível
#
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
#
# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeot        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeot.
from tabulate import tabulate


distancia = 1000
preco_combustivel = 2.25
lista_carros = []
lista_km_litro = []
tabela_final = [["Carro", "Km/L", "Combustível", "Custo"]]
print("Comparativo de Consumo de Combustível")
for x in range(5):
    print(f"Veículo {x + 1}")
    carro = str(input("Nome: "))
    lista_carros.append(carro)
    while True:
        try:
            km_litro = float(input("Km por litro: "))
            lista_km_litro.append(km_litro)
            break
        except ValueError:
            print("Erro.")

maior_km_litro = max(lista_km_litro)
carro_economico = lista_km_litro.index(maior_km_litro)

for x in range(len(lista_carros)):
    linha_tabela = [lista_carros[x], lista_km_litro[x]]
    litros = distancia / lista_km_litro[x]
    custo = litros * preco_combustivel
    linha_tabela.append(f"{litros:.1f} litros")
    linha_tabela.append(f"R$ {custo:.2f}")
    tabela_final.append(linha_tabela)


print(tabulate(tabela_final, headers='firstrow', tablefmt='rst'))
print(f"O menor consumo é o do {lista_carros[carro_economico]}.")


















