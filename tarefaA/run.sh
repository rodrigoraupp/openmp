#!/bin/bash

# garante que o executável existe antes de tentar executar
if [ ! -f "./tarefaA" ]; then
    echo "Erro: Executável 'tarefaA' não encontrado. Rode 'make' primeiro."
    exit 1
fi

# um teste
./tarefaA 1 1 1000000 20 4