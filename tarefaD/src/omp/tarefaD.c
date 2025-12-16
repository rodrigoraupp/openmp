
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(int argc, char **argv) {

    if (argc < 3) {
        printf("ERRO: Argumentos insuficientes.\n");
        printf("Uso: %s <N_Tamanho> <Num_Threads>\n", argv[0]);
        return 1; // Retorna código de erro
    }

    int N = atoi(argv[1]);
    // int N = 100000;
    // int N = 500000;
    // int N = 1000000;

    int n_threads = atoi(argv[2]);
    // int n_threads = 1;
    // int n_threads = 2;
    // int n_threads = 4;
    // int n_threads = 8;
    // int n_threads = 16;
    omp_set_num_threads(n_threads);

    if (N <= 0 || n_threads <= 0) {
        printf("ERRO: N e Num_Threads devem ser maiores que zero.\n");
        return 1;
    }

    // Aloca vetor
    int *vetor1 = (int*) malloc(N * sizeof(int));
    int *vetor2 = (int*) malloc(N * sizeof(int));

    // Preenche o vetor com valores simples (ou aleatórios)
    for (int i = 0; i < N; i++) {
        vetor1[i] = i+1;
        vetor2[i] = i+1+N;
    }

    //-------------------------------
    // Variante Ingênua
    //-------------------------------

    long long soma_ing = 0;
    long long mult_ing = 0;

    int i, j;

    double t1_ing = omp_get_wtime();

    #pragma omp parallel
    {
        #pragma omp for reduction(+:soma_ing)
        for (i = 0; i < N; i++) {
        soma_ing += vetor1[i] + vetor2[i];
        }
    }

    #pragma omp parallel
    {
        #pragma omp for reduction(+:mult_ing)
        for (j = 0; j < N; j++) {
        mult_ing += (long long)vetor1[j] * vetor2[j];
        }
    }

    double t2_ing = omp_get_wtime();
    double tempo_ing = t2_ing - t1_ing;

    //-------------------------------
    // Variante Arruamda
    //-------------------------------

    long long soma_arru = 0;
    long long mult_arru = 0;

    double t1_arru = omp_get_wtime();

    #pragma omp parallel
    {
        #pragma omp for reduction(+:soma_arru)
        for (i = 0; i < N; i++) {
        soma_arru += vetor1[i] + vetor2[i];
        }

        #pragma omp for reduction(+:mult_arru)
        for (j = 0; j < N; j++) {
        mult_arru += (long long)vetor1[j] * vetor2[j];
        }
    }

    double t2_arru = omp_get_wtime();
    double tempo_arru = t2_arru - t1_arru;

    //-------------------------------
    // RESULTADOS
    //-------------------------------
    printf("\n--- RESULTADOS ---\n");
    printf("Soma Ingenua = %lld\n", soma_ing);
    printf("Soma Arrumada   = %lld\n", soma_arru);

    if (soma_ing == soma_arru)
        printf("As somas sao iguais ✓\n");
    else
        printf("As somas sao diferentes ✗\n");

        printf("Soma Ingenua = %lld\n", mult_ing);
    printf("Soma Arrumada   = %lld\n", mult_arru);

    if (mult_ing == mult_arru)
        printf("As multiplicações sao iguais ✓\n");
    else
        printf("As multiplicações sao diferentes ✗\n");

    printf("\nTempo Ingenua = %f s\n", tempo_ing);
    printf("Tempo Arrumada   = %f s\n", tempo_arru);

    if (tempo_arru > 0)
        printf("Speedup = %.4f\n", tempo_ing / tempo_arru);

    // Imprime no CSV
    printf("RESULTADO_CSV;%d;%d;%f;%f\n", N, n_threads, tempo_ing, tempo_arru);

    free(vetor1);
    free(vetor2);
    return 0;
}
