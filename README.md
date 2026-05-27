# 🔄 Simulador Round Robin - Escalonamento de Processos

[![Sistemas Operacionais](https://img.shields.io/badge/Disciplina-Sistemas_Operacionais-blue.svg)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.x-green.svg)](https://python.org)
[![Algoritmo](https://img.shields.io/badge/Algoritmo-Round_Robin-orange.svg)](https://pt.wikipedia.org/wiki/Round_robin_(ci%C3%AAncia_da_computa%C3%A7%C3%A3o))

> ⚡ **"Justiça no compartilhamento da CPU, um quantum de cada vez!"**

---

## 🎯 Visão Geral

Este projeto implementa uma **simulação didática** do algoritmo de escalonamento **Round Robin (RR)** , um dos mais importantes e justos algoritmos utilizados em sistemas operacionais modernos.

### 📊 Cenário Simulado

| Processo | Tempo Total (ut*) | Quantum |
|----------|-------------------|---------|
| **P1**   | 10 unidades       | 2 ut    |
| **P2**   | 5 unidades        | 2 ut    |
| **P3**   | 8 unidades        | 2 ut    |

> *ut = unidades de tempo (ex: milissegundos, ticks de CPU)

---

## 🧠 Como Funciona o Round Robin?

```mermaid
graph LR
    A[Fila de Prontos] --> B[Pega 1º processo]
    B --> C[Executa por 1 quantum]
    C --> D{Terminou?}
    D -->|Sim| E[Processo finalizado]
    D -->|Não| F[Volta ao final da fila]
    F --> A
    E --> A
