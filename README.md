# OpenMP na Prática

Trabalho para a cadeira de Introdução ao Processamento Paralelo e Distribuído do curso de Ciência da Computação da Universidade Federal de Pelotas.

## Integrantes:
- Alan Souza dos Santos (Tarefa C)
- Lucas Bayer de Araújo (Tarefa D)
- Rodrigo de Laforet Padilha Raupp (Tarefa A)

## Estrutura do Repositório

    .
    ├── README.md
    ├── tarefaA
    │   ├── Makefile
    │   ├── plot.py
    │   ├── REPRODUCIBILIDADE.md
    │   ├── RESULTADOS.md
    │   ├── results
    │   │   ├── analise_v1_static.png
    │   │   ├── analise_v2_dynamic.png
    │   │   ├── analise_v3_guided.png
    │   │   └── experimentos.csv
    │   ├── run.sh
    │   ├── src
    │   │   └── omp
    │   │       └── tarefaA.c
    │   └── tarefaA.md
    ├── tarefaC
    │   ├── Makefile
    │   ├── plot.py
    │   ├── README.md
    │   ├── REPRODUCIBILIDADE.md
    │   ├── RESULTADOS.md
    │   ├── results
    │   │   ├── plots
    │   │   │   ├── eficiencia.png
    │   │   │   ├── escalabilidade.png
    │   │   │   ├── speedup_vs_tamanho.png
    │   │   │   ├── tempo_vs_tamanho.png
    │   │   │   └── variancia.png
    │   │   └── resultados.csv
    │   ├── run.sh
    │   └── src
    │       ├── omp
    │       │   ├── saxpy_parallel_simd.c
    │       │   └── saxpy_simd.c
    │       └── seq
    │           └── saxpy_seq.c
    └── tarefaD
        ├── bin
        │   └── omp_D
        ├── Makefile
        ├── plot.py
        ├── plots_D
        │   ├── speedup_vs_threads_N_1000000.png
        │   ├── speedup_vs_threads_N_100000.png
        │   ├── speedup_vs_threads_N_500000.png
        │   ├── tempo_vs_threads_N_1000000.png
        │   ├── tempo_vs_threads_N_100000.png
        │   └── tempo_vs_threads_N_500000.png
        ├── REPRODUCIBILIDADE.md
        ├── resultados_D.csv
        ├── RESULTADOS.md
        ├── run.sh
        └── src
            └── omp
                └── tarefaD.c
