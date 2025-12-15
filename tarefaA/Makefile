# --- Variáveis ---
CC = gcc
CFLAGS = -Wall -O3
OMP_FLAGS = -fopenmp
LDFLAGS = -lm

# --- Caminhos ---
# Onde está o código fonte
SRC = src/omp/tarefaA.c
# Onde vai ser gerado o executável
BUILD_DIR = build
# Nome final do executável (com o caminho)
EXEC = $(BUILD_DIR)/tarefaA

# --- Regras ---

# Regra padrão: garante que o executável seja criado
all: $(EXEC)

# Regra de Compilação
# 1. Cria a pasta build se ela não existir (mkdir -p)
# 2. Compila o código jogando a saída (-o) dentro da pasta build
$(EXEC): $(SRC)
	@echo "Criando diretório de build..."
	@mkdir -p $(BUILD_DIR)
	@echo "Compilando $(SRC)..."
	$(CC) $(CFLAGS) $(OMP_FLAGS) $(SRC) -o $(EXEC) $(LDFLAGS)

# Regra de Execução
# Chama o seu script run.sh
run: all
	@echo "Dando permissão de execução ao script..."
	@chmod +x run.sh
	@echo "Executando o script..."
	./run.sh

# Regra de Limpeza
# Apaga a pasta build inteira
clean:
	@echo "Limpando arquivos compilados..."
	rm -rf $(BUILD_DIR)