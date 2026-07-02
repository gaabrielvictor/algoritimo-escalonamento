#!/usr/bin/env python3
# ============================================================
# EXPERIMENTOS — Parte 2 do Projeto
# Disciplina: Sistemas Operacionais  |  UNIFACISA
#
# Executa automaticamente os experimentos com as três políticas
# e três capacidades distintas, gerando gráficos comparativos.
#
# Uso:
#   python experimentos.py --input trace.csv
# ============================================================

import argparse
import sys
import os

from policies import CacheFIFO, CacheLRU, CacheLFU
from utils import ler_trace, executar_simulacao, exibir_resultado
from utils import gerar_grafico_comparativo, gerar_graficos_individuais

# ----------------------------------------------------------
# Configuração dos experimentos
# Capacidades testadas conforme orientação do projeto
# ----------------------------------------------------------
CAPACIDADES = [100, 500, 1000]

POLITICAS = {
    "FIFO": CacheFIFO,
    "LRU":  CacheLRU,
    "LFU":  CacheLFU,
}


def executar_experimentos(acessos: list[int]) -> dict:
    """
    Executa todos os experimentos (3 políticas × 3 capacidades).

    Retorna:
        Dicionário no formato:
        { "FIFO": [(100, hr), (500, hr), (1000, hr)], ... }
    """
    resultados = {politica: [] for politica in POLITICAS}

    print("\n" + "=" * 55)
    print("  EXPERIMENTOS — FIFO vs LRU vs LFU")
    print("=" * 55)

    for politica, ClasseCache in POLITICAS.items():
        print(f"\n  Política: {politica}")
        print("  " + "-" * 45)

        for capacidade in CAPACIDADES:
            # Cria uma instância nova para cada experimento
            cache = ClasseCache(capacidade=capacidade)
            stats = executar_simulacao(cache, acessos)

            hr = stats["hit_ratio"]
            resultados[politica].append((capacidade, hr))

            print(
                f"  Cap={capacidade:5d} | "
                f"Hits={stats['hits']:6d} | "
                f"Misses={stats['misses']:6d} | "
                f"Hit Ratio={hr:.2f}%"
            )

    return resultados


def main():
    parser = argparse.ArgumentParser(
        description="Experimentos do Simulador de Cache — Parte 2"
    )
    parser.add_argument(
        "--input",
        required=True,
        metavar="ARQUIVO.csv",
        help="Arquivo CSV com a sequência de acessos (coluna: item_id)"
    )
    parser.add_argument(
        "--output",
        default="results",
        metavar="PASTA",
        help="Pasta de saída para os gráficos (padrão: results/)"
    )
    args = parser.parse_args()

    # Lê o trace de acessos
    try:
        acessos = ler_trace(args.input)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[ERRO] {erro}")
        sys.exit(1)

    print(f"\n  Arquivo carregado: {args.input}")
    print(f"  Total de acessos : {len(acessos)}")

    # Executa os experimentos
    resultados = executar_experimentos(acessos)

    # Gera os gráficos
    print("\n" + "=" * 55)
    print("  Gerando gráficos...")

    caminho_comp = gerar_grafico_comparativo(resultados, args.output)
    caminhos_ind = gerar_graficos_individuais(resultados, args.output)

    print(f"  ✔ Gráfico comparativo: {caminho_comp}")
    for c in caminhos_ind:
        print(f"  ✔ Gráfico individual : {c}")

    print("\n  Experimentos concluídos com sucesso!")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
