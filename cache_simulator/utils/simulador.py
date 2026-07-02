# ============================================================
# UTILITÁRIO: Motor de Simulação
#
# Recebe uma lista de acessos e uma instância de política de
# cache e executa a simulação completa, retornando estatísticas.
# ============================================================


def executar_simulacao(cache, acessos: list[int]) -> dict:
    """
    Executa a simulação de cache para a sequência de acessos fornecida.

    Parâmetros:
        cache   : instância de CacheFIFO, CacheLRU ou CacheLFU
        acessos : lista de item_ids representando a sequência de acessos

    Retorna:
        Dicionário com estatísticas completas da simulação.
    """
    # Processa cada acesso da sequência
    for item_id in acessos:
        cache.acessar(item_id)

    # Retorna as estatísticas ao final
    return cache.estatisticas()


def exibir_resultado(stats: dict) -> None:
    """
    Exibe no terminal os resultados formatados de uma simulação.

    Parâmetro:
        stats: dicionário retornado por estatisticas()
    """
    print("=" * 45)
    print(f"  Política  : {stats['politica']}")
    print(f"  Capacidade: {stats['capacidade']} itens")
    print("-" * 45)
    print(f"  Total de acessos : {stats['total_acessos']}")
    print(f"  Hits             : {stats['hits']}")
    print(f"  Misses           : {stats['misses']}")
    print(f"  Hit Ratio        : {stats['hit_ratio']:.2f}%")
    print("=" * 45)
    print()
