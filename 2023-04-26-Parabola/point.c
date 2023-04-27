#include <stdlib.h>

#include "point.h"

static Point origin = {0, 0};

PointVec create_points(long count, boolean init, Point refPoint) {
    PointVec points = (PointVec)malloc(sizeof(Point) * count);
    if (!init)
        return points;
    for (long i = 0; i < count; ++i) {
        points[i].x = refPoint.x;
        points[i].y = refPoint.y;
    }
    return points;
}

void free_points(PointVec* pointVec) {
    if (!pointVec || !*pointVec)
        return;
    
    free(*pointVec);
    *pointVec = NULL;
}