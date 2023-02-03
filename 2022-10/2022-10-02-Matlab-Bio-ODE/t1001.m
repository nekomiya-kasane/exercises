clear all;

% starting point
% strong forcing function
y0 = [14.59, 32.89, 13.76, 9.16, 37.50, 11.47, 26.03, 25.19, 11.46, 7.93];
% weak forcing function
% y0 = [14.64, 22.65, 29.06, 4.01, 47.71, 6.33, 20.97, 35.39, 6.33, 2.92];

% for convenience, y0 is indexed as y10
al = [0, 0, 0, 0.10, 0.10, 0.10, 0.10, 0.75, 0.75];
be = [
    [0,    0,    0, -0.01, -0.01,     0,     0,     0, -0.01,  0.25]; % 1 -> ?
    [0,    0,    0, -0.01, -0.01, -0.01,     0,     0,     0,  0.25]; % 2 -> ?
    [0,    0,    0,     0, -0.01, -0.01,     0,     0, -0.01,  0.26]; % 3 -> ?
    [0,    0,    0,     0,     0,     0, -0.01,     0, -0.01,     0]; % 4 -> ?
    [0,    0,    0,     0,     0,     0, -0.01, -0.01,     0,     0]; % 5 -> ?
    [0,    0,    0,     0,     0,     0,     0, -0.01, -0.01,     0]; % 6 -> ?
    [0,    0,    0,     0,     0,     0,     0, -0.01, -0.01,     0]; % 7 -> ?
    [0,    0,    0,     0,     0,     0,     0,     0,     0,     0]; % 8 -> ?
    [0,    0,    0,     0,     0,     0,     0,     0,     0,     0]; % 9 -> ?
    [0,    0,    0,     0,     0,     0,     0,     0,     0,     0]; % 0 -> ? not used
    ];
be = be + (-1) * be';
gi = [0.25, 0.25, 0.26];

n = 1000;
dt = 0.1;
m = length(1:dt:n);
ys = zeros(10, n + 1);

global T
T = 12;
tn = T / dt;

[t, x] = ode45(@(t, y) odestep(t,y, dt, be, al, gi), 1:dt:n, y0); 
% solve the differential equations using 4-order runge-kutta
figure(1)
plot(t,x)
legend("y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8", "y9", "y0")

% y'and y''
% can be abtained by the given differential equations, but for
% convenience, here we adopt numerical method, i.e.
% y'(t) = (y(t + Δt) - y(t)) / Δt
% y''(t) = (y'(t + Δt) - y'(t)) / Δt 
%        = (y(t + Δt) - 2y(t) + y(t - Δt)) / Δt ^ 2
% hence
% FI = 1 / T * ∫ R'^2(t) / R''^4(t)
%    = 1 / t * Σ R'^2(t) / R''^4(t) Δt

yp = zeros(m, 10);
ypp = zeros(m, 10);
yp(1, :) = odestep(t(1), transpose(x(1, :)), dt, be, al, gi) / dt;
for i = 2:m
    % yp(i, :) = (x(i + 1, :) - x(i, :)) / dt;
    yp(i, :) = odestep(t(i), transpose(x(i, :)), dt, be, al, gi) / dt;
    % ypp(i, :) = (x(i + 1, :) - 2 * x(i, :) + x(i - 1, :)) / dt / dt;
    ypp(i, :) = (yp(i, :) - yp(i - 1, :)) / dt;
end
% yp(1, :) = (x(2, :) - x(1, :)) / dt;
ypp(1, :) = ypp(2, :); 
% for small dt, this approximation is valid since 
% we are calculating integral
% yp(m, :) = (x(m, :) - x(m - 1, :)) / dt;
% ypp(m, :) = ypp(m - 1, :);

% FI
FI = zeros(1, m);
FI(1) = 0;
resFI = zeros(1, m);
for i = 2:m
    R = norm(yp(i, 1:9));
    %dot(yp(i, 1:9), ypp(i, 1:9)) ^ 2 / R ^ 6 * dt
    FI(i) = FI(i - 1) + dot(yp(i, 1:9), ypp(i, 1:9)) ^ 2 / R ^ 6 * dt;
    if i > 24 % ???
        resFI(i) = (FI(i) - FI(24)) / (t(i) - t(24));
    end
end

figure(2)
plot(t, FI)

figure(3)
plot(t, resFI)

% ODE step
function dy = odestep(t, y, dt, be, al, gi)
    global T
    [al, be] = modifier(t, al, be);
    gi = be(1:3, 10)';

    dy = zeros(10, 1);

    factor = (2/3 + sin(2 * pi * t / T - pi / 2) / 3) ^ 2;
    g = gi * factor;

    be(1:3, 10) = g;
    be(10, 1:3) = -transpose(g);

    dy = (be * y) .* y - y .* transpose([al 0]);

    dy(10) = dot(al, y(1:9)) - y(10) * dot(g, y(1:3));
    
    % project to zero plane
    % dy = dy - dot(dy, ones(1, 10)) / sqrt(10);
    % -
    dy = dy * dt;
    % dot(ones(1,10),dy)
end

% pertubator function
function [a, b] = modifier(t, a, b)
    th = 750;
    tl = 250;
    if t > tl && t < th
        b(3, 10) = 0.09 * (t - tl) / (th - tl) + 0.26;
    elseif t >= th
        b(3, 10) = 0.35;
    else
        b(3, 10) = 0.26;
    end
    b(10, 3) = -b(3, 10);
end
% function [a, b] = modifier(t, a, b)
%     th = 750;
%     tl = 250;
%     if t > tl && t < th
%         a(9) = -0.25 * (t - tl) / (th - tl) + 0.75;
%     elseif t >= th
%         a(9) = 0.50;
%     else
%         a(9) = 0.75;
%     end
% end