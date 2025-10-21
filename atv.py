import matplotlib.pyplot as plt
import numpy as np

def ler_dados():
    dados = []
    try:
        with open('notas_alunos.txt', 'r') as f:
            for linha in f:
                dados.append(linha.strip().split(','))
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return dados

def calcular_media(n1, n2, n3):
    return (n1 + n2) / 3

def gerar_grafico(series, medias):
    series_unicas = sorted(list(set(series)))
    medias_por_serie = {serie: [] for serie in series_unicas}

    for i, serie in enumerate(series):
        medias_por_serie[serie].append(medias[i])

    plt.figure(figsize=(10, 6))
    largura_barra = 0.25
    deslocamento = np.arange(0, len(np.arange(0, 11, 0.5))  largura_barra, largura_barra)
    
    for i, serie in enumerate(series_unicas):
        medias_arred = [round(m, 1) for m in medias_por_serie[serie]]
        valores, contagem = np.unique(medias_arred, return_counts=True)
        plt.bar(valores + (i * largura_barra), contagem, width=largura_barra, 
                alpha=0.6, edgecolor='black', label=f"Série {serie}")

    plt.title("Distribuição das médias finais por série")
    plt.xlabel("Quantidade de alunos")
    plt.ylabel("Média final")
    plt.legend(title="Séries")
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()
dados = ler_dados()

if dados:
    medias = []
    series = []

    for aluno in dados:
        nome, serie, n1, n2, n3 = aluno
        n1, n2, n3 = float(n1), float(n2), float(n3)
        media = calcular_media(n1, n2, n3)
        medias.append(media)
        series.append(serie)

    print("Média geral por série:")
    medias_por_serie = {}

    for i, serie in enumerate(series):
        if serie not in medias_por_serie:
            medias_por_serie[serie] = []
        medias_por_serie[serie].append(medias[i])

    for serie, lista_medias in medias_por_serie.items():
        media_geral = np.mean(lista_medias)
        print(f"Série {serie}: {media_geral:.2f}")

    gerar_grafico(series, medias)
