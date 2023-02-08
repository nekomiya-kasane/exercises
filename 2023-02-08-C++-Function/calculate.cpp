#include <cmath>

#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>

using namespace std;

const double T = 2., X = 15000., r = 0.0236, q = 0.0302, sigma = 0.1954;

double d1(double S, double t) {
    double numerator = 1 - exp(1 - S / X) + r * (T - t) * exp(1 - sigma * sigma / q);
    double denominator = cos(sigma * sigma * (T - t));
    return numerator / denominator;
}

double d2(double S, double t) {
    double numerator = 1 - exp(1 - S / X) - sigma * sqrt(T - t) * exp((r - q) / (sigma * sigma));
    double denominator = cos(sigma * sigma * (T - t));
    return numerator / denominator;
}

double N(double x) {
    return erfc(-x / sqrt(2.)) / 2.;
}

double capital_pi(double S, double t) {
    double item1 = sqrt(pow(S, 1 + r / q) * pow(X, 1 - r / q)) * exp(-r * (T - t)) * N(d1(S, t));
    double item2 = X * pow(S / X, q / r) * exp(-q * (T - t)) * N(d2(S, t));
    return item1 - item2;
}

int main()
{
    std::vector<double> Ss = { 11250, 12000, 12750, 13500, 14250, 15000, 15750, 16500, 17250, 18000, 18750 };

    std::cout << "S\t" << "d_1\t\t" << "d_2\t\t" << "Π(S, 0)" << std::endl;

    std::for_each(Ss.cbegin(), Ss.cend(), [](double S) mutable -> void {
        auto rd1 = d1(S, 0), rd2 = d2(S, 0);
    auto tmp = capital_pi(S, 0);
    std::cout << std::setprecision(10) << S << "\t" << rd1 << "\t" << rd2 << "\t" << tmp << std::endl;
        });

    return 0;
}
