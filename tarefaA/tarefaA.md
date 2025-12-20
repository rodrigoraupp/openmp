# Tarefa A - Laço irregular e políticas de schedule

## Configurações
- Kernel: para `i = 0..N-1`, compute `fib(i % K)` e grave em `v[i]` usando fib custosa sem memoização.
- Variante 1: `#pragma omp parallel for schedule(static)`
- Variante 2: `schedule(dynamic,chunk)` com chunk ∈ {1,4,16,64}
- Variante 3: `schedule(guided,chunk)` com chunk ∈ {1,4,16,64}
- Se houver dois laços paralelos em sequência, use uma única região parallel e dois for internos.

## Parâmetros

- Variantes ∈ {1, 2, 3}
- N ∈ {100000, 500000, 1000000}     
- K ∈ {20, 24, 28}     
- Threads: {1, 2, 4, 8, 16}   