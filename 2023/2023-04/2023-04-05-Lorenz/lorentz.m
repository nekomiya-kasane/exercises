sigma = 10;
b = 8 / 3;
r = 22;

init = [-10, -10, 10];
T = [0, 100];

f = @(t, x) [ ...
    sigma * (x(2) - x(1)); ...
    r * x(1) - x(2) - x(1) * x(3); ...
    x(1) * x(2) - b * x(3)
    ];

[t, x] = ode45(f, T, init);

figure(1)
plot3(x(:, 1), x(:, 2), x(:, 3))

figure(2)
plot(x(:, 1), x(:, 3))

x(end, :)