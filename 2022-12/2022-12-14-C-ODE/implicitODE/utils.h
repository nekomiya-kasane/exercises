#ifndef UTILS_H
#define UTILS_H

#include <stddef.h>

#include "vector.h"

// t, y, yp0, max_iter
typedef double (*RK_func)(double, double, double, long);

double composite_simpson(vector* iVec, double h);
vector* quadrate_interp(vector* iXsEval, vector* iXs, vector* iYs);
int runge_kutta(
	RK_func f, double t0, double y0, double h, long n,
	vector** oTs, vector** oYs);

inline double absd(double iVar) {
	return iVar < 0 ? -iVar : iVar;
}

#endif // UTILS_H