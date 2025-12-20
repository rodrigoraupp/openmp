# --- Variáveis de Compilação ---
CC = gcc
CFLAGS = -Wall -O3
OMP_FLAGS = -fopenmp
LDFLAGS = -lm

# --- Caminhos ---
SRC = src/omp/tarefaA.c
BUILD_DIR = build
EXEC = $(BUILD_DIR)/tarefaA

# --- Configuração do Help ---
.PHONY: all run plot setup clean help

# Regra padrão (ao digitar apenas 'make')
all: $(EXEC) ## Compila o projeto e gera o executável

# --- Regras de Construção ---

$(EXEC): $(SRC)
	@echo "Criando diretório de build..."
	@mkdir -p $(BUILD_DIR)
	@echo "Compilando $(SRC)..."
	$(CC) $(CFLAGS) $(OMP_FLAGS) $(SRC) -o $(EXEC) $(LDFLAGS)

# --- Regras de Execução e Análise ---

run: all ## Executa a bateria de testes (run.sh)
	@echo "--- Iniciando Experimentos ---"
	@chmod +x run.sh
	./run.sh

plot: ## Gera os gráficos a partir do CSV (plot.py)
	@echo "--- Gerando Gráficos ---"
	python3 plot.py

setup: ## Instala dependências Python (pandas, seaborn)
	@echo "Instalando bibliotecas..."
	pip install pandas seaborn matplotlib

clean: ## Remove arquivos compilados e temporários
	@echo "Limpando projeto..."
	rm -rf $(BUILD_DIR)

# --- Regra de Ajuda (Mágica) ---
help: ## Mostra esta mensagem de ajuda
	@echo "Uso: make [alvo]"
	@echo ""
	@echo "Alvos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'