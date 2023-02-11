% starting point
y0 = ones(1,10) * 0.5;

% for convenience, y0 is indexed as y10
al = [0, 0, 0, 0.10, 0.10, 0.10, 0.10, 0.75, 0.75];
be = [
    [0, 0, 0, 0.01, 0.01, 0, 0, 0, 0.01, 0.25]; % 1 -> ?
    [0, 0, 0, 0.01, 0.01, 0.01, 0, 0, 0, 0.25]; % 2 -> ?
    [0, 0, 0, 0, 0.01, 0.01, 0, 0, 0.01, 0.26]; % 3 -> ?
    [0, 0, 0, 0, 0, 0, 0.01, 0, 0.01, 0];       % 4 -> ?
    [0, 0, 0, 0, 0, 0, 0.01, 0.01, 0, 0];       % 5 -> ?
    [0, 0, 0, 0, 0, 0, 0, 0.01, 0.01, 0];       % 6 -> ?
    [0, 0, 0, 0, 0, 0, 0, 0.01, 0.01, 0];       % 7 -> ?
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.05]; % 8 -> ?
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.05]; % 9 -> ?
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; % 0 -> ? not used
    ];
be = be + (-1) * be';
gi = [0.25, 0.25, 0.26];

n = 1000;
dt = 0.1;
m = length(1:dt:n);
ys = zeros(10, n + 1);

[t,x] = ode45(@(t, y) odestep(t,y, dt, be, alpha, gi), 1:dt:n, y0);
figure(1)
plot(t,x)
legend("y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8", "y9", "y0")

% y'and y''
yp = zeros(m, 10);
ypp = zeros(m, 10);
for i = 2:m - 1
    yp(i, :) = (x(i + 1, :) - x(i, :)) / dt;
    ypp(i, :) = (x(i + 1, :) - 2 * x(i, :) + x(i - 1, :)) / dt / dt;
end
yp(1, :) = (x(2, :) - x(1, :)) / dt;
ypp(1, :) = ypp(2, :); 
% for small dt, this approximation is valid since 
% we are calculating integral
yp(m, :) = (x(m, :) - x(m - 1, :)) / dt;
ypp(m, :) = ypp(m - 1, :);

% FI
FI = zeros(1, m);
FI(1) = 0;
for i = 2:m
    R = norm(yp(i));
    FI(i) = FI(i - 1) + dot(yp(i, :), ypp(i, :)) / R ^ 6 * dt;
    if i ~= 1
        FI(i - 1) = FI(i - 1) / ((i - 1) * dt);
    end
    % prevent zero denominator
    %if abs(FI(i - 1)) > 10
    %    FI(i - 1) = 10;
    %end
end
FI(m) = FI(m) / (n - 1);
% prevent zero denominator
%if abs(FI(m)) > 10
%    FI(m) = 10;
%end

figure(2)
plot(t, FI)

% ODE step
function dy = odestep(t, y, dt, be, al, gi)
    [al, be] = modifier(t, al, be);

    dy = zeros(10, 1);
    dy(1:9) = y(1:9) .* transpose(ipdf(y, be, al));
    factor = (2/3 + sin(2 * pi * t / 12 - pi / 2) / 3) ^ 2;
    g = gi * factor;
    dy(10) = dot(al, y(1:9)) - y(10) * dot(g, y(1:3));
    % project to zero plane
    dy = dy - dot(dy, ones(1, 10)) / sqrt(10);
    % -
    dy = dy * dt;
end

function sums = ipdf(y, b, a)
    sums = zeros(1,9);
    for i = 1:9
        for j = 1:10
            if i == j
                continue
            elseif i < j && j ~= 10
                sums(i) = sums(i) - b(i, j) * y(j);
            else
                sums(i) = sums(i) + b(i, j) * y(j);
            end
        end
        sums(i) = sums(i) - a(i);
    end
end

% pertubator function
function [a, b] = modifier(t, a, b)
    if t > 300 && t < 600
        b(2, 5) = 0.09 * (t - 300) / 300 + 0.01;
    elseif t >= 600
        b(2, 5) = 0.10;
    else
        b(2, 5) = 0.01;
    end
end