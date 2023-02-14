clear all;
clf reset;
close all;

[x, y] = ndgrid(linspace(-10,10,500));

h = 6;
r1 = 4;
r2 = 9;

z1 = 0 * x;
z2 = 0 * x + h;
z3 = -h * sqrt(x.^2+y.^2) / 5 + 10.8;

z1(x.^2 + y.^2 > r2^2) = NaN;
z2(x.^2 + y.^2 > r1^2) = NaN;
z3(x.^2 + y.^2 < r1^2) = NaN;
z3(x.^2 + y.^2 > r2^2) = NaN;

surf(x, y, z1,'edgecolor','none')
xlim([-10, 10])
ylim([-10, 10])
hold on
surf(x, y, z2,'edgecolor','none')
surf(x, y, z3,'edgecolor','none')
hold off 

disp("Volumn:")
disp(pi * h * (r2 ^ 2 + r1 ^ 2 + r2 * r1) / 3)
