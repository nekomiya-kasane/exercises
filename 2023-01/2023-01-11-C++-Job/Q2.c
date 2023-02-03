#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <stdlib.h>

char** str_split(char* a_str, const char a_delim, int* num)
{
  char** result = 0;
  int count = 0;
  char* tmp = a_str;
  char* last_comma = 0;
  char delim[2];
  delim[0] = a_delim;
  delim[1] = 0;

  while (*tmp)
  {
    if (a_delim == *tmp)
    {
      count++;
      last_comma = tmp;
    }
    tmp++;
  }

  count += last_comma < (a_str + strlen(a_str) - 1);

  count++;

  result = malloc(sizeof(char*) * count);

  if (result)
  {
    size_t idx = 0;
    char* token = strtok(a_str, delim);

    while (token)
    {
      *(result + idx++) = strdup(token);
      token = strtok(0, delim);
    }
    *(result + idx) = 0;
  }

  *num = count;

  return result;
}

typedef struct {
  int index;
  int count;
} Map;

typedef struct {
  int index;
  int* images;
  int count;
} Pair;

typedef struct {
  Pair* data;
  int len;
} PairVec;

Map* maps;
int maps_len;

int add_to_maps(int index) {
  for (int i = 0; i < maps_len; ++i) {
    if (maps[i].index == index) {
      return 0;
    }
  }
  maps = (Map*)realloc(maps, sizeof(Map) * (maps_len + 1));
  maps_len++;
  maps[maps_len - 1].count = 0;
  return 1;
}

int set_visited(int index) {
  for (int i = 0; i < maps_len; ++i) {
    if (maps[i].index == index) {
      maps[i].count = 1;
      return 1;
    }
  }
  return 0;
}

Pair* get_pair(PairVec pairs, int index) {
  for (int i = 0; i < pairs.len; ++i) {
    if (pairs.data[i].index == index) {
      return &pairs.data[i];
    }
  }
  return NULL;
}

int main() {
  maps = NULL;
  maps_len = 0;

  char buf[128];
  int count;
  if (fgets(buf, sizeof buf, stdin) != NULL) {
    char** res = str_split(buf, ':', &count);
    if (count != 2) {
      return -1;
    }

    sscanf(res[0], "%d", &count);
    free(res);
  }

  maps = (Map*)malloc(sizeof(Map) * count);
  maps_len = count;

  PairVec pairs = { (Pair*)malloc(sizeof(Pair) * count), count };
  for (int i = 0; i < count; ++i) {
    if (fgets(buf, sizeof buf, stdin) != NULL) {
      char** res = str_split(buf, ':', &pairs.data[i].index);
      if (pairs.data[i].index != 2) {
        return -1;
      }

      sscanf(res[0], "%d", &pairs.data[i].index);
      char* content = res[1];
      free(res);

      content++;
      content[strlen(content) - 1] = '\0';

      res = str_split(buf, ',', &pairs.data[i].count);
      pairs.data[i].images = (int*)malloc(sizeof(int) * pairs.data[i].count);

      for (int k = 0; k < pairs.data[i].count; ++k) {
        sscanf(res[k], "%d", &pairs.data[i].images[k]);
      }
    }
  }

  for (int i = 0; i < pairs.len; ++i) {
    for (int j = 0; j < pairs.data[i].count; ++j) {
      add_to_maps(pairs.data[i].images[j]);
    }
  }

  while ()
}