## Descrição

Implementação de SAXPY (`y[i] = a*x[i] + y[i]`) em três versões:

1. **V1 (Sequencial)**: Implementação base
2. **V2 (SIMD)**: `#pragma omp simd`
3. **V3 (Parallel+SIMD)**: `#pragma omp parallel for simd`

**Objetivo:** Analisar ganhos e limitações de vetorização e paralelização.

---

## Estrutura

```
.
├── README.md
├── RESULTADOS.md
├── REPRODUCIBILIDADE.md
├── Makefile
├── run.sh
├── plot.py
├── src/
│   ├── seq/
│   │   └── saxpy_seq.c
│   └── omp/
│       ├── saxpy_simd.c
│       └── saxpy_parallel_simd.c
└── results/
    ├── resultados.csv
    └── plots/
```

---

## Parâmetros

- **N**: 100.000, 500.000, 1.000.000
- **Threads**: 1, 2, 4, 8, 16
- **Repetições**: 5 por configuração
- **Constante a**: 2.5

---

## Principais Resultados

| N         | Sequencial | SIMD  | Parallel 8T | Melhor     |
|-----------|------------|-------|-------------|------------|
| 100.000   | 0.075 ms   | 0.081 | 9.025       | Sequencial |
| 500.000   | 1.464 ms   | 1.118 | 3.488       | SIMD       |
| 1.000.000 | 2.684 ms   | 2.184 | 1.636       | Parallel   |

**Speedup SIMD:** 1.23-1.31x  
**Speedup Parallel (8T, N=1M):** 1.64x  

**Conclusão:** SIMD eficaz para arrays médios. Paralelização só compensa para N > 1M devido a overhead de threads.

---

## Documentação Completa

- **RESULTADOS.md**: Tabelas, gráficos e análise detalhada
- **REPRODUCIBILIDADE.md**: Informações de ambiente (SO, compilador, CPU, flags)
