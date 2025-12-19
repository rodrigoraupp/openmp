#!/bin/bash

# Nome do executável OpenMP
EXE="./bin/omp_D"

# Arquivo CSV de saída 
OUTPUT_FILE="resultados_D.csv"

# --- Matriz de Parâmetros ---
N_VALUES="100000 500000 1000000"
THREAD_VALUES="1 2 4 8 16"
REPETITIONS=5

# 1. Cria o cabeçalho do arquivo CSV
echo "N;Threads;Repeticao;Tempo_Ingenua;Tempo_Arrumada" > $OUTPUT_FILE

# 2. Laço para o Tamanho do Problema (N)
for N in $N_VALUES; do

    # 3. Laço para o Número de Threads
    for T in $THREAD_VALUES; do

        # 4. Laço para Repetições (Média de 5 execuções)
        for R in $(seq 1 $REPETITIONS); do

            RESULT=$( $EXE $N $T | grep "Tempo" )

            RAW_DATA=$($EXE $N $T | grep "RESULTADO_CSV" | awk -F';' '{print $4 ";" $5}')
            # Grava no CSV: N;Threads;R;Tempo_Ingenua;Tempo_Arrumada
            echo "$N;$T;$R;$RAW_DATA" >> $OUTPUT_FILE

            echo "Executado N=$N, T=$T, Rep=$R"
        done
    done
done

echo "Matriz de experimentos concluída. Resultados em $OUTPUT_FILE"
