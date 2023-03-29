%% a

K = 23;
T1 = 03;

sys = tf(K, [T1*T1, 2*T1, 1]);

figure(1)

figure('Renderer', 'painters',  'Position', [100 100 1500 600])
set(gcf,'color','w');

[y, time] = step(sys, 50);
plot(time, y)
xlabel("Time (s)")
ylabel("Amplitude")
title("Step function response")

%% b

% tangent and its max

h = time(2) - time(1);
tans = y(1:end-4)./12-2*y(2:end-3)./3+2*y(4:end-1)./3-y(5:end)./12;
tans = tans ./ h;

figure(2)

plot(time(3:end-2), tans)
[peak, loc] = findpeaks(tans);
y_peak = y(loc);
hold on
scatter(time(loc), tans(loc))
hold off

figure(3)
plot(time, y)
hold on
xlabel("Time (s)")
ylabel("Amplitude")
title("Step function response")

tan_line = @(t) tans(loc) * (t - time(loc)) + y_peak;
ts = time(1):0.01:time(end)/2;
ys = tan_line(ts);

upper_line = @(t) y(end);

plot(ts, ys)
yline([0, y(end)])
xlim([0,30])
ylim([-0.5, y(end)+0.5])
hold off

% parameter
K = y(end);

L = fsolve(tan_line,1);
disp("L = " + string(Td))

T = fsolve(@(t) y(end) - tan_line(t), 1) - Td;
disp("T = " + string(Ts))


%% c
figure(4)
Kc = 0.9 * T / L;
Ti = L / 0.3;
GPI = pidstd(Kc, Ti, 0);
sys_c = feedback(GPI * sys, 1)

step(sys_c,50)
xlabel("Time (s)")
ylabel("Amplitude")
title("Step function response")

Kc = 0.0974;
Tis = 1:2:7;

n = length(Tis);
syses = cell(1, n);
lends = ["", "", "", ""];
overshoots = [0, 0, 0, 0];

for i = 1:n
    GPI = pidstd(Kc, Tis(i), 0);
    syses{i} = feedback(GPI * sys, 1);
    lends(i) = "Ti = " + string(Tis(i));
    [y, time] = step(syses{i}, 50);
    [peak, loc] = findpeaks(y);
    overshoots(i) = y(loc(1)) - 1;
end

figure(5)
step(syses{1}, syses{2}, syses{3}, syses{4}, 50)
legend(lends)
xlabel("Time (s)")
ylabel("Amplitude")
title("Step Respondse for different Ti")

figure(6)
plot(Tis, overshoots)
title("Overshoots")
xlabel("Ti")
