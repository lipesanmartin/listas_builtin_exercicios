# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função
# para gerar numeros aleatórios, simulando os lançamentos dos dados.
import random

dado = [1, 2, 3, 4, 5, 6]
resultados = []
for x in range(100):
    jogar_dado = random.choice(dado)
    resultados.append(jogar_dado)

ocorrencias = []
for x in range(1, 7):
    contador = resultados.count(x)
    ocorrencias.append(contador)

print(resultados)
for x in range(6):
    print(f"Número {x + 1} saiu {ocorrencias[x]} vezes.")
