#ifndef PARABOLA_H
#define PARABOLA_H

#include <vector>
#include <algorithm>

#include "common.h"

// 点
struct Point
{
    double x = 0;
    double y = 0;

    // construct point
    Point(double iX = 0.0, double iY = 0.0) : x(iX), y(iY) {}

    // point calculation
    Point operator+(const Point &iRight) { return Point{x + iRight.x, y + iRight.y}; }

    Point operator-(const Point &iRight) { return Point{x - iRight.x, y - iRight.y}; }

    friend Point operator*(double coeff, const Point &iPoint)
    {
        return Point{coeff * iPoint.x, coeff * iPoint.y};
    }

    friend Point operator*(const Point &iPoint, double coeff) { return coeff * iPoint; }

    static Point origin;
};

// 区间
struct Interval
{
    double left  = 0;
    double right = 0;
};

typedef std::vector<Point> PointVector;

// 曲线段
class Parabola
{
  public:
    Point points[4];

    Parabola() { reset(); }
    Parabola(const Point &pt0, const Point &pt1, const Point &pt2, const Point &pt3)
    {
        set(pt0, pt1, pt2, pt3);
    }

    inline void reset()
    {
        for (int i = 0; i < 4; ++i)
            points[i] = Point::origin;
    }

    inline void set(const Point &pt0, const Point &pt1, const Point &pt2, const Point &pt3)
    {
        points[0] = pt0;
        points[1] = pt1;
        points[2] = pt2;
        points[3] = pt3;
    }

    inline Point evaluate(double t)
    {
#ifdef _DEBUG
        if (t < 0 || t > 0.5)
        {
            TRACE("Param out of domain.");
        }
#endif
        auto res = (-1 + 4 * (1 - t) * t) * points[0] + (1 + t * t * (-10 + 12 * t)) * points[1] +
                   (t * (1 + (8 - 12 * t) * t)) * points[2] + (t * t * (-2 + 4 * t)) * points[3];
        return res;
    }

    inline Point evaluate_deriv(double t)
    {
#ifdef _DEBUG
        if (t < 0 || t > 0.5)
        {
            TRACE("Param out of domain.");
        }
#endif
        auto res = (4 * (1 - 2 * t)) * points[0] + (t * (-20 + 36 * t)) * points[1] +
                   ((1 + (16 - 36 * t) * t)) * points[2] + (t * (-4 + 12 * t)) * points[3];
        return res;
    }
};

// 插值曲线
class ParabolaIntCurve
{
  protected:
    std::vector<Parabola> _curves;

  public:
    enum class Type
    {
        FREE       = 0,
        DERIVATIVE = 1,
        PERIDOIC   = 2
    } type;

    Interval domain;

    ParabolaIntCurve(const PointVector &points,
                     Type itype       = Type::FREE,
                     Point leftDeriv  = Point::origin,
                     Point rightDeriv = Point::origin)
        : type(itype)
    {
        PointVector _points = points;
        switch (type)
        {
            case Type::FREE:
                _points.insert(_points.cbegin(), _points[0]);
                _points.push_back(_points.back());
                break;
            case Type::DERIVATIVE:
                _points.insert(_points.cbegin(), _points[1] - leftDeriv);
                _points.push_back(_points[_points.size() - 2] + rightDeriv);
                break;
            case Type::PERIDOIC:
                _points.insert(_points.cbegin(), _points.back());
                _points.push_back(_points[0]);
                _points.push_back(_points[1]);
                break;
            default:
                TRACE("Wrong type.");
                break;
        }
        regenerate(_points);
    }

    inline void regenerate(const PointVector &points)
    {
        domain.left  = 0;
        domain.right = (points.size() - 3) * 0.5;

        _curves.resize(points.size() - 3);

        for (int i = 0; i < points.size() - 3; ++i)
        {
            _curves[i].set(points[i], points[i + 1], points[i + 2], points[i + 3]);
        }
    }

    // 值计算
    inline Point evaluate(double t)
    {
        auto index = (size_t)(t / 0.5);
        index = index >= _curves.size() ? _curves.size() - 1 : index;
        return _curves[index].evaluate(t - index * 0.5);
    }

    // 导数计算
    inline Point evaluate_deriv(double t)
    {
        auto index = (size_t)(t / 0.5);
        index = index >= _curves.size() ? _curves.size() - 1 : index;
        return _curves[index].evaluate_deriv(t - index * 0.5);
    }
};

inline void normalize(std::vector<PointVector> &data, double x, double y)
{
    // 获取包围盒
    Point mi = {HUGE_VAL, HUGE_VAL};
    Point mx = {-HUGE_VAL, -HUGE_VAL};
    for (size_t i = 0; i < data.size(); ++i)
    {
        for (size_t j = 0; j < data[i].size(); ++j)
        {
            const auto &pt = data[i][j];
            mi.x           = data[i][j].x > mi.x ? mi.x : data[i][j].x;
            mi.y           = data[i][j].y > mi.y ? mi.y : data[i][j].y;
            mx.x           = data[i][j].x < mx.x ? mx.x : data[i][j].x;
            mx.y           = data[i][j].y < mx.y ? mx.y : data[i][j].y;
        }
    }

    // 正规化样点
    for (size_t i = 0; i < data.size(); ++i)
    {
        for (size_t j = 0; j < data[i].size(); ++j)
        {
            auto &pt = data[i][j];
            pt.x     = (pt.x - mi.x) / (mx.x - mi.x) * x;
            pt.y     = (pt.y - mi.y) / (mx.y - mi.y) * y;
        }
    }
}

#endif