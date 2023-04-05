# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
# o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
#
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que
# gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
#
# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB

from tabulate import tabulate


def bytes_to_megabytes(byte):
    megabytes = (byte / 1024) / 1024
    return megabytes


if __name__ == '__main__':

    tabela = [["N°", "Usuário", "Espaço utilizado", "% do uso"]]
    lista_usuarios = []
    lista_espaco_utilizado = []

    with open("usuários.txt", "r") as usuarios:
        for linha in usuarios:
            usuario = linha[:15]
            usuario_sem_espaco = usuario.strip()
            lista_usuarios.append(usuario_sem_espaco)
            espaco = linha[15:]
            tamanho_ocupado = espaco.strip()
            lista_espaco_utilizado.append(round(bytes_to_megabytes(int(tamanho_ocupado)), 2))

    for x in range(len(lista_usuarios)):
        porcentagem = round(lista_espaco_utilizado[x] / sum(lista_espaco_utilizado) * 100, 2)
        tabela.append([x + 1, lista_usuarios[x], str(lista_espaco_utilizado[x]) + ' MB', str(porcentagem) + '%'])

        try:
            relatorio = open('relatório.txt', 'w')
            relatorio.write(tabulate(tabela, headers="firstrow", tablefmt="srt"))
            relatorio.close()
        except Exception as e:
            print("Exception:", e)


    print(tabulate(tabela, headers="firstrow", tablefmt="srt"))
