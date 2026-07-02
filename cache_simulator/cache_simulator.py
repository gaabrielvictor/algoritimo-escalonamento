#!/usr/bin/env python3
# ============================================================
# SIMULADOR DE MEMÓRIA CACHE — Arquivo Principal (main)
# Disciplina: Sistemas Operacionais  |  UNIFACISA
#
# Uso:
#   python cache_simulator.py --input trace.csv --policy lru --capacity 100
#
# Flags obrigatórias:
#   --input     : caminho para o arquivo CSV com os acessos
#   --policy    : política de substituição (fifo | lru | lfu)
#   --capacity  : capacidade máxima do cache (número inteiro > 0)
# ============================================================

import argparse
import sys

# Importa as políticas do módulo policies/
from policies import CacheFIFO, CacheLRU, CacheLFU

# Importa utilitários do módulo utils/
from utils import ler_trace, executar_simulacao, exibir_resultado


# ----------------------------------------------------------
# Mapeamento de nome de política → classe correspondente
# ----------------------------------------------------------
POLITICAS = {
    "fifo": CacheFIFO,
    "lru":  CacheLRU,
    "lfu":  CacheLFU,
}


def configurar_argumentos() -> argparse.Namespace:
    """
    Configura e faz o parse dos argumentos de linha de comando.
    Retorna o objeto com os argumentos já validados.
    """
    parser = argparse.ArgumentParser(
        description="Simulador de Memória Cache — FIFO, LRU e LFU",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--input",
        required=True,
        metavar="ARQUIVO.csv",
        help="Arquivo CSV com a sequência de acessos (coluna: item_id)"
    )
    parser.add_argument(
        "--policy",
        required=True,
        choices=["fifo", "lru", "lfu"],
        metavar="POLÍTICA",
        help="Política de substituição: fifo | lru | lfu"
    )
    parser.add_argument(
        "--capacity",
        required=True,
        type=int,
        metavar="N",
        help="Capacidade máxima do cache (número de itens)"
    )

    args = parser.parse_args()

    # Validação extra: capacidade deve ser positiva
    if args.capacity <= 0:
        parser.error("--capacity deve ser um número inteiro positivo.")

    return args


def main():
    """
    Função principal: coordena leitura, simulação e exibição de resultados.
    """
    # 1. Lê os argumentos da linha de comando
    args = configurar_argumentos()

    print()
    print("=" * 45)
    print("   SIMULADOR DE MEMÓRIA CACHE")
    print("=" * 45)
    print(f"  Arquivo  : {args.input}")
    print(f"  Política : {args.policy.upper()}")
    print(f"  Capacidade: {args.capacity} itens")
    print("=" * 45)
    print()

    # 2. Lê o arquivo CSV e obtém a sequência de acessos
    try:
        acessos = ler_trace(args.input)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[ERRO] {erro}")
        sys.exit(1)

    print(f"  Total de acessos carregados: {len(acessos)}")
    print()

    # 3. Instancia a política de cache escolhida
    ClasseCache = POLITICAS[args.policy]
    cache = ClasseCache(capacidade=args.capacity)

    # 4. Executa a simulação
    stats = executar_simulacao(cache, acessos)

    # 5. Exibe os resultados no terminal
    exibir_resultado(stats)


# Ponto de entrada: garante que main() só é chamado diretamente
if __name__ == "__main__":
    main()
