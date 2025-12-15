#!/usr/bin/bash

mkdir -p results

OUTPUT="results/resultados.csv"

echo "versao,n,threads,tempo_ms,checksum,repeticao" > $OUTPUT

SIZES=(100000 500000 1000000)
THREADS=(1 2 4 8 16)
REPETICOES=5

echo "=== Iniciando experimentos da Tarefa C - SAXPY ==="
echo ""

echo "Executando versão sequencial..."
for n in "${SIZES[@]}"; do
    echo "  N = $n"
    for rep in $(seq 1 $REPETICOES); do
        result=$(./saxpy_seq $n)
        echo "$result,$rep" >> $OUTPUT
    done
done

echo ""
echo "Executando versão SIMD..."
for n in "${SIZES[@]}"; do
    echo "  N = $n"
    for rep in $(seq 1 $REPETICOES); do
        result=$(./saxpy_simd $n)
        echo "$result,$rep" >> $OUTPUT
    done
done

echo ""
echo "Executando versão Parallel + SIMD..."
for n in "${SIZES[@]}"; do
    for t in "${THREADS[@]}"; do
        echo "  N = $n, Threads = $t"
        for rep in $(seq 1 $REPETICOES); do
            result=$(./saxpy_parallel_simd $n $t)
            echo "$result,$rep" >> $OUTPUT
        done
    done
done

echo ""
echo "=== Experimentos concluídos ==="
echo "Resultados salvos em: $OUTPUT"