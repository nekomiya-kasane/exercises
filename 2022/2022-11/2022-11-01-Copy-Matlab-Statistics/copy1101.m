n = 10; r = 2; m = 2;
Y1 = [54.8 55.3 53.1 56.4 55.0 55.2 54.6 53.9 54.9 55.1]';
Z1 = [51.0 51.9 49.9 53.1 51.2 51.4 49.8 50.0 50.1 51.7]';
Z2 = [1128 1108 1011 993 996 997 991 928 990 992]';
Z0 = ones(10, 1);
Z = [Z0 Z1 Z2];
Zn = inv(Z' * Z);

betaj1 = Zn * Z' * Y1;
Yj1 = Z * betaj1;
epsilonj1 = Y1 - Yj1;

z0 = [1 50.5 970]';
A1 = z0' * betaj1;
s1 = sqrt(epsilonj1' * epsilonj1) / (n - r - 1);
B1 = s1 * sqrt(1 + z0' * Zn * z0);

t = 2.3646;
C1 = [A1 - t * B1 A1 + t * B1];

Y2 = [1720 1575 1410 1595 1488 1454 1475 1375 1564 1458]';
Y = [Y1 Y2];
betaj2 = Zn * Z' * Y2;
betaj = [betaj1 betaj2];
Yj = Z * betaj;
epsilonj = Y - Yj;

Yj2 = Z * betaj2;
epsilonj2 = Y2 - Yj2;
A2 = z0' * betaj2;
s2 = sqrt(epsilonj2' * epsilonj2) / (n - r - 1);
nsgmaj = [epsilonj1' * epsilonj1 epsilonj1' * epsilonj2;
    epsilonj2' * epsilonj1 epsilonj2' * epsilonj2];
A = betaj' * z0;

D = z0' * inv(Z' * Z) * z0;
E = (m * (n - r - 1)) / (n - r - m);
F = 4.74;
G = (1 / (n - r - 1));
H = inv(nsgmaj);

[eigenvec, eigenval] = eig(nsgmaj);
[largest_eigenvec_ind_c, r] = find(eigenval == max(max(eigenval)));
largest_eigenvec = eigenvec(:, largest_eigenvec_ind_c);
largest_eigenval = max(max(eigenval));

if (largest_eigenvec_ind_c == 1)
    smallest_eigenval = max(eigenval(:, 2));
    smallest_eigenvec = eigenvec(:, 2);
else
    smallest_eigenval = max(eigenval(:, 1));
    smallest_eigenvec = eigenvec(:, 1);  
end

angle = atan2(largest_eigenvec(2), largest_eigenvec(1));
if (angle < 0)
    angle = angle + 2 * pi;
end
avg = A;
chisquare_val = 2.4477;
theta_grid = linspace(0, 2 * pi);
phi = angle;
X0 = avg(1);
Y0 = avg(2);
a = chisquare_val * sqrt(largest_eigenval);
b = chisquare_val * sqrt(smallest_eigenval);
ellipse_x_r = a * cos(theta_grid);
ellipse_y_r = b * sin(theta_grid);
R = [cos(phi) sin(phi); -sin(phi) cos(phi)];
r_ellipse = [ellipse_x_r; ellipse_y_r]' * R;

plot(r_ellipse(:, 1) + X0, r_ellipse(:, 2) + Y0, '-');
hold on;
hXLabel = xlabel("Y01");
hYLabel = ylabel("Y02");
title("The 95% prediction ellipse for both SaleHt and SaleWt");
