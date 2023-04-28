#include <iostream>

#include "graphics.h"

using namespace std;

int main(int argc, char** argv)
{
    initgraph(800, 600, SHOWCONSOLE);
    // setbkcolor(WHITE);
    cleardevice();

    settextcolor(RGB(163, 73, 164));
    outtextxy(5, 5, TEXT("Press backspace to exit."));

    int i = 0;
    std::cin >> i;
    closegraph();
    return 0;
}
