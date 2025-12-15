// Tarefa A
/*
Variantes ∈ {1, 2, 3} 
N ∈ {100000, 500000, 1000000}     
K ∈ {20, 24, 28}
Threads: {1, 2, 4, 8, 16}
*/
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

// Função Fibonacci recursiva de maneira serializada
int fibo(int n){
    //int r1, r2;
    if (n < 2){
        return n;
    }
    return fibo(n-1) + fibo(n-2);
}

int main(int argc, char *argv[]){
    int *resultados, i; //resultado
    double start_time, end_time, elapsed_time; //tempo de parede
    int variante; //seleção da variante do código
    int numero_threads; //número de threads
    int N; //número de iterações
    int tamanho_chunk; //tamanho do chunk para a simulação desejada
    int K; //para dividir a carga

    // checando se existem os argumentos necessários
    if(argc != 6){
        // ./tarefaA variante tamanho_chunk N K numero_threads 
        printf("Uso: %s <numero inteiro> <numero inteiro> <numero inteiro> <numero inteiro> <numero inteiro>\n", argv[0]);
        return 1;
    }
    // transformando input char em int
    variante = atoi(argv[1]);
    tamanho_chunk = atoi(argv[2]);
    N = atoi(argv[3]);
    K = atoi(argv[4]);
    numero_threads = atoi(argv[5]);

    // alocando memória para os resultados
    resultados = (int *)malloc(N * sizeof(int));

    // configuração do número de threads a ser usada
    omp_set_num_threads(numero_threads);
    printf("Número de threads: %d\n", omp_get_max_threads());

    // início da contagem do tempo
    start_time = omp_get_wtime();
    // seleção da variante
    switch (variante){
    case 1:
        #pragma omp parallel for schedule(static)
            for(i = 0; i < N - 1; i++){
                resultados[i] = fibo(i % K);
            }
        break;
    case 2:

        break;
    case 3:
        
        break;
    default:
        printf("Erro.\n");
        break;
    }
    end_time = omp_get_wtime();
    elapsed_time = end_time - start_time;
    printf("Tempo despendido: %f\n", elapsed_time);

    // salvando resultados em csv
    // abrindo arquivo
    FILE *arquivo = fopen("src/tarefaA/tarefaA_resultados.csv", "a+");

    // checa abertura
    if(arquivo==NULL){
        perror("Erro ao abrir arquivo. Suspensão de salvamento do resultado.\n");
    }
    else{
        // colunas
        // variante tamanho_chunk N K numero_threads tempo
        fprintf(arquivo, "%d,%d,%d,%d,%d,%f\n", variante, tamanho_chunk, N, K, numero_threads, elapsed_time);
        fclose(arquivo);
    }
    return 0;
}