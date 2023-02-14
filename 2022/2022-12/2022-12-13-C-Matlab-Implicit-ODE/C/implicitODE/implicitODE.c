// implicitODE.cpp: 定义应用程序的入口点。
//

#include "vector.h"
#include "utils.h"

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

vector* ys = NULL, * xs = NULL;

extern double xs_data[] = {
	0, 0.3149803, 0.9999999, 1.9655560, 3.1748020, 4.6050390, 6.2402510,
	8.068264, 10.07937, 12.26556, 14.62009, 17.13712, 19.81156, 22.63891,
	25.61514, 28.73660, 31.99999, 35.40231, 38.94074, 42.61273, 46.41589
};

vector* phi_vec(vector* iYsEval) {
	return quadrate_interp(iYsEval, ys, xs);
}

double phi(double iVar) {
	vector* iYsEval = new_vector(DOUBLE, 1);
	set(iYsEval, 0, iVar);
	vector* iXsEval = quadrate_interp(iYsEval, ys, xs);
	double res = get_double(iXsEval, 0);
	free_vector(&iXsEval);
	free_vector(&iYsEval);
	return res;
}

double F(double t, double y, double yp) {
	double res = pow(yp, 3) - 6 * pow(t, 3) * phi(y) * pow(y, 2) * yp
		+ pow(t, 3) * pow(phi(y), 3) + 8 * pow(t, 6) * pow(y, 6);
	return res;
}

double Fypp(double t, double y, double yp) {
	double res = 3 * pow(yp, 2) - 6 * pow(t, 3) * phi(y) * pow(y, 2);
	return res;
}

double f(double t, double y, double yp0, long max_iter) {
	const double tol = 1e-14;
	double yp = 100000;

	long i = 0;

	while (1) {
		if (i > max_iter) {
			printf("Not converging.");
			break;
		}

		yp = yp0 - F(t, y, yp0) / Fypp(t, y, yp0);
		if (absd(yp) <= tol || (absd(yp - yp0) / absd(yp)) <= tol) {
			break;
		}
		yp0 = yp;
		++i;
	}
	return yp;
}

int main()
{
	long n = 51;

	vector* yts = NULL, * yys = NULL, * yxs = NULL;

	do {
		// fill data
		long phi_n = (long)(sizeof(xs_data) / sizeof(double));
		ys = new_vector(DOUBLE, phi_n);
		if (fill_vector(ys, 0.0, 10.0, 0.5)) {
			printf("Failed to fill ys.");
			break;
		}

		xs = new_vector(DOUBLE, phi_n);
		for (long i = 0; i < phi_n; ++i) {
			set(xs, i, xs_data[i]);
		}

		// double sdaf = phi(5.12);

		// RK
		double t0 = 0.5, y0 = 8, h = 0.1;

		if (runge_kutta(f, t0, y0, h, n, &yts, &yys)) {
			printf("Failed to solve RK4.");
			break;
		}

		yxs = phi_vec(yys);

		printf("\n\n\033[31mt values:\n\033[0m");
		print_vector(yts);
		printf("\n\n\033[32my values:\n\033[0m");
		print_vector(yys);
		printf("\n\n\033[33mx values:\n\033[0m");
		print_vector(yxs);

		double res = composite_simpson(yys, h);

		printf("\n\n\033[34mIntegral value: \n\033[0m\n%.12e\n\n", res);
	} while (0);

	free_vector(&ys);
	free_vector(&xs);
	free_vector(&yts);
	free_vector(&yys);
	free_vector(&yxs);

	return 0;
}
