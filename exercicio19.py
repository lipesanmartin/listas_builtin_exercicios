#  Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
#  organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
# mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das
# opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular
# a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa,
# e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
#
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
from tabulate import tabulate

lista_sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
lista_votos = []
tabela_resultados = [["Sistema Operacional", "Votos", "%"]]

print("Qual o melhor Sistema Operacional para uso em servidores?")
while True:
    for x in range(6):
        print(f"{x + 1}- {lista_sistemas[x]}")
    voto = int(input())
    if voto == 0:
        break
    elif voto in range(1, 7):
        lista_votos.append(voto)
    else:
        print("Valor inválido. Digite 1 a 6 ou 0 para sair.")

numero_de_votos = []
for x in range(6):
    contador = lista_votos.count(x + 1)
    numero_de_votos.append(contador)
mais_votos = max(numero_de_votos)
ganhador = numero_de_votos.index(mais_votos)

#  montagem da lista tabela
for x in range(6):
    lis = [lista_sistemas[x], lista_votos.count(x + 1)]
    porcentagem = str(round((numero_de_votos[x] / len(lista_votos)) * 100)) + '%'
    lis.append(porcentagem)
    tabela_resultados.append(lis)
tabela_resultados.append(["Total", len(lista_votos)])
print(tabulate(tabela_resultados, headers='firstrow', tablefmt='fancy_grid'))
print(
    f"O sistema operacional mais votado foi o {lista_sistemas[ganhador]}, com {lista_votos.count(ganhador + 1)} votos,"
    f" correspondendo a {int((numero_de_votos[ganhador] / len(lista_votos)) * 100)}% dos votos.")
