# 🗄️ Simulador de Memória Cache

> **Disciplina:** Sistemas Operacionais — UNIFACISA  
> **Fase 2 — Simulação e Experimentos com Políticas de Substituição de Cache**

Simulador de memória cache em Python que implementa e compara as políticas de substituição **FIFO**, **LRU** e **LFU**, avaliando o desempenho através do *hit ratio* em diferentes capacidades de cache.

---

## 📁 Estrutura do Projeto

```
cache_simulator/
│
├── cache_simulator.py     ← Ponto de entrada principal (main)
├── experimentos.py        ← Executa os 3 experimentos e gera gráficos
├── gerar_trace.py         ← Gera o arquivo trace.csv (10.000 acessos)
├── trace.csv              ← Trace de acessos gerado
│
├── policies/              ← Módulo: políticas de substituição
│   ├── __init__.py
│   ├── fifo.py            ← Política FIFO (First-In First-Out)
│   ├── lru.py             ← Política LRU (Least Recently Used)
│   └── lfu.py             ← Política LFU (Least Frequently Used)
│
├── utils/                 ← Módulo: utilitários
│   ├── __init__.py
│   ├── leitor_csv.py      ← Leitura do arquivo CSV
│   ├── simulador.py       ← Motor de simulação e exibição de resultados
│   └── graficos.py        ← Geração de gráficos com Matplotlib
│
└── results/               ← Gráficos gerados automaticamente
    ├── grafico_comparativo.png
    ├── grafico_fifo.png
    ├── grafico_lru.png
    └── grafico_lfu.png
```

---

## ⚙️ Requisitos

- Python **3.10** ou superior
- Biblioteca `matplotlib`
- Biblioteca `Pillow` *(opcional, para geração dos gráficos de relatório)*

### Instalação das dependências

```bash
pip install matplotlib
```

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/cache-simulator.git
cd cache-simulator
```

### 2. Gere o arquivo de trace (CSV com 10.000 acessos)

```bash
python gerar_trace.py
```

Isso cria o arquivo `trace.csv` na pasta do projeto, com 10.000 requisições simuladas a um universo de 300 itens distintos.

---

### 3. Execute uma simulação específica

```bash
python cache_simulator.py --input trace.csv --policy lru --capacity 100
```

**Flags obrigatórias:**

| Flag | Descrição | Valores aceitos |
|------|-----------|-----------------|
| `--input` | Caminho para o arquivo CSV | qualquer `.csv` com coluna `item_id` |
| `--policy` | Política de substituição | `fifo`, `lru` ou `lfu` |
| `--capacity` | Capacidade máxima do cache | número inteiro positivo |

**Exemplos:**

```bash
# FIFO com 100 itens
python cache_simulator.py --input trace.csv --policy fifo --capacity 100

# LRU com 500 itens
python cache_simulator.py --input trace.csv --policy lru --capacity 500

# LFU com 1000 itens
python cache_simulator.py --input trace.csv --policy lfu --capacity 1000
```

**Saída esperada:**

```
=============================================
   SIMULADOR DE MEMÓRIA CACHE
=============================================
  Arquivo   : trace.csv
  Política  : LRU
  Capacidade: 100 itens
=============================================

  Total de acessos carregados: 10000

=============================================
  Política  : LRU
  Capacidade: 100 itens
---------------------------------------------
  Total de acessos : 10000
  Hits             : 7317
  Misses           : 2683
  Hit Ratio        : 73.17%
=============================================
```

---

### 4. Execute todos os experimentos e gere os gráficos

```bash
python experimentos.py --input trace.csv
```

Roda automaticamente as **3 políticas × 3 capacidades** (100, 500 e 1.000 itens) e salva os gráficos na pasta `results/`.

---

## 📊 Resultados dos Experimentos

| Política | Capacidade | Hits | Misses | Hit Ratio |
|----------|-----------|------|--------|-----------|
| FIFO | 100 itens | 6.435 | 3.565 | 64,35% |
| FIFO | 500 itens | 9.700 | 300 | 97,00% |
| FIFO | 1.000 itens | 9.700 | 300 | 97,00% |
| LRU | 100 itens | 7.317 | 2.683 | 73,17% |
| LRU | 500 itens | 9.700 | 300 | 97,00% |
| LRU | 1.000 itens | 9.700 | 300 | 97,00% |
| **LFU** | **100 itens** | **7.893** | **2.107** | **78,93% ✓** |
| LFU | 500 itens | 9.700 | 300 | 97,00% |
| LFU | 1.000 itens | 9.700 | 300 | 97,00% |

> O **LFU** apresentou o melhor desempenho com cache restrito (100 itens), aproveitando a concentração de acessos em poucos itens populares.

---

## 📄 Formato do arquivo CSV

O arquivo de entrada deve conter uma coluna chamada `item_id`:

```csv
item_id
10
15
10
20
15
30
```

Cada linha representa uma requisição a um item do cache.

---

## 🧠 Sobre as Políticas

| Política | Critério de remoção | Melhor para |
|----------|---------------------|-------------|
| **FIFO** | Item inserido há mais tempo | Simplicidade de implementação |
| **LRU** | Item não acessado há mais tempo | Workloads com localidade temporal |
| **LFU** | Item acessado com menor frequência | Workloads com distribuição desigual (Pareto) |

---

## 📦 Tecnologias utilizadas

- **Python 3** — linguagem principal
- **collections** (`deque`, `OrderedDict`) — estruturas de dados para as políticas
- **csv** — leitura do trace de acessos
- **argparse** — interface de linha de comando
- **matplotlib** — geração dos gráficos
- **random** — geração do trace sintético
