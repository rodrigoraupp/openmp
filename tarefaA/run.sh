#!/bin/bash

# --- Configurações Básicas ---
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
if [ ! -f "$CSV_FILE" ]; then
    echo "variante,tamanho_chunk,N,K,numero_threads,tempo" > "$CSV_FILE"
fi

# --- Definição dos Parâmetros ---
VARIANTS=(1 2 3)
CHUNKS=(1 4 16 64)
NS=(100000 500000 1000000)
KS=(20 24 28)
THREADS=(1 2 4 8 16)
REPETICOES=5

echo "--- Iniciando Bateria de Testes ---"
echo "Saída será gravada em: $CSV_FILE"

# --- Loops de Execução ---

for v in "${VARIANTS[@]}"; do
    
    # Lógica para Otimizar Variante 1:
    # Se for variante 1 (Static), não variamos o chunk (usamos 1 fixo).
    # Se for 2 ou 3 (Dynamic/Guided), usamos a lista completa de chunks.
    if [ "$v" -eq 1 ]; then
        CHUNKS_ATUAIS=(1)
    else
        CHUNKS_ATUAIS=("${CHUNKS[@]}")
    fi

    for c in "${CHUNKS_ATUAIS[@]}"; do
        for n in "${NS[@]}"; do
            for k in "${KS[@]}"; do
                for t in "${THREADS[@]}"; do
                    
                    # Loop de Repetições (Média)
                    for ((r=1; r<=REPETICOES; r++)); do
                        
                        # Feedback visual no terminal para você não achar que travou
                        echo "[Executando] Var:$v | Chunk:$c | N:$n | K:$k | Threads:$t | Rep:$r/$REPETICOES"

                        # Executa o programa
                        # Ordem: variante tamanho_chunk N K numero_threads
                        OUTPUT=$($EXEC $v $c $n $k $t)

                        # Verifica se houve saída e salva no CSV
                        if [ -n "$OUTPUT" ]; then
                            echo "$OUTPUT" >> "$CSV_FILE"
                        else
                            echo "ALERTA: Execução retornou vazio ou falhou!"
                        fi
                        
                    done # Fim Repetições
                    
                done # Fim Threads
            done # Fim K
        done # Fim N
    done # Fim Chunk
done # Fim Variante

echo "--- Fim dos Experimentos ---"
echo "Verifique os resultados em $CSV_FILE"