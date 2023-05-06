#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <numeric>

int main()
{
    double number;

    std::cout << "Please enter a float: ";
    std::cin >> number;

    std::string lf, rt;

    size_t bits = *reinterpret_cast<size_t*>(&number);

    size_t signbit = 1 << 63;
    size_t fraction = 1 << 52 - 1;
    size_t exponential = (1 << 63 - 1) ^ fraction;

    size_t e = bits & exponential >> 52;
    size_t f = bits & fraction;
    bool sign = signbit & bits != 0;

    if (e) { // not zero

    }
}