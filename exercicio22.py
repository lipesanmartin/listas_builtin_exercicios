# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer
# um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que
# se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
# indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# 1 necessita da esfera;
# 2 necessita de limpeza;
# 3 necessita troca do cabo ou conector;
# 4 quebrado ou inutilizado
# Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100
#
# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

from tabulate import tabulate

tabela = [["Situação", "Quantidade", "Percentual"]]
lista_problemas = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo ou conector",
                   "quebrado ou inutilizado"]
lista_entradas = []
mouse = 1
while True:
    print(f"Defina a situação do mouse {mouse}")
    cont = 1
    for elementos in lista_problemas:
        print(f"{cont} - {elementos}")
        cont += 1
    try:
        entrada = int(input())
        if entrada == 0:
            break
        elif entrada in range(1, 5):
            lista_entradas.append(entrada)
        else:
            print("Insira um valor de 1 a 4 (0 para finalizar)")
    except ValueError:
        print("Insira um valor de 1 a 4 (0 para finalizar)")
    mouse += 1

lista_quantidades = []  # quantidade de cada problema
for a in range(1, 5):
    lista_quantidades.append(lista_entradas.count(a))
print(lista_quantidades)

lista_percentual = []  # percentuais de ocorrencia
for b in range(4):
    percentual = f'{(lista_quantidades[b] / len(lista_entradas)) * 100:.1f} %'
    lista_percentual.append(percentual)

for c in range(4):
    tabela.append([f'{c + 1}- ' + lista_problemas[c], lista_quantidades[c], lista_percentual[c]])

print(tabulate(tabela, headers='firstrow', tablefmt='mixed_outline'))
