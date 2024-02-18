#include "renderer.h"
#include "curve.h"

Renderer::Renderer(std::string backgroundPath) {
    loadimage(&backgroundImage, _T(backgroundPath.data()));
    width = backgroundImage.getwidth();
    height = backgroundImage.getheight();

    initgraph(width, height, SHOWCONSOLE);
    cleardevice();

    putimage(0, 0, &backgroundImage);
}

Renderer::~Renderer() {
    closegraph();
}

bool Renderer::drawCurves(std::string dataPath, std::function<POINT(POINT)> transformer, bool closed) {
    auto curves = loadCurvesFromFile(dataPath);
    if (curves.empty())
        return false;

    for (auto curve : curves) {
        // sampling
        double h = (curve.upperBound - curve.lowerBound) / (grid - 1);

        auto knots = new POINT[grid];
        auto t = curve.lowerBound;
        for (int i = 0; i < grid; ++i) {
            auto knot = transformer(curve.evaluate(t));
            knots[i].x = knot.x;
            knots[i].y = knot.y;
            t += h;
        }
        closed ? polygon(knots, grid) : polyline(knots, grid);
        delete[] knots;
    }
    return true;
}
