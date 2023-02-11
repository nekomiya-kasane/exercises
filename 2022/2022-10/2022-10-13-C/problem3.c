#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
  long key;
  long count;
} dict_ele;

double entropy(long *arr, long n) {
  // initialization
  dict_ele *dict = (dict_ele *)malloc(sizeof(dict_ele) * n);
  if (!dict) {
    return 0;
  }
  for (long i = 0; i < n; ++i) {
    dict[i].key = 0;
    dict[i].count = 0;
  }

  // calculation
  long ind = 0;
  for (long i = 0; i < n; ++i) {
    bool exist = false;
    for (long j = 0; j < ind; ++j) {
      if (dict[j].key == arr[i]) {
        dict[j].count++;
        exist = true;
        break;
      }
    }
    if (!exist) {
      dict[ind].key = arr[i];
      dict[ind].count = 1;
      ind++;
    }
  }

  double res = 0.;
  for (long i = 0; i < ind; ++i) {
    double item = dict[i].count / (double)n;
    res += item * log(item);
  }

  free(dict);
  return -res / log(2);
}

typedef struct {
  long x;
  long y;
} point;

typedef struct {
  point key;
  long count;
} dict_ele2;

bool equal(point lf, point rt) { return lf.x == rt.x && lf.y == rt.y; }

double entropy2(point *arr, long n) {
  // initialization
  dict_ele2 *dict = (dict_ele2 *)malloc(sizeof(dict_ele2) * n);
  if (!dict) {
    return 0;
  }
  for (long i = 0; i < n; ++i) {
    dict[i].key.x = 0;
    dict[i].key.y = 0;
    dict[i].count = 0;
  }

  // calculation
  long ind = 0;
  for (long i = 0; i < n; ++i) {
    bool exist = false;
    for (long j = 0; j < ind; ++j) {
      if (equal(dict[j].key, arr[i])) {
        dict[j].count++;
        exist = true;
        break;
      }
    }
    if (!exist) {
      dict[ind].key = arr[i];
      dict[ind].count = 1;
      ind++;
    }
  }

  double res = 0.;
  for (long i = 0; i < ind; ++i) {
    double item = dict[i].count / (double)n;
    res += item * log(item);
  }

  free(dict);
  return -res / log(2);
}

int main() {
  long X1[] = {4, 2, 3, 5, 3, 4, 5};
  point PS[] = {{4, 2}, {3, 5}, {3, 4}, {5, 1}, {1, 1}, {1, 1}, {2, 2}};

  printf("entropy 1: %f\n", entropy(X1, 7));
  printf("entropy 2: %f\n", entropy2(PS, 7));
}