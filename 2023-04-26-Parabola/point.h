#include "common.h"

typedef struct {
    double x;
    double y;
} Point;

extern Point origin; 

typedef Point* PointVec;

PointVec create_points(long count, boolean init = TRUE, Point refPoint = origin);

void free_points(PointVec* pointVec);



