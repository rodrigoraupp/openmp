# --- Variáveis de Configuração ---
CC = gcc
CFLAGS = -O3 -Wall
OMP_FLAGS = -fopenmp
# Diretórios
SRC_DIR = src/omp
BIN_DIR = bin
# Arquivo fonte e executáveis
SRC = $(SRC_DIR)/tarefaD.c
EXE_OMP = $(BIN_DIR)/omp_D
EXE_SEQ = $(BIN_DIR)/seq_D

# --- Alvos Principais ---

# Alvo padrão: compila tudo
all: $(EXE_OMP) $(EXE_SEQ)

# 1. Alvo 'omp': Compila com suporte a OpenMP
omp: $(EXE_OMP)

$(EXE_OMP): $(SRC)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(OMP_FLAGS) $(SRC) -o $(EXE_OMP)
	@echo "✔ Compilado: $(EXE_OMP) (OpenMP)"

# 2. Alvo 'seq': Compila sem OpenMP (ignora os pragmas)
seq: $(EXE_SEQ)

$(EXE_SEQ): $(SRC)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(SRC) -o $(EXE_SEQ)
	@echo "✔ Compilado: $(EXE_SEQ) (Sequencial)"

# 3. Alvo 'run': Executa o script de experimentos
run: $(EXE_OMP)
	@chmod +x run.sh
	./run.sh

# 4. Alvo 'plot': Executa o script de geração de gráficos
plot:
	@python3 plot.py

# Limpeza
clean:
	rm -rf $(BIN_DIR) *.csv plots_D/
	@echo "🧹 Limpeza concluída."

.PHONY: all omp seq run plot clean
