# OpenMP na Prática

Trabalho para a cadeira de Introdução ao Processamento Paralelo e Distribuído do curso de Ciência da Computação da Universidade Federal de Pelotas.

## Integrantes:
- Alan Souza dos Santos (Tarefa C)
- Lucas Bayer de Araújo (Tarefa D)
- Rodrigo de Laforet Padilha Raupp (Tarefa A)

## Estrutura do Repositório

openmp/
├── tarefaA/
│   ├── src/
│   │   └── omp/
│   │       └── tarefaA.c
│   ├── .gitignore
│   ├── Makefile
│   ├── Reprodutibilidade.md
│   ├── Resultados.md
│   ├── run.sh
│   └── tarefaA.md
│
├── tarefaC/
│   ├── results/
│   │   ├── plots/
│   │   │   ├── eficiencia.png
│   │   │   ├── escalabilidade.png
│   │   │   ├── speedup_vs_tamanho.png
│   │   │   ├── tempo_vs_tamanho.png
│   │   │   └── variancia.png
│   │   └── resultados.csv
│   │
│   ├── src/
│   │   ├── omp/
│   │   │   ├── saxpy_parallel_simd
│   │   │   └── saxpy_simd.c
│   │   └── seq/
│   │       └── saxpy_seq.c
│   │
│   ├── .gitignore
│   ├── Makefile
│   ├── plot.py
│   ├── README.md
│   ├── REPRODUCIBILIDADE.md
│   ├── RESULTADOS.md
│   ├── run.sh
│   ├── saxpy_parallel_simd
│   ├── saxpy_seq
│   └── saxpy_simd
│
├── tarefaD/
│   ├── bin/
│   │   └── omp_D
│   │
│   ├── plots_D/
│   │   ├── speedup_vs_threads_N_*
│   │   ├── tempo_vs_threads_N_*
│   │
│   ├── src/
│   │   └── omp/
│   │       └── tarefaD.c
│   │
│   ├── Makefile
│   ├── plot.py
│   ├── REPRODUCIBILIDADE.md
│   ├── RESULTADOS.md
│   ├── resultados_D.csv
│   ├── run.sh
│   └── .gitignore
│
├── .gitignore
└── README.md
