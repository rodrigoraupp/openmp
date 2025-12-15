CC = gcc
CFLAGS = -O2 -Wall -Wextra
OMPFLAGS = -fopenmp
LDFLAGS = -lm

# Alvos dos executáveis
SEQ = saxpy_seq
SIMD = saxpy_simd
PARALLEL = saxpy_parallel_simd

# Código fonte
SRC_SEQ = src/seq/saxpy_seq.c
SRC_SIMD = src/omp/saxpy_simd.c
SRC_PARALLEL = src/omp/saxpy_parallel_simd.c

.PHONY: all seq omp clean run plot help

# Compilar tudo
all: seq omp

# Compilar versão sequencial
seq: $(SEQ)

$(SEQ): $(SRC_SEQ)
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS)

# Compilar versões OpenMP (SIMD e Parallel+SIMD)
omp: $(SIMD) $(PARALLEL)

$(SIMD): $(SRC_SIMD)
	$(CC) $(CFLAGS) $(OMPFLAGS) $< -o $@ $(LDFLAGS)

$(PARALLEL): $(SRC_PARALLEL)
	$(CC) $(CFLAGS) $(OMPFLAGS) $< -o $@ $(LDFLAGS)

# Executar experimentos
run: all
	@echo "Executando experimentos..."
	@bash run.sh

# Gerar gráficos
plot:
	@echo "Gerando gráficos..."
	@python3 plot.py

# Limpar arquivos compilados
clean:
	rm -f $(SEQ) $(SIMD) $(PARALLEL)
	rm -rf results/

# Ajuda
help:
	@echo "Makefile - Tarefa C: SAXPY com OpenMP"
	@echo ""
	@echo "Alvos disponíveis:"
	@echo "  make all     - Compila todas as versões"
	@echo "  make seq     - Compila apenas versão sequencial"
	@echo "  make omp     - Compila versões OpenMP (SIMD e Parallel)"
	@echo "  make run     - Executa experimentos (gera CSV)"
	@echo "  make plot    - Gera gráficos dos resultados"
	@echo "  make clean   - Remove executáveis e resultados"
	@echo "  make help    - Mostra esta mensagem"
	@echo ""
	@echo "Uso típico:"
	@echo "  make all && make run && make plot"