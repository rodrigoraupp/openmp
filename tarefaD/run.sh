#!/bin/bash

# Nome do executável OpenMP
EXE="./bin/omp_D"

# Arquivo CSV de saída (deve estar no formato correto para o plot.py)
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

            # Executa o programa com os parâmetros N e T
            # (Exemplo: ./bin/omp_D 1000000 4)

            # A saída do seu programa em C precisa ser formatada para fácil leitura
            # Exemplo de saída em C que facilita a captura:
            # printf("%d;%d;%f;%f\n", N, T, tempo_ing, tempo_arru);

            # Executa e captura a saída (Adaptar conforme a sua saída em C)
            # A linha abaixo é um exemplo simplificado de captura e gravação

            # EXEMPLO: Executa o programa e filtra os tempos
            RESULT=$( $EXE $N $T | grep "Tempo" )

            # Isso requer que você formate a saída em C de maneira mais limpa!
            # Vamos assumir que você mudou o printf final em C para gerar um CSV:

            # printf("%d;%d;%f;%f\n", N, T, tempo_ing, tempo_arru);
            # O código C deve imprimir o tempo e mais nada para essa linha.

            # Como a sua saída final tem muito texto (RESULTADOS), você pode
            # mudar o programa C para imprimir APENAS uma linha de resultados no final:
            # printf("RESULTADO_CSV;%d;%d;%f;%f\n", N, T, tempo_ing, tempo_arru);

            # E no shell, você faria:
            RAW_DATA=$($EXE $N $T | grep "RESULTADO_CSV" | awk -F';' '{print $4 ";" $5}')
            # Grava no CSV: N;Threads;R;Tempo_Ingenua;Tempo_Arrumada
            echo "$N;$T;$R;$RAW_DATA" >> $OUTPUT_FILE

            echo "Executado N=$N, T=$T, Rep=$R"
        done
    done
done

echo "Matriz de experimentos concluída. Resultados em $OUTPUT_FILE"
