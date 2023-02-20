#include <iostream>
#include <fstream>
#include <sstream>

struct Arguments {
	double sigma = 0.;
	double kappa = 0.;
	double theta = 0.;

	double Xr = 0.;
};

double q(double t, double T, Arguments args) {
	return args.sigma * args.sigma * std::pow((1 - std::exp(-args.kappa * (T - t))), 3) 
		/ (4 * args.kappa * args.kappa);

}

double ksq(double t, double T, const Arguments& args) {
	return args.sigma * args.sigma * (
			(3 * std::exp(-args.kappa * (T - t))) - 
			2 * std::exp(-2 * args.kappa * (T - t)) + 
			args.kappa * (T - t) - 1
		) / (2 * std::pow(args.kappa, 3));
}

double n(double r, double t, double T, const Arguments& args) {
	return r * (T - t) / 3 -
		(args.theta - r) * (1 - std::exp(-2 * args.kappa * (T - t))) / (4 * args.kappa);
}

double m(double r, double t, double T, const Arguments& args) {
	return std::exp(-args.kappa * (T - t))* r + (1 - std::exp(-args.kappa * (T - t))) * args.theta;
}

double vsq(double t, double T, const Arguments& args) {
	return args.sigma * args.sigma * (1 - std::exp(-3 * args.kappa * (T - t)))
		/ (3 * args.kappa);
}

double f(double r, double t, double T, const Arguments& args) {
	return m(r, t, T, args) - 2 * q(t, T, args);
}

double P(double r, double t, double T, const Arguments& args) {
	return std::exp(ksq(t, T, args) * 2. / 3. - n(r, t, T, args) / 4);
}

double V(double r, double t, double T, const Arguments& args) {
	return 0.5 * std::erfc(-(args.Xr - f(r, t, T, args)) / std::sqrt(2 * vsq(t, T, args)));
}

int main()
{
	Arguments args = {
		.sigma = 0.0277, .kappa = 0.1416, .theta = 0.067, .Xr = 0.05
	};

	double t = 0, T = 6, q2res = V(0.0265, t, T, args);

	std::cout << "Question 2 result: " << q2res << std::endl;

	// Q3
	std::fstream file("result.csv", std::ios::ate | std::ios::out);

	if (!file.is_open()) {
		std::cout << "Failed to open file." << std::endl;
		return -1;
	}

	int N = 100;
	double step = 0.2 / (N - 1);
	double r = 0;

	std::cout << "\nQuestion 3 result: (r, P, V)\n" << std::endl;
	for (int i = 0; i < N; ++i, r += step) {
		std::stringstream stream;
		stream << r << "," << P(r, t, T, args) << "," << V(r, t, T, args) << std::endl;
		std::cout << stream.str();
		file << stream.str();
	}

	file.close();
	return 0;
}
