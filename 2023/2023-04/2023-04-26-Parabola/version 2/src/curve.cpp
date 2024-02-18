#include "curve.h"

#include <iostream>
#include <fstream>

// 插值用的小段曲线
PrimitiveCurve::PrimitiveCurve(POINT P1, POINT P2, POINT P3, POINT P4)
{
    points[0].x = P1.x;
    points[0].y = P1.y;
    points[1].x = P2.x;
    points[1].y = P2.y;
    points[2].x = P3.x;
    points[2].y = P3.y;
    points[3].x = P4.x;
    points[3].y = P4.y;
}

// 计算小段上的点 P(t)
POINT PrimitiveCurve::evaluate(double t)
{
    double x = t * (-1 + 4 * (1 - t) * t) * points[0].x +
               (1 + t * t * (-10 + 12 * t)) * points[1].x +
               (t * (1 + (8 - 12 * t) * t)) * points[2].x +
               (t * t * (-2 + 4 * t)) * points[3].x;
    double y = t * (-1 + 4 * (1 - t) * t) * points[0].y +
               (1 + t * t * (-10 + 12 * t)) * points[1].y +
               (t * (1 + (8 - 12 * t) * t)) * points[2].y +
               (t * t * (-2 + 4 * t)) * points[3].y;
    POINT res = {static_cast<long>(x), static_cast<long>(y)};
    return res;
}

InterpolationCurve::InterpolationCurve(std::vector<POINT> &points, BC type)
{
    // 补充边界点
    switch (bcType = type)
    {
    case FREE:
        points.insert(points.begin(), points.front());
        points.push_back(points.back());
        break;
    case DERIVATIVE: // not implemented.
        std::cout << "Not implemented yet.\n";
        break;
    case CLOSED:
        points.insert(points.begin(), points.back());
        points.push_back(points[1]);
        points.push_back(points[2]);
        break;
    }

    // 填充插值曲线
    m_curves.reserve(points.size() - 3);
    for (int i = 1; i < points.size() - 2; ++i)
    {
        PrimitiveCurve curve(points[i - 1], points[i], points[i + 1], points[i + 2]);
        m_curves.push_back(std::move(curve));
    }

    // 插值曲线定义域
    lowerBound = 0;
    upperBound = (points.size() - 3) * 0.5;
}

// 插值曲线（整条）上的点计算 P[t]
POINT InterpolationCurve::evaluate(double t)
{
    t = t < 0 ? 0 : t;
    auto index = static_cast<size_t>(t / 0.5);
    index = min(index, m_curves.size() - 1);
    return m_curves[index].evaluate(t - index * 0.5);
}

// 读取数据文件
std::vector<InterpolationCurve> loadCurvesFromFile(std::string path)
{
    std::fstream f(path, std::ios::in);

    if (!f.is_open())
        return {};

    std::vector<InterpolationCurve> res;

    std::vector<POINT> points;
    std::string buf;
    InterpolationCurve::BC bcType = InterpolationCurve::BC::FREE;

    try
    {
        while (f >> buf)
        {
            const size_t commaPos = buf.rfind(',');
            if (std::string::npos == commaPos)
                return {};

            auto x = std::stol(buf.substr(0, commaPos));
            auto y = std::stol(buf.substr(commaPos + 1, buf.size()));
            if (y < 0)
            {
                if (y < -3)
                {
                    std::cout << "Bad location.\n";
                    return {};
                }

                InterpolationCurve::BC newBcType = static_cast<InterpolationCurve::BC>(-y);
                if (res.empty() && points.empty())
                { // first
                }
                else if (points.size() < 2)
                {
                    points.clear();
                }
                else
                { // points
                    InterpolationCurve curve(points, bcType);
                    res.push_back(std::move(curve));
                    points.clear();
                }
                bcType = newBcType;
            }
            else
            {
                points.push_back({x, y});
            }
        }
    }
    catch (std::exception &e)
    {
        std::cout << e.what() << "\n";
        return {};
    }

    return res;
}