#include "parabola.h"

double interpolate(double t, double x0, double x1, double x2, double x3) {
    double res = (-1 + 4 * (1 - t) * t) * x0
        + (1 + t * t * (-10 + 12 * t)) * x1
        + (t * (1 + (8 - 12 * t) * t)) * x2
        + (t * t * (-2 + 4 * t)) * x3;
    return res;
}

double parabola(double t, point P0, point P1, point P2, point P3) {
    if (t < 0 || t > 0.5) {
        TRACE("Parabola param not in the domain.");
    }

    double x = interpolate(t, P0.x, P1.x, P2.x, P3.x);
    double y = interpolate(t, P0.y, P1.y, P2.y, P3.y);
}

long find_missing_points(
    long n, pointVec points, 
    pointVec* pointsOut, 
    ExtendingMethod method,
    point tangentLeft,
    point tangentRight
) {
    if (*pointsOut) {
        *pointsOut = (pointsVec)
    }
}