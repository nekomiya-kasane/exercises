#include "common.h"

typedef struct {
    double x;
    double y;
} Point;

extern Point origin; 

typedef Point* PointVec;

PointVec create_points(long count, boolean, Point refPoint);

void free_points(PointVec* pointVec);



