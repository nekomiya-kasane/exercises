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