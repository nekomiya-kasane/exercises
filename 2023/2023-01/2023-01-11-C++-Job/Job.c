#include "stdio.h"
#include "malloc.h"
#include "string.h"

int main()
{
	int n = 0;
	char fl[10];
	if (fgets(fl, sizeof fl, stdin) != NULL) {
		if (1 != sscanf(fl, "%d", &n)) {
			return -1;
		}
	}

	char line[20003];
	char left[10001], right[10002];

	int *res = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; ++i) {
		res[i] = 1;

		char first = '\0', second = '\0';
		int is_second = 0;

		if (fgets(line, sizeof line, stdin) != NULL) {
			if (1 == sscanf(line, "%s", left) && 1 == sscanf(line + strlen(left), "%s", right)) {
				if (strlen(left) != strlen(right))
					res[i] = -1;
				else 
				{
					for (int k = 0; k < strlen(left); ++k) {
						if (left[k] != right[k]) {
							if (!is_second && !first) {
								first = left[k];
								second = right[k];
							}
							else if (!is_second) {
								if ((first != right[k]) || (second != left[k])) {
									res[i] = -1;
									break;
								}
								is_second = 1;
							}
							else {
								res[i] = -1;
								break;
							}
						}
					}
				}
			}
		}

		if (first && !is_second) {
			res[i] = -1;
		}
	}

	for (int i = 0; i < n; ++i) {
		printf("%d ", res[i]);
	}

	free(res);
	return 0;
}
