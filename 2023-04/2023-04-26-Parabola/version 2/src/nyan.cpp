#include <iostream>

#include "renderer.h"

using namespace std;

// 获取文件目录
std::string getDirectory(std::string in)
{
    std::string directory;
    const size_t backslashPos = in.rfind('\\');
    if (std::string::npos != backslashPos)
    {
        directory = in.substr(0, backslashPos);
    }
    return directory;
}

int main(int argc, char **argv)
{
    // 数据文件
    std::string file = ".\\data\\data.txt";
    if (argc > 1)
    {
        file = std::string(argv[1]);
    }

    auto dir = getDirectory(file);

    // 绘制背景
    Renderer renderer(dir + "\\daijin3.png");
    if (!renderer.ready())
    {
        return -1;
    }

    // 滤镜
    auto flipper = [&renderer](POINT in) -> POINT {
        return {in.x, renderer.height - in.y};
    };
    auto leftUp = [&renderer](POINT in) -> POINT {
        return {in.x / 8, (renderer.height - in.y) / 8};
    };

    // 绘制所有曲线
    setlinecolor(RGB(204, 157, 225)); // 👈 这里改线的颜色
    setlinestyle(PS_SOLID | PS_JOIN_BEVEL, 1);
    renderer.drawCurves(file, flipper);

    // 绘制猫爪
    setlinecolor(RGB(201, 142, 255)); 
    renderer.drawCurves(dir + "\\paw.txt", leftUp, true);

    int i = 0;
    std::cin >> i;

    return 0;
}
