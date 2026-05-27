# ============================================================
# ALGORITMO DE ESCALONAMENTO: ROUND ROBIN
# Disciplina: Sistemas Operacionais
#
# Cenário simulado:
#   - Processo 1 (P1): 10 unidades de tempo
#   - Processo 2 (P2):  5 unidades de tempo
#   - Processo 3 (P3):  8 unidades de tempo
#   - Quantum fixo   :  2 unidades de tempo
# ============================================================


# ----------------------------------------------------------
# CONFIGURAÇÃO DOS PROCESSOS
# Cada processo é um dicionário com:
#   "nome"      -> identificação do processo
#   "restante"  -> quanto tempo ainda falta executar
# ----------------------------------------------------------
processos = [
    {"nome": "P1", "restante": 10},
    {"nome": "P2", "restante": 5},
    {"nome": "P3", "restante": 8},
]

# Quantum: fatia de tempo que cada processo recebe por vez
QUANTUM = 2


# ----------------------------------------------------------
# FUNÇÃO PRINCIPAL: simula o Round Robin
# ----------------------------------------------------------
def round_robin(lista_processos, quantum):

    # Cria a fila de execução com todos os processos
    # (usamos uma lista simples para facilitar a leitura)
    fila = list(lista_processos)

    tempo_total = 0   # Contador de tempo total decorrido
    ciclo = 1         # Número do ciclo atual

    print("=" * 45)
    print("      SIMULAÇÃO - ROUND ROBIN")
    print(f"      Quantum = {quantum} unidades de tempo")
    print("=" * 45)
    print()

    # O loop continua enquanto ainda houver processos na fila
    while fila:

        print(f"--- Ciclo {ciclo} ---")

        # Mostra quais processos ainda estão na fila
        print("Fila atual: ", end="")
        for p in fila:
            print(f"{p['nome']}({p['restante']}ut)", end="  ")
        print("\n")

        # Pega o PRIMEIRO processo da fila (o próximo a executar)
        processo = fila.pop(0)

        # Calcula quanto tempo vai executar neste ciclo:
        # Se o restante for menor que o quantum, executa só o restante
        # Exemplo: processo com 1ut restante e quantum=2 → executa 1ut
        tempo_executado = min(quantum, processo["restante"])

        # Desconta o tempo executado do tempo restante do processo
        processo["restante"] -= tempo_executado

        # Soma ao tempo total da CPU
        tempo_total += tempo_executado

        print(f"  Executando : {processo['nome']}")
        print(f"  Tempo usado: {tempo_executado} unidade(s)")
        print(f"  Restante   : {processo['restante']} unidade(s)")

        # Verifica se o processo terminou (tempo restante zerado)
        if processo["restante"] == 0:
            print(f"  ✔ {processo['nome']} FINALIZADO!")
        else:
            # Processo ainda não terminou → volta para o FINAL da fila
            print(f"  ↩ {processo['nome']} volta para o final da fila.")
            fila.append(processo)

        print()
        ciclo += 1

    # Todos os processos foram concluídos
    print("=" * 45)
    print("  Todos os processos foram concluídos!")
    print(f"  Tempo total de CPU utilizado: {tempo_total} unidades")
    print("=" * 45)


# ----------------------------------------------------------
# EXECUÇÃO DO PROGRAMA
# ----------------------------------------------------------
round_robin(processos, QUANTUM)