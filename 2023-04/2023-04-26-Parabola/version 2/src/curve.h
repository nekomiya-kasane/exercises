#ifndef CURVE_H
#define CURVE_H

#include "graphics.h"

#include <vector>
#include <string>

struct PrimitiveCurve {
    PrimitiveCurve(POINT P1, POINT P2, POINT P3, POINT P4);

    POINT evaluate(double param);

    POINT points[4];
};

class InterpolationCurve {
public:
    enum BoundaryCondition {
        FREE = 1, 
        DERIVATIVE = 2,
        CLOSED = 3,
    } bcType;

    using BC = BoundaryCondition;

    InterpolationCurve(std::vector<POINT>& points, BC type);

    POINT evaluate(double param);

    double lowerBound = 0, upperBound = 0;
protected:
    std::vector<PrimitiveCurve> m_curves;
};

std::vector<InterpolationCurve> loadCurvesFromFile(std::string path);

#endif