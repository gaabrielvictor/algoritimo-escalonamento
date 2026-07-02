# ============================================================
# POLÍTICA DE SUBSTITUIÇÃO: FIFO (First-In First-Out)
#
# O item que chegou PRIMEIRO ao cache é o primeiro a ser
# removido quando o cache está cheio.
# ============================================================

from collections import deque


class CacheFIFO:
    """
    Implementação da política FIFO.
    Usa uma fila (deque) para controlar a ordem de chegada.
    """

    def __init__(self, capacidade: int):
        # Capacidade máxima do cache (número de itens)
        self.capacidade = capacidade

        # Conjunto de itens atualmente no cache (busca O(1))
        self.cache = set()

        # Fila que registra a ordem de chegada dos itens
        self.fila_chegada = deque()

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
            return True  # HIT: item encontrado, nada a fazer

        # MISS: item não está no cache
        self.misses += 1

        # Se o cache está cheio, remove o item mais antigo (FIFO)
        if len(self.cache) >= self.capacidade:
            item_mais_antigo = self.fila_chegada.popleft()
            self.cache.discard(item_mais_antigo)

        # Insere o novo item no cache e registra sua chegada
        self.cache.add(item_id)
        self.fila_chegada.append(item_id)

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
            "politica": "FIFO",
            "capacidade": self.capacidade,
            "total_acessos": self.hits + self.misses,
            "hits": self.hits,
            "misses": self.misses,
            "hit_ratio": self.hit_ratio(),
        }
