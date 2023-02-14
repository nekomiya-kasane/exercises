#include "utils.h"

vector* quadrate_interp(vector* iXsEval, vector* iXs, vector* iYs) {
	if (!iXsEval || !iXs || !iYs || (iXs->size != iYs->size)) {
		return 0;
	}

	long n = iXs->size;
	long m = iXsEval->size;

	vector* x_boud = new_vector(DOUBLE, n - 1);
	set(x_boud, 0, get_double(iXs, 0));
	for (long i = 1; i < n - 2; ++i) {
		set(x_boud, i, 0.5 * (get_double(iXs, i) + get_double(iXs, i + 1)));
	}
	set(x_boud, n - 2, get_double(iXs, n - 1));

	long n_boud = n - 1;

	long count = 0;
	vector* oYsEval = new_vector(DOUBLE, m);
	
	for (long i = 0; i < m; ++i) {
		double x = get_double(iXsEval, i);

		long span = n_boud - 2;

		for (long j = 0; j < n_boud; ++j) {
			if (x < get_double(x_boud, j)) {
				span = j - 1;
				break;
			}
		}

		if (span == -1) {
			span = 0;
		}
		double x0 = get_double(iXs, span), 
			x1 = get_double(iXs, span + 1),
			x2 = get_double(iXs, span + 2);
		double y0 = get_double(iYs, span),
			y1 = get_double(iYs, span + 1),
			y2 = get_double(iYs, span + 2);

		double ele = y0 * (x - x1) * (x - x2) / (x0 - x1) / (x0 - x2)
			+ y1 * (x - x0) * (x - x2) / (x1 - x0) / (x1 - x2)
			+ y2 * (x - x0) * (x - x1) / (x2 - x0) / (x2 - x1);
		set(oYsEval, count, ele);

		++count;
	}

	return oYsEval;
}