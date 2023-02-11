#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <float.h>
#include <string.h>

static long* fibs = NULL;

void fibon(int* len) {
    int n = *len;
    fibs = NULL;
    if (!n) {
        return;
    }
    fibs = (long*)malloc(sizeof(long) * n);

    if (n > 0) {
        fibs[0] = 0;
    }
    if (n > 1) { 
        fibs[1] = 1;
    }
    for (int i = 2; i < n; i ++) {
        fibs[i] = fibs[i - 1] + fibs[i - 2];
    }
}

int main(int argc, char** argv) {
    if (argc == 1) {
        printf("No param provided.");
        return 0;
    }
    int n = strtod(argv[1], NULL);

    pthread_t generator;

    pthread_create(&generator, NULL, (void*)fibon, (void*)&n);

    pthread_join(generator, NULL);

    for (int i = 0; i < n; i++) {
        printf("%ld  ", fibs[i]);
    }

    if (fibs) {
        free(fibs);
    }
    return 0;
}