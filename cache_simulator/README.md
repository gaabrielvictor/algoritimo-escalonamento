# Simulador de Memória Cache

**Disciplina:** Sistemas Operacionais — UNIFACISA  
**Fase 2 do Projeto**

Simulador de cache em Python capaz de avaliar o desempenho das políticas de substituição **FIFO**, **LRU** e **LFU**, utilizando traces de acesso fornecidos em arquivos CSV.

---

## Estrutura do Projeto

```
cache_simulator/
│
├── cache_simulator.py   ← Arquivo principal (main) — execução por flags
├── experimentos.py      ← Roda os 3 experimentos e gera os gráficos
├── gerar_trace.py       ← Gera o arquivo trace.csv com 10.000 acessos
├── trace.csv            ← Trace de acessos gerado (10.000 linhas)
│
├── policies/            ← Módulo com as políticas de substituição
│   ├── __init__.py
│   ├── fifo.py          ← Política FIFO (First-In First-Out)
│   ├── lru.py           ← Política LRU (Least Recently Used)
│   └── lfu.py           ← Política LFU (Least Frequently Used)
│
├── utils/               ← Módulo com utilitários
│   ├── __init__.py
│   ├── leitor_csv.py    ← Leitura do arquivo CSV
│   ├── simulador.py     ← Motor de simulação e exibição de resultados
│   └── graficos.py      ← Geração de gráficos com Matplotlib
│
└── results/             ← Pasta criada automaticamente com os gráficos
    ├── grafico_comparativo.png
    ├── grafico_fifo.png
    ├── grafico_lru.png
    └── grafico_lfu.png
```

---

## Requisitos

- Python 3.10 ou superior
- Biblioteca `matplotlib`

### Instalação da dependência

```bash
pip install matplotlib
```

---

## Como Executar

### 1. Gerar o arquivo de trace (CSV com 10.000 acessos)

```bash
python gerar_trace.py
```

Isso cria o arquivo `trace.csv` na pasta do projeto.

---

### 2. Simular uma política específica

```bash
python cache_simulator.py --input trace.csv --policy lru --capacity 100
```

**Flags obrigatórias:**

| Flag         | Descrição                                              |
|--------------|--------------------------------------------------------|
| `--input`    | Caminho para o arquivo CSV (deve ter coluna `item_id`) |
| `--policy`   | Política de substituição: `fifo`, `lru` ou `lfu`       |
| `--capacity` | Capacidade do cache (número inteiro positivo)          |

**Exemplos:**

```bash
# Política FIFO com cache de 100 itens
python cache_simulator.py --input trace.csv --policy fifo --capacity 100

# Política LRU com cache de 500 itens
python cache_simulator.py --input trace.csv --policy lru --capacity 500

# Política LFU com cache de 1000 itens
python cache_simulator.py --input trace.csv --policy lfu --capacity 1000
```

---

### 3. Rodar todos os experimentos e gerar os gráficos

```bash
python experimentos.py --input trace.csv
```

Os gráficos serão salvos automaticamente na pasta `results/`.

---

## Formato do arquivo CSV

O arquivo deve conter uma coluna chamada `item_id`:

```csv
item_id
10
15
10
20
15
30
```

Cada linha representa uma requisição a um item.

---

## Saída esperada (exemplo)

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
