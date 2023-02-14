clear all;
clf reset;
close all;

xs = 0:0.4:2.8;
ys = [2, 3.5, 5, 6.3, 8, 16, 35, 86];

xs = xs';
n = length(xs);

A = [zeros(n, 1) xs xs.^2];
b = log(ys)';

coeff = A \ b;
coeff(1) = exp(coeff(1));

g = @(x) coeff(1) * exp(coeff(2) * x + coeff(3) * x);

xfs = 0:0.01:2.8;
yfs = g(xfs);

figure;
plot(xs, ys);
hold on
plot(xfs, yfs);
title("Model y=a exp(bx+cx^2)")
legend("Given curve", "Fitting curve")
xlabel("x")
ylabel("y")
hold off