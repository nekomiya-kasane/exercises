#pragma once

#ifndef PARABOLA_H
#  define PARABOLA_H

#  include "common.h"

struct Point
{
  double x = 0;
  double y = 0;

  // construct point
  Point(double iX, double iY) : x(iX), y(iY) {}

  // point calculation
  Point operator+(const Point &iRight)
  {
    return Point{x + iRight.x, y + iRight.y};
  }

  Point operator-(const Point &iRight)
  {
    return Point{x - iRight.x, y - iRight.y};
  }

  friend Point operator*(double coeff, const Point &iPoint)
  {
    return Point{coeff * iPoint.x, coeff * iPoint.y};
  }

  static Point origin;
};

class Parabola
{
public:
  Point points[4];

  Parabola() { reset(); }

  inline void reset()
  {
    for (int i = 0; i < 4; ++i)
      points[i] = Point::origin;
  }

  inline void set(const Point &pt0,
                  const Point &pt1,
                  const Point &pt2,
                  const Point &pt3)
  {
    points[0] = pt0;
    points[1] = pt1;
    points[2] = pt2;
    points[3] = pt3;
  }

  inline Point evaluate(double t)
  {
#  ifdef _DEBUG
    if (t < 0 || t > 0.5)
    {
      TRACE("Param out of domain.");
    }
#  endif
    auto res = (-1 + 4 * (1 - t) * t) * points[0] +
               (1 + t * t * (-10 + 12 * t)) * points[1] +
               (t * (1 + (8 - 12 * t) * t)) * points[2] +
               (t * t * (-2 + 4 * t)) * points[3];
    return res;
  }
}

#endif