#include <math.h>

#include "utils.h"

double composite_simpson(vector* iVec, double h) {
	long n = iVec->size;
	double sm = 0;

	if (!(n % 2)) {
		--n;
	} // to odd

	for (long i = 0; i < round((n - 1) / 2); ++i) {
		sm += get_double(iVec, 2 * i) 
			+ 4 * get_double(iVec, 2 * i + 1) 
			+ get_double(iVec, 2 * i + 2);
	}

	return h * sm / 3;
}