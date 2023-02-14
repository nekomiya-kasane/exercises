clear all;
clf reset;
close all;

global g;
global l;
g = 9.8;
l = 1; % rope length

torad = @(t) t / 180 * pi;

span = 0:0.005:10;

opts = odeset('RelTol', 1e-8, 'AbsTol', 1e-8);

ds = 1 : 45;

min_err = zeros(length(ds), 1);
max_err = zeros(length(ds), 1);

for i = ds
    y0 = [torad(i) 0]'; % theta w
    [ts1, ys1] = ode45(@advance, span, y0, opts);
    [ts2, ys2] = ode45(@advance_approx, span, y0, opts);
    
    diff = ys1(:, 1) - ys2(:, 1);
    min_err(i) = min(diff);
    max_err(i) = max(diff);
end
mid_err = 0.5 * (min_err + max_err);
abs_err = max(abs(min_err), abs(max_err));

figure;
plot(ds, mid_err, "displayname", "Average Error")
hold on
errorbar(ds, mid_err, min_err, max_err, "displayname", "Error Bar")
plot(ds, abs_err, "displayname", "Max Error");
title("Error of two ODE");
xlabel("Degree")
ylabel("Angle Error")
legend()
hold off

function dy = advance(~, y)
    global g;
    global l;
    
    % d theta / dt = w
    % d w / dt = -g sin theta / l
    dy = [y(2); -g * sin(y(1)) / l];
end

function dy = advance_approx(~, y)
    global g;
    global l;
    
    % d theta / dt = w
    % d w / dt = -g theta / l
    dy = [y(2); -g * y(1) / l];
end