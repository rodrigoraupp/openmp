# --- Variáveis ---
CC = gcc
CFLAGS = -Wall -O3
OMP_FLAGS = -fopenmp
LDFLAGS = -lm

# --- Arquivos ---
# Ajuste o caminho se seu arquivo tiver outro nome
SRC = src/tarefaA/tarefaA.c
EXEC = tarefaA

# --- Regra Padrão ---
all: $(EXEC)

# --- Compilação ---
# Gera um único executável com suporte a OpenMP habilitado
$(EXEC): $(SRC)
	@echo "Compilando Tarefa A..."
	$(CC) $(CFLAGS) $(OMP_FLAGS) $(SRC) -o $(EXEC) $(LDFLAGS)

# --- Execução via Script ---
# Garante que está compilado e chama o seu shell script
run: all
	@chmod +x runtarefaA.sh
	./runtarefaA.sh

# --- Limpeza ---
clean:
	rm -f $(EXEC)