#include <stdio.h>
#include <stdlib.h>

void fibon_rec(long long* res, long long next_index, long long n) {
    if (next_index > n)
        return;
    res[next_index] = res[next_index - 1] + res[next_index - 2];
    fibon_rec(res, ++next_index, n);
}

void fibon_for(long long* res, long long n) {
    long long arr0 = res[0], arr1 = res[1];
    long long next = arr0 + arr1;
    
    for (int i = 2; i <= n; i++) {
        res[i] = next;
        arr0 = arr1;
        arr1 = next;
        next = arr0 + arr1;
    }
}

// stackoverflow versions
long long fibon_rec_single(long long first, long long second, long long index) {
    if (!index)
        return first;
    else if (index == 2)
        return second;
    else if (index < 0)
        return 0;
    return fibon_rec_single(first, second, index - 1) 
        + fibon_rec_single(first, second, index - 2);
}

long long fibon_for_for(long long first, long long second, long long index) {
    if (!index)
        return first;
    else if (index == 2)
        return second;
    else if (index < 0)
        return 0;
    long long tmp = first + second;
    for (long long i = 0; i < index; i++) {
        first = second;
        second = tmp;
        tmp = first + second;
    }
    return tmp;
}

void plot(long long *arr, long n, int factor) {
  printf("\n");
  for (long i = 1; i <= n; i++) {
    printf("%2ld", i);
    long sq = i * i;
    for (long j = 0; 
        j <= ((arr[i] > sq ? arr[n] : sq) + factor - 1) / factor;
        j++) {
      if (j == sq / factor) {
        printf("%c", '+');
      }
      if (j == arr[i] / factor) {
        printf("%c", '*');
      }
      if (j != (sq / factor) && j != (arr[i] / factor)) {
        printf("%c", ' ');
      }
    }
    printf("\n");
  }
  printf("\t+ f(n) = n ^ 2\t\t * f(n) = f(n - 1) + f(n - 2) with f(0) = f(1) = 1");
}

int main() {
    long long n = 70;
    long long* arr1 = (long long*)malloc(sizeof(long long) * (n + 1));
    long long* arr2 = (long long*)malloc(sizeof(long long) * (n + 1));
    if (!arr1 || !arr2) {
      return 1;
    }

    arr1[0] = arr2[0] = arr1[1] = arr2[1] = 1;

    fibon_rec(arr1, 2, n);
    fibon_for(arr2, n);

    printf("\nFibonacci numbers by fibon_res [2-70]:\n");
    for (long long i = 2; i <= n; i++)
        printf("%lld ", arr1[i]);
    printf("\nFibonacci numbers by fibon_for [2-70]:\n");
    for (long long i = 2; i <= n; i++)
        printf("%lld ", arr2[i]);
    //// stackoverflow version
    // printf("\nFibonacci numbers by fibon_res_single [2-70]:\n");
    // for (long long i = 2; i <= n; i++)
    //   printf("%lld ", fibon_rec_single(1, 1, i));
    // printf("\nFibonacci numbers by fibon_for_single [2-70]:\n");
    // for (long long i = 2; i <= n; i++)
    //   printf("%lld ", fibon_for_for(1, 1, i));

    // window's width too small, so we multiply it with an integer factor
    plot(arr1, 14, 3); 

    free(arr1);
    free(arr2);
    return 0;
}

