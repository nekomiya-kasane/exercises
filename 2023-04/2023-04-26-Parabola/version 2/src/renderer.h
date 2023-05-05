#ifndef RENDERER_H
#define RENDERER_H

#include <string>
#include <functional>

#include "graphics.h"

class Renderer
{
public:
    Renderer(std::string backgroundPath);
    ~Renderer();

    inline bool ready() const { return width > 1 && height > 1; }

    bool drawCurves(std::string dataPath, std::function<POINT(POINT)> transformer, bool polygon = false);

    int width = -1, height = -1;
    IMAGE backgroundImage;

    size_t grid = 500;
};

#endif