# Mini Task 1 By 10767474

### Results

|  $S$  |     $d_1$      |     $d_2$      | $\Pi (S, 0)$ |
| :---: | :------------: | :------------: | :----------: |
| 11250 | -0.2485113066  | -0.5180052177  | 1496.971582  |
| 12000 | -0.1857056206  | -0.4551995318  | 1556.829855  |
| 12750 | -0.1259630041  | -0.3954569153  | 1598.258422  |
| 13500 | -0.06913406943 | -0.3386279806  | 1620.188695  |
| 14250 | -0.01507671457 | -0.2845706257  | 1621.873506  |
| 15000 | 0.03634423198  | -0.2331496792  | 1602.851833  |
| 15750 | 0.08525734937  | -0.1842365618  | 1562.911411  |
| 16500 |  0.1317849459  | -0.1377089653  | 1502.051401  |
| 17250 |  0.1760433647  | -0.09345054642 | 1420.446675  |
| 18000 |  0.218143275   | -0.05135063613 | 1318.414731  |
| 18750 |  0.2581899485  | -0.01130396269 | 1196.385835  |

<center>Table 1: Results of the calculation</center>

### Codes

```c++
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

double N(double x) { // CDF of standard normal distribution
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

    // output header
    std::cout << "S\t" << "d_1\t\t" << "d_2\t\t" << "Π(S, 0)" << std::endl; 

    // calculate at each S and output
    std::for_each(Ss.cbegin(), Ss.cend(), [](double S) mutable -> void {
        auto rd1 = d1(S, 0), rd2 = d2(S, 0);
    auto tmp = capital_pi(S, 0);
    std::cout << std::setprecision(10) << S << "\t" << rd1 << "\t" << rd2 << "\t" << tmp << std::endl;
        });

    return 0;
}
```

