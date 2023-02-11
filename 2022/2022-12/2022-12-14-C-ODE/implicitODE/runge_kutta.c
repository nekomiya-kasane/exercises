#include "utils.h"

int runge_kutta(
	RK_func f, double t0, double y0, double h, long n,
	vector** oTs, vector** oYs) {
	if (!oYs || !oYs) {
		return 1;
	}

	if (*oTs) {
		free_vector(oTs);
	}
	if (*oYs) {
		free_vector(oYs);
	}

	*oTs = new_vector(DOUBLE, n);
	*oYs = new_vector(DOUBLE, n);

	vector* ts = *oTs, * ys = *oYs;

	set(ts, 0, t0);
	set(ys, 0, y0);

	double k1 = 0, k2 = 0, k3 = 0, k4 = 0;
	const long max_iter = 1000;

	double yp0 = f(t0, y0, 0, max_iter);
	for (long i = 0; i < n - 1; ++i) {
		double tsi = get_double(ts, i), ysi = get_double(ys, i);
		yp0 = f(tsi, ysi, yp0, max_iter);
		k1 = h * yp0;
		k2 = h * f(tsi + 0.5 * h, ysi + 0.5 * k1, yp0, max_iter);
		k3 = h * f(tsi + 0.5 * h, ysi + 0.5 * k2, yp0, max_iter);
		k4 = h * f(tsi + h, ysi + k3, yp0, max_iter);

		set(ys, i + 1, ysi + (k1 + 2 * k2 + 2 * k3 + k4) / 6);
		set(ts, i + 1, tsi + h);
	}

	return 0;
}