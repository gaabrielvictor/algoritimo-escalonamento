# ============================================================
# UTILITÁRIO: Leitura do arquivo CSV de trace de acessos
#
# O arquivo CSV deve conter uma coluna chamada "item_id".
# Cada linha representa uma requisição a um item do cache.
# ============================================================

import csv
import os


def ler_trace(caminho_csv: str) -> list[int]:
    """
    Lê o arquivo CSV e retorna uma lista de item_ids (inteiros).

    Parâmetro:
        caminho_csv: caminho para o arquivo .csv

    Retorna:
        Lista de inteiros representando a sequência de acessos.

    Lança:
        FileNotFoundError se o arquivo não existir.
        ValueError se a coluna 'item_id' não for encontrada.
    """
    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")

    acessos = []

    with open(caminho_csv, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        # Verifica se a coluna obrigatória existe
        if "item_id" not in leitor.fieldnames:
            raise ValueError(
                f"O CSV deve conter a coluna 'item_id'. "
                f"Colunas encontradas: {leitor.fieldnames}"
            )

        for linha in leitor:
            try:
                # Converte o valor para inteiro e adiciona à lista
                acessos.append(int(linha["item_id"]))
            except ValueError:
                # Ignora linhas com valores inválidos (não numéricos)
                continue

    return acessos
