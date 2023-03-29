#  Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
#  calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#  e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro"]
temperaturas_meses = []

for x in range(12):
    temperatura = float(input(f"Insira a temperatura média de {meses[x]}: "))
    temperaturas_meses.append(temperatura)

media_anual = sum(temperaturas_meses) / len(meses)

print(f"\nMédia anual: {media_anual:.1f}°C\n\nMeses com temperatura média acima da média anual:")
for x in range(12):
    if temperaturas_meses[x] > media_anual:
        print(f"{x + 1} - {meses[x]}: {temperaturas_meses[x]:.1f}°C")
