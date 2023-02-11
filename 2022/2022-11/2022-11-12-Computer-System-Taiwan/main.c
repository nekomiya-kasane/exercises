#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <float.h>
#include <string.h>

static double average = 0, min = 0, max = 0;
static double* inputs = NULL;

void calc_average(double numbers[]) {
    int n = numbers[0];
    if (!n) {
        return;
    }
    average = 0;
    for (int i = 1; i <= n; ++i) {
        average += numbers[i];
    }
    average /= n;
}

void calc_min(double numbers[]) {
    min = DBL_MAX;
    for (int i = 1; i <= numbers[0]; ++i) {
        min = min > numbers[i] ? numbers[i] : min;
    }
}

void calc_max(double numbers[]) {
    max = DBL_MIN;
    for (int i = 1; i <= numbers[0]; ++i) {
        max = max < numbers[i] ? numbers[i] : max;
    }
}

int main(int argc, char** argv) {
    if (argc == 1) {
        printf("No param provided.");
        return 0;
    }
    
    inputs = (double*)malloc(sizeof(double) * (argc));
    inputs[0] = argc - 1;
    for (int i = 1; i < argc; ++i) {
        inputs[i] = strtod(argv[i], NULL);
    }

    pthread_t aver_t, min_t, max_t;

    pthread_create(&aver_t, NULL, (void*)calc_average, inputs);
    pthread_create(&min_t, NULL, (void*)calc_min, inputs);
    pthread_create(&max_t, NULL, (void*)calc_max, inputs);

    pthread_join(aver_t, NULL);
    pthread_join(min_t, NULL);
    pthread_join(max_t, NULL);

    printf("Average: %.3f\n", average);
    printf("Minimum: %.3f\n", min);
    printf("Maximum: %.3f\n", max);

    free(inputs);
    //printf("asdfasdfqwef q");
    return 0;
}