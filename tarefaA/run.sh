#!/bin/bash

# --- Configurações ---
EXEC="./build/tarefaA"
RESULTS_DIR="./results"
CSV_FILE="$RESULTS_DIR/experimentos.csv"

# 1. Garante que o executável existe
if [ ! -f "$EXEC" ]; then
    echo "ERRO: Executável não encontrado em $EXEC."
    echo "Por favor, rode 'make' antes de executar este script."
    exit 1
fi

# 2. Cria a pasta 'results' se ela não existir
if [ ! -d "$RESULTS_DIR" ]; then
    echo "Criando diretório de resultados: $RESULTS_DIR"
    mkdir -p "$RESULTS_DIR"
fi

# 3. Cria o cabeçalho do CSV (apenas se o arquivo for novo)
# Certifique-se que este cabeçalho bate com a ordem do printf do seu C
if [ ! -f "$CSV_FILE" ]; then
    echo "variante,tamanho_chunk,N,K,numero_threads,tempo" > "$CSV_FILE"
fi

# --- Execução do Teste ---
# Parâmetros: variante=1, tamanho_chunk=1, N=1000000, K=20, numero_threads=4
PARAMS="1 1 1000000 20 4"

echo "Executando teste com parâmetros: $PARAMS"

# 4. Captura a saída e salva
# Como seu C já imprime "param,param,param,tempo", pegamos tudo direto.
OUTPUT=$($EXEC $PARAMS)

# Verifica se o output não veio vazio antes de salvar (boa prática)
if [ -n "$OUTPUT" ]; then
    echo "$OUTPUT" >> "$CSV_FILE"
    echo "Sucesso! Linha salva: $OUTPUT"
else
    echo "Aviso: O programa não retornou nada na saída padrão."
fi