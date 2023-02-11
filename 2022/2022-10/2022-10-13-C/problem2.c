#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sort(long *arr, long n) {
  for (long i = 0; i < n; i++)
    printf("%ld ", arr[i]);
  printf("\n");
  for (long i = 1; i < n; i++) {
    long j = i;
    while (j >= 1 && arr[j] < arr[j - 1]) {
      long tmp = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = tmp;
      --j;
    }
  }
  for (long i = 0; i < n; i++)
    printf("%ld ", arr[i]);
  printf("\n");
}

void partition(long *A, long left, long right, long *pos) {
  long data = A[left];
  long i;
  for (*pos = left, i = left + 1; i <= right; i++) {
    if (A[i] < data) {
      (*pos)++;
      long tmp = A[*pos];
      A[*pos] = A[i];
      A[i] = tmp;
    }
  }
  long tmp = A[left];
  A[left] = A[*pos];
  A[*pos] = tmp;
}

double find_mid_with_sorting(long *arr, long n) {
  sort(arr, n);
  if ((n & 0b1) || (arr[n / 2 - 1] == arr[n / 2])) {
    return arr[n / 2];
  }
  return (arr[n / 2 - 1] + arr[n / 2]) / 2.;
}

double find_mid_without_sorting(long *arr, long n) {
  long left = 0;
  long right = n - 1;
  long mid = (left + right) / 2;
  long pos, count = 1;
  while (1) {
    partition(arr, left, right, &pos);
    if (pos == mid)
      break;
    else if (pos > mid)
      right = pos - 1;
    else
      left = pos + 1;
  }
  if (n & 0b1 || (arr[mid] == arr[mid + 1])) {
    return arr[mid];
  }
  return (arr[mid] + arr[mid + 1]) / 2.;
}

int main() {
  long n = 0;
  (void)scanf("%ld", &n);
  long *arr = (long *)malloc(sizeof(long) * n);

  for (long i = 0; i < n; i++) {
    (void)scanf("%ld", arr + i);
  }

  long *arrp = (long *)malloc(sizeof(long) * n);
  memcpy(arrp, arr, sizeof(long) * n);

  //// find median with sorting
  printf("\nThe median is [with sorting]: %.1f\n",
         find_mid_with_sorting(arr, n));

  //// find median without sorting
  // find min first
  printf("\nThe median is [without sorting]: %.1f\n",
         find_mid_without_sorting(arrp, n));

  free(arr);
  free(arrp);

  return 0;
}