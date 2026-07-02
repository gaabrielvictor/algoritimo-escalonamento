# ============================================================
# UTILITÁRIO: Geração de Gráficos
#
# Gera gráficos de Hit Ratio x Capacidade do Cache
# para as três políticas (FIFO, LRU, LFU) usando Matplotlib.
# ============================================================

import matplotlib.pyplot as plt
import os


def gerar_grafico_comparativo(resultados: dict, pasta_saida: str = "results") -> str:
    """
    Gera um gráfico comparativo com as três políticas em um único gráfico.

    Parâmetros:
        resultados   : dicionário no formato
                       { "FIFO": [(cap, hit_ratio), ...],
                         "LRU":  [(cap, hit_ratio), ...],
                         "LFU":  [(cap, hit_ratio), ...] }
        pasta_saida  : pasta onde o arquivo PNG será salvo

    Retorna:
        Caminho do arquivo gerado.
    """
    os.makedirs(pasta_saida, exist_ok=True)

    # Configuração visual do gráfico
    plt.figure(figsize=(10, 6))
    plt.style.use("seaborn-v0_8-whitegrid")

    # Cores e marcadores para cada política
    estilos = {
        "FIFO": {"color": "#E74C3C", "marker": "o", "linestyle": "-"},
        "LRU":  {"color": "#2980B9", "marker": "s", "linestyle": "--"},
        "LFU":  {"color": "#27AE60", "marker": "^", "linestyle": "-."},
    }

    # Plota uma linha para cada política
    for politica, pontos in resultados.items():
        capacidades = [p[0] for p in pontos]
        hit_ratios  = [p[1] for p in pontos]
        estilo = estilos.get(politica, {})
        plt.plot(
            capacidades, hit_ratios,
            label=politica,
            linewidth=2.5,
            markersize=8,
            **estilo
        )
        # Adiciona anotação com o valor de hit ratio em cada ponto
        for cap, hr in zip(capacidades, hit_ratios):
            plt.annotate(
                f"{hr:.1f}%",
                xy=(cap, hr),
                xytext=(0, 10),
                textcoords="offset points",
                ha="center",
                fontsize=8,
                color=estilo.get("color", "black")
            )

    # Configurações do gráfico
    plt.title("Hit Ratio por Capacidade do Cache — FIFO vs LRU vs LFU",
              fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Capacidade do Cache (número de itens)", fontsize=12)
    plt.ylabel("Hit Ratio (%)", fontsize=12)
    plt.legend(title="Política", fontsize=11)
    plt.xticks(capacidades)
    plt.ylim(0, 105)
    plt.tight_layout()

    caminho = os.path.join(pasta_saida, "grafico_comparativo.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close()
    return caminho


def gerar_graficos_individuais(resultados: dict, pasta_saida: str = "results") -> list:
    """
    Gera um gráfico individual para cada política.

    Retorna lista com os caminhos dos arquivos gerados.
    """
    os.makedirs(pasta_saida, exist_ok=True)

    cores = {"FIFO": "#E74C3C", "LRU": "#2980B9", "LFU": "#27AE60"}
    arquivos = []

    for politica, pontos in resultados.items():
        capacidades = [p[0] for p in pontos]
        hit_ratios  = [p[1] for p in pontos]

        plt.figure(figsize=(8, 5))
        plt.style.use("seaborn-v0_8-whitegrid")

        plt.bar(
            [str(c) for c in capacidades],
            hit_ratios,
            color=cores.get(politica, "#555"),
            edgecolor="white",
            width=0.5,
            label=politica
        )

        # Valor no topo de cada barra
        for i, hr in enumerate(hit_ratios):
            plt.text(i, hr + 1, f"{hr:.1f}%", ha="center", fontsize=10, fontweight="bold")

        plt.title(f"Hit Ratio por Capacidade — Política {politica}",
                  fontsize=13, fontweight="bold")
        plt.xlabel("Capacidade do Cache (itens)", fontsize=11)
        plt.ylabel("Hit Ratio (%)", fontsize=11)
        plt.ylim(0, 115)
        plt.tight_layout()

        caminho = os.path.join(pasta_saida, f"grafico_{politica.lower()}.png")
        plt.savefig(caminho, dpi=150, bbox_inches="tight")
        plt.close()
        arquivos.append(caminho)

    return arquivos
