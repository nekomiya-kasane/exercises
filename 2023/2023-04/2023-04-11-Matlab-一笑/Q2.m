r = 1;
w = 1;
dz = 1;
phi = 0;
f = @(t) [r * sin(w * t + phi); r * cos(w * t + phi); dz * t];

ts = 0 : 0.1 : 10 * pi;

pts = f(ts);

plot3(pts(1, :), pts(2, :), pts(3, :))
grid on
set(gca, 'GridLineStyle',':')
zlim([0, 40])