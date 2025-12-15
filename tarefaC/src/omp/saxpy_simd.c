#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <omp.h>

#ifdef _WIN32
    #include <malloc.h>
#endif

double get_time() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + tv.tv_usec * 1e-6;
}

void saxpy_simd(int n, float a,
                float *restrict x,
                float *restrict y) {

    #pragma omp simd aligned(x,y:64)
    for (int i = 0; i < n; i++) {
        y[i] = a * x[i] + y[i];
    }
}

void init_arrays(int n, float *x, float *y) {
    for (int i = 0; i < n; i++) {
        x[i] = (float)(i % 100) / 10.0f;
        y[i] = (float)(i % 50) / 5.0f;
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Uso: %s <tamanho>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    float a = 2.5f;

    float *x = NULL;
    float *y = NULL;

#ifdef _WIN32
    x = (float*) _aligned_malloc(n * sizeof(float), 64);
    y = (float*) _aligned_malloc(n * sizeof(float), 64);
#else
    if (posix_memalign((void**)&x, 64, n * sizeof(float)) != 0 ||
        posix_memalign((void**)&y, 64, n * sizeof(float)) != 0) {
        fprintf(stderr, "Erro ao alocar memória\n");
        return 1;
    }
#endif

    if (!x || !y) {
        fprintf(stderr, "Erro ao alocar memória\n");
        return 1;
    }

    init_arrays(n, x, y);

    saxpy_simd(n, a, x, y);
    init_arrays(n, x, y);

    double start = get_time();
    saxpy_simd(n, a, x, y);
    double end = get_time();

    double time_ms = (end - start) * 1000.0;

    double checksum = 0.0;
    for (int i = 0; i < n; i++) {
        checksum += y[i];
    }

    printf("simd,%d,1,%.6f,%.2f\n", n, time_ms, checksum);

#ifdef _WIN32
    _aligned_free(x);
    _aligned_free(y);
#else
    free(x);
    free(y);
#endif

    return 0;
}
