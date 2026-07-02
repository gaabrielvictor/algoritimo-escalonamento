# ============================================================
# POLÍTICA DE SUBSTITUIÇÃO: LFU (Least Frequently Used)
#
# O item que foi acessado com MENOR FREQUÊNCIA é o primeiro
# a ser removido quando o cache está cheio.
# Em caso de empate na frequência, remove o mais antigo (FIFO).
# ============================================================

from collections import defaultdict


class CacheLFU:
    """
    Implementação da política LFU.
    Mantém contagem de frequência de acesso para cada item.
    Em empate de frequência, o item mais antigo é removido.
    """

    def __init__(self, capacidade: int):
        # Capacidade máxima do cache
        self.capacidade = capacidade

        # Dicionário: item_id → frequência de acesso
        self.frequencia = {}

        # Dicionário: item_id → ordem de chegada (para desempate)
        self.ordem_chegada = {}

        # Contador global de inserções (usado para desempate FIFO)
        self.contador_insercao = 0

        # Contadores de desempenho
        self.hits = 0
        self.misses = 0

    def acessar(self, item_id: int) -> bool:
        """
        Processa um acesso ao item informado.
        Retorna True se foi HIT, False se foi MISS.
        """
        # Verifica se o item já está no cache (HIT)
        if item_id in self.frequencia:
            self.hits += 1
            # Incrementa a frequência de acesso do item
            self.frequencia[item_id] += 1
            return True  # HIT

        # MISS: item não está no cache
        self.misses += 1

        # Se o cache está cheio, remove o item menos frequente
        if len(self.frequencia) >= self.capacidade:
            # Encontra o item com menor frequência
            # Em caso de empate, remove o que chegou primeiro (menor ordem)
            item_remover = min(
                self.frequencia.keys(),
                key=lambda x: (self.frequencia[x], self.ordem_chegada[x])
            )
            del self.frequencia[item_remover]
            del self.ordem_chegada[item_remover]

        # Insere o novo item com frequência 1
        self.frequencia[item_id] = 1
        self.ordem_chegada[item_id] = self.contador_insercao
        self.contador_insercao += 1

        return False  # MISS

    def hit_ratio(self) -> float:
        """Calcula e retorna o hit ratio em porcentagem."""
        total = self.hits + self.misses
        if total == 0:
            return 0.0
        return (self.hits / total) * 100

    def estatisticas(self) -> dict:
        """Retorna um dicionário com todas as estatísticas."""
        return {
            "politica": "LFU",
            "capacidade": self.capacidade,
            "total_acessos": self.hits + self.misses,
            "hits": self.hits,
            "misses": self.misses,
            "hit_ratio": self.hit_ratio(),
        }
