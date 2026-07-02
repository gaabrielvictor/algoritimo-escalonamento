#!/usr/bin/env python3
# ============================================================
# GERADOR DE TRACE CSV
# Gera um arquivo trace.csv com 10.000 acessos simulados.
#
# O trace simula um padrão realista com:
#   - Localidade temporal: alguns itens são muito acessados
#   - Localidade espacial: acessos tendem a ocorrer em grupos
#   - Itens de 1 a 300 (simula um catálogo de produtos/páginas)
#
# Uso:
#   python gerar_trace.py
# ============================================================

import csv
import random


def gerar_trace(caminho: str = "trace.csv", total_acessos: int = 10000):
    """
    Gera um arquivo CSV com sequência de acessos simulada.

    A distribuição usa:
      - 20% dos itens respondem por ~80% dos acessos (Lei de Pareto)
      - Itens "quentes": IDs de 1 a 60 (alta frequência)
      - Itens "frios"  : IDs de 61 a 300 (baixa frequência)
    """
    random.seed(42)  # Semente fixa para reprodutibilidade

    # Universo de itens
    itens_quentes = list(range(1, 61))    # 60 itens populares
    itens_frios   = list(range(61, 301))  # 240 itens raros

    acessos = []

    for _ in range(total_acessos):
        # 75% de chance de acessar um item quente
        if random.random() < 0.75:
            item = random.choice(itens_quentes)
        else:
            item = random.choice(itens_frios)
        acessos.append(item)

    # Salva no arquivo CSV
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["item_id"])      # Cabeçalho obrigatório
        for item in acessos:
            writer.writerow([item])

    print(f"  ✔ Arquivo gerado: {caminho}")
    print(f"  ✔ Total de acessos: {total_acessos}")
    print(f"  ✔ Itens únicos no universo: 300")


if __name__ == "__main__":
    print("\n  Gerando trace.csv...")
    gerar_trace()
    print()
