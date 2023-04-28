#include "graphics.h"

#include "common.h"
#include "parabola.h"
#include "parser.h"

int main(int argc, char *argv[])
{
    // 读入数据文件
    std::string file = "..\\resources\\data_1.txt";
    if (argc > 1)
    {
        file = std::string(argv[1]);
    }

    // 获取目录
    std::string directory;
    const size_t last_slash_idx = file.rfind('\\');
    if (std::string::npos != last_slash_idx)
    {
        directory = file.substr(0, last_slash_idx);
    }

    // 准备缓冲区
    IMAGE img1, mask1;
    loadimage(&img1, _T((directory + "\\img1.jpg").data()));    // 底图
    loadimage(&mask1, _T((directory + "\\mask1.png").data()));  // 蒙版

    auto imgBuf  = GetImageBuffer(&img1);
    auto maskBuf = GetImageBuffer(&mask1);

    int imgWidth = img1.getwidth(), imgHeight = img1.getheight();

    // 初始化窗口
    int width = imgWidth, height = imgHeight;

    initgraph(width, height, SHOWCONSOLE);
    // setbkcolor(WHITE);
    cleardevice();

    settextcolor(RGB(163, 73, 164));
    outtextxy(5, 5, TEXT("Press backspace to exit."));

    size_t n = 100;

    std::vector<POINT *> allPts;
    do
    {
        // 解析数据文件
        Parser parser;

        if (!parser.parse(file.data()))
        {
            TRACE("Failed to open file.");
            break;
        }

        // 正规化插值点
        auto res = parser.get_data();
        // Point mi, mx;
        auto box = normalize(res, width, height);
#if 0
         mi            = box.first;
         mx            = box.second;
         int clipWidth = mx.y - mi.y, clipHeight = mx.x - mi.x;

        {
            for (int j = 0; j < width; ++j)
            {
                auto loc = i / height * clipWidth;
                if (BGR(maskBuf[loc]) < 100)
                    continue;
                auto screenX   = int((j - mi.x) / (mx.x - mi.x) * width);
                auto screenY   = int((mx.y - j) / (mx.y - mi.y) * height);
                auto screenLoc = (screenY - 1) * width + screenX;

                currentBuf[screenLoc] = RGB(BGR(imgBuf[loc]));
            }
        }
#endif
        // 着色
        auto currentBuf = GetImageBuffer();

        putimage(0, 0, &img1);

        for (int i = 0; i < height; ++i)
        {
            for (int j = 0; j < width; ++j)
            {
                auto loc       = i * height + j;
                auto maskPixel = BGR(maskBuf[loc]);

                if ((maskPixel & 0xFFFFFF) <= 0)
                {
                    if ((i / 30. - int(i / 30)) < 0.5 && (j / 30. - int(j / 30)) < 0.5)
                        currentBuf[loc] = BGR(RGB(255, 238, 198));
                }
            }
        }

        FlushBatchDraw();

        // 建立插值曲线
        setlinecolor(RGB(55, 55, 55));
        setlinestyle(PS_SOLID | PS_JOIN_BEVEL, 3);
        for (size_t i = 0; i < res.size(); ++i)
        {
            const auto &data = res[i];
            auto curve       = ParabolaIntCurve(data, ParabolaIntCurve::Type::FREE);
            auto domain      = curve.domain;

            POINT *pts = (POINT *)malloc(sizeof(POINT) * n);
            allPts.push_back(pts);

            double h = (domain.right - domain.left) / (n - 1);
            for (size_t i = 0; i < n; ++i)
            {
                auto sample = curve.evaluate(domain.left + h * i);
                pts[i].x    = LONG(sample.x);
                pts[i].y    = LONG(sample.y);
            }

            polyline(pts, (int)n);  // 对插值曲线采样并绘制近似多段线
        }

    } while (false);

    // 按退格键退出
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

    // 清理内存
    for (size_t i = 0; i < allPts.size(); ++i)
    {
        free(allPts[i]);
    }

    closegraph();
    return 0;
}