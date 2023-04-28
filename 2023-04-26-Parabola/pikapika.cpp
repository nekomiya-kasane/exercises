#include "graphics.h"

#include "common.h"
#include "parabola.h"
#include "parser.h"

int main()
{
    int width = 640, height = 480;

    initgraph(width, height);
    setbkcolor(WHITE);
    cleardevice();

    settextcolor(RGB(163, 73, 164));
    outtextxy(5, 5, TEXT("Press backspace to exit."));

    size_t n = 100;

    std::vector<POINT*> allPts;
    do {
        Parser parser;

        if (!parser.parse("E:\\assignments\\2023-04-26-Parabola\\resources\\data_1.txt")) {
            TRACE("Failed to open file.");
            break;
        }

        auto res = parser.get_data();
        normalize(res, width, height);

        for (size_t i = 0; i < res.size(); ++i) {
            const auto& data = res[i];
            auto curve = ParabolaIntCurve(data, ParabolaIntCurve::Type::FREE);
            auto domain = curve.domain;

            POINT* pts = (POINT*)malloc(sizeof(POINT) * n); 
            allPts.push_back(pts);

            double h = (domain.right - domain.left) / (n - 1);
            for (size_t i = 0; i < n; ++i) {
                auto sample = curve.evaluate(domain.left + h * i);
                pts[i].x = LONG(sample.x);
                pts[i].y = LONG(sample.y);
            }

            polyline(pts, (int)n);
        }

        int i = 0;
    } while (false);

    ExMessage msg;
    bool loop = true;
    while (loop)
    {
        while (loop && peekmessage(&msg, EX_CHAR | EX_KEY | EX_MOUSE))
        {
            if (msg.ch == _T('\b'))
                loop = false;
        }
    }

    for (size_t i = 0; i < allPts.size(); ++i) {
        free(allPts[i]);
    }

    closegraph();
    return 0;
}