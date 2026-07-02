# ============================================================
# POLÍTICA DE SUBSTITUIÇÃO: LRU (Least Recently Used)
#
# O item que foi acessado há MAIS TEMPO é o primeiro a ser
# removido quando o cache está cheio.
# ============================================================

from collections import OrderedDict


class CacheLRU:
    """
    Implementação da política LRU.
    Usa um OrderedDict para manter a ordem de uso recente.
    O item no INÍCIO do OrderedDict é o menos recentemente usado.
    """

    def __init__(self, capacidade: int):
        # Capacidade máxima do cache
        self.capacidade = capacidade

        # OrderedDict mantém a ordem de inserção/acesso
        # Chave: item_id | Valor: True (apenas marcador)
        self.cache = OrderedDict()

        # Contadores de desempenho
        self.hits = 0
        self.misses = 0

    def acessar(self, item_id: int) -> bool:
        """
        Processa um acesso ao item informado.
        Retorna True se foi HIT, False se foi MISS.
        """
        # Verifica se o item já está no cache (HIT)
        if item_id in self.cache:
            self.hits += 1
            # Move o item para o FINAL (mais recentemente usado)
            self.cache.move_to_end(item_id)
            return True  # HIT

        # MISS: item não está no cache
        self.misses += 1

        # Se o cache está cheio, remove o menos recentemente usado
        # (o item no INÍCIO do OrderedDict)
        if len(self.cache) >= self.capacidade:
            self.cache.popitem(last=False)  # Remove o primeiro (LRU)

        # Insere o novo item no final (mais recente)
        self.cache[item_id] = True

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
            "politica": "LRU",
            "capacidade": self.capacidade,
            "total_acessos": self.hits + self.misses,
            "hits": self.hits,
            "misses": self.misses,
            "hit_ratio": self.hit_ratio(),
        }
