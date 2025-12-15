# REPRODUCIBILIDADE - Tarefa C: SAXPY com SIMD

## 1. Ambiente de Execução

### Sistema Operacional
```bash
$ uname -a
Linux alan-Aspire-A315-54 6.8.0-87-generic #88-Ubuntu SMP PREEMPT_DYNAMIC 
Sat Oct 11 09:28:41 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
```
- **OS**: Ubuntu 24.04 LTS
- **Kernel**: 6.8.0-87-generic

### Compilador
```bash
$ gcc --version
gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0

$ gcc -fopenmp -dM -E - < /dev/null | grep -i openmp
#define _OPENMP 201511
```
- **GCC**: 13.3.0
- **OpenMP**: 4.5 (201511)

### CPU
```bash
$ lscpu
Model name:               Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz
CPU(s):                   8
Thread(s) per core:       2
Core(s) per socket:       4
CPU max MHz:              4200.0000
L3 cache:                 6 MiB
Flags:                    ... avx avx2 ...
```
- **CPU**: Intel Core i5-10210U (10ª geração)
- **Cores/Threads**: 4 cores / 8 threads
- **Frequência**: 1.6-4.2 GHz
- **SIMD**: AVX, AVX2
- **Cache L3**: 6 MB

---

## 2. Flags de Compilação

```makefile
CC = gcc
CFLAGS = -O2 -Wall -Wextra
OMPFLAGS = -fopenmp
```

| Flag       | Propósito                          |
|------------|------------------------------------|
| `-O2`      | Otimização (habilita vetorização)  |
| `-fopenmp` | Habilita OpenMP                    |

---

## 3. Parâmetros dos Experimentos

- **Tamanhos (N)**: 100.000, 500.000, 1.000.000
- **Threads**: 1, 2, 4, 8, 16 (apenas Parallel+SIMD)
- **Repetições**: 5 por configuração
- **Constante `a`**: 2.5
- **Alinhamento**: 64 bytes

---

## 4. Reprodução dos Experimentos

```bash
# 1. Clonar e entrar no diretório
git clone https://github.com/rodrigoraupp/openmp
cd tarefaC

# 2. Compilar
make all

# 3. Executar experimentos
make run

# 4. Gerar gráficos
make plot
```

---

## 5. Dependências

```bash
sudo apt update

# Compilação
sudo apt-get install build-essential gcc

# Gráficos
sudo apt install -y python3-numpy python3-matplotlib
```

---

## 6. Configuração Opcional (Testes Estáveis)

```bash
# Fixar frequência da CPU
sudo cpupower frequency-set -g performance

# Variáveis OpenMP
export OMP_PROC_BIND=true
export OMP_PLACES=cores
export OMP_DYNAMIC=false
```

**Nota**: Testes foram executados com configuração padrão do sistema (governor `powersave`).

---

## 7. Resumo do Ambiente

| Item           | Valor                     |
|----------------|---------------------------|
| **SO**         | Ubuntu 24.04              |
| **GCC**        | 13.3.0                    |
| **CPU**        | Intel i5-10210U           |
| **Cores**      | 4 cores / 8 threads       |
| **SIMD**       | AVX2                      |
| **OpenMP**     | 4.5                       |
